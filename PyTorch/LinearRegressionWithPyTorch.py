import torch

class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel.self).__init__()
        self.linear = torch.nn.Linear(1, 1)  # 构造对象

    def forward(self, x):
        y_pred = self.linear(x)  # 可调用对象
        return y_pred

model = LinearModel()

class Foobar:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("Hello"+str(args[0]))


foobar = Foobar()
foobar(1, 2, 3)


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

#func(1, 2, 3, x=3, y=5)
