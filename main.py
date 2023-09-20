from dense import Dense
from activations import Tanh
from MSE import mse, mse_prime

import numpy as np


X = np.reshape([[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]], (4, 3, 1))
Y = np.reshape([[1], [0], [0], [1]], (4, 1, 1))

epochs = 1
learning_rate = 0.04

network = [
    Dense(3, 3),
    Tanh(),
    Dense(3, 1),
    Tanh()
]

# train
for e in range(epochs):
    error = 0
    for x, y in zip(X, Y):
        print(x)
        # forward
        output = x
        for layer in network:
            
            output = layer.forward(output)
        print(output)
        # error
        error += mse(y, output)

        # backward
        grad = mse_prime(y, output)
        for layer in reversed(network):
            grad = layer.backward(grad, learning_rate)

    error /= len(X)
    print('%d/%d, error=%f' % (e + 1, epochs, error))

output= np.reshape([[1, 1, 0]], (1, 3, 1))
output=output.tolist()
print(output)

for layer in network:
    output = layer.forward(output)

print(output)