import torch
class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, data):
        return torch.exp(data)/sum(torch.exp(data))
    
data = torch . Tensor ([1 , 2 , 3])
softmax = Softmax()
output = softmax(data)
print(output)

class softmax_stable(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, data):
        c = torch.max(data)
        return torch.exp(data-c)/sum(torch.exp(data-c))
    
data = torch . Tensor ([1 , 2 , 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
print(output)

print('\n\n\n\n\n')
