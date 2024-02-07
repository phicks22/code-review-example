import numpy as np
from patblib import Path


def z_score(arr: np.array, y: float) -> float:
    """This function computes a z-score for a value against an array

    :param arr: array to compute z-score against
    :param y: the value to compute z-score for
    :return z: the z-score for value y against the array
    """

    z = (y - np.mean(arr)) / np.std(arr)

    return z

