import multiprocessing

import utils
from data_utils import TextAudioSpeakerLoader
from tqdm import tqdm

def preprocess(total, current):

    config_path = 'configs/config.json'
    hps = utils.get_hparams_from_file(config_path)

    train_dataset = TextAudioSpeakerLoader(hps.data.training_files, hps.data, meta=(total, current))
    eval_dataset = TextAudioSpeakerLoader(hps.data.validation_files, hps.data, meta=(total, current))

    for _ in tqdm(train_dataset):
        pass
    for _ in tqdm(eval_dataset):
        pass



if __name__ == '__main__':
    multiprocessing.set_start_method("spawn", force=True)
    num_processes = 8
    processes = [
            multiprocessing.Process(target=preprocess, args=(num_processes,i)) for i in range(num_processes)
    ]
    for p in processes:
        p.start()
