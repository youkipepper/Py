import matplotlib.pyplot as plt
import numpy as np

x_data = [1.0, 2.0, 3.0, ]
y_data = [2.0, 4.0, 6.0, ]

w = 1.0


def forward(x):
    return x*w


def loss(x, y):
    y_pred = forward(x)
    return (y_pred-y)**2


print('Predict (before training)', 4, forward(4))


def gradient(xs, ys):
    return 2*x*(x*w-y)


for epoch in range(100):
    for x, y in zip(x_data, y_data):
        grad = gradient(x, y)
        w = w-0.01*grad
        print('\t grad: ', x, y, grad)
        l = loss(x, y)
    print("progress: ", epoch, "w = ", w, "loss", 1)
print('Predict (after training)', 4, forward(4))
