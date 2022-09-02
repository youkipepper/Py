import matplotlib.pyplot as plt
import numpy as np

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

ω = 1.0

def forward(x):
    return x*ω


def cost(xs, ys):
    cost = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x)
        cost += (y_pred-y)**2
    return cost/len(xs)


def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2*x*(x*ω-y)
    return grad/len(xs)


loss_list = []
epoch_list = []

print('Predict (before training', 4, forward(4))
for epoch in range(100):
    cost_val = cost(x_data, y_data)
    grad_val = gradient(x_data, y_data)
    ω -= 0.01*grad_val
    print('Epoch:', epoch, 'ω=', ω, 'loss=', cost_val)
    loss_list.append(cost_val)
    epoch_list.append(epoch)

print('Preict (after traning),4,forward(4)')

plt.plot(epoch_list, loss_list)
plt.ylabel("Cost")
plt.xlabel("Epoch")
plt.show()
