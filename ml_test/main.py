import copy
import torch
from model import Net

torch.nn.Module.dump_patches = True

device = torch.device("cpu")
sign_lang_net = torch.load("model_trained.pt", map_location=device)
#sign_lang_net.eval()

print(device)
print(sign_lang_net)
print("Model Load Done.")

print("***********************************")

t = torch.randn(1, 1, 28, 28).float()
out = sign_lang_net(t)
print(out)
print(out.size())
print("Model Eval Done.")