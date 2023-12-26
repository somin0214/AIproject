import torch

model = torch.load('model.pt')

model.eval()

predict = model(data)

print(predict)