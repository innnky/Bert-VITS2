import torch
ckpt_path = "logs/G_35000.pth"
save_path = 'G_35000.pth'
ckpt = torch.load(ckpt_path, map_location="cpu")
ckpt['optimizer'] = None
torch.save(ckpt, save_path)

