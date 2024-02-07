import numpy as np
from pathlib import Path
from argparse import ArgumentParser


def z_score(arr: np.array, y: float) -> float:
    """This function computes a z-score for a value against an array

    :param arr: array to compute z-score against
    :param y: the value to compute z-score for
    :return z: the z-score for value y against the array
    """

    z = (y - np.mean(arr)) / np.std(arr)

    return z


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-arr_file",
        help="An .npy file storing an array to compute z-score against",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-value", help="The value to compute z-score for", required=True, type=float
    )
    args = parser.parse_args()

    # Load data and set variables
    arr_file = Path(args.arr_file)
    arr_of_something = np.load(arr_file)
    myValue = args.value

    # Compute z-score
    myZ = z_score(arr=arr_of_something, y=myValue)
