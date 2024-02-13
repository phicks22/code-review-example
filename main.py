import numpy as np
from pathlib import Path


def z(x, y):
    x = np.array(x)
    return (y - np.mean(x)) / np.std(x)


x = [1, 2, 3, 4, 5]
y = 7

z = z(x, y)
