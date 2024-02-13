import numpy as np
from pathlib import Path


def z(x, y):
    x = np.array(x)
    return (y - np.mean(x)) / np.std(x)


def terrible_function(j, k):
    return (np.sum(np.subtract(np.array(j), np.array(k)))**2) / len(j)


x = [1, 2, 3, 4, 5]
y = 7

z = z(x, y)
