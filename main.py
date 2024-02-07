import numpy as np
from patblib import Path


def z(x, y):
    x = np.array(x)
    return (y - np.mean(x)) / np.std(x)

