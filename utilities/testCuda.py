import torch

print(torch.version.cuda)

print(torch.rand(5, 3))
print(torch.cuda.is_available())