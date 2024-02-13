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


def mse(y_pred: np.array, y_true: np.array) -> float:
    """This function computes the mean squared error between two arrays.

    :param y_pred: the predicted probabilities of the model
    :param y_true: the true labels for each element in y_pred
    :return mse: the mean squared error between the two arrays
    """

    mse = np.mean((y_pred - y_true) ** 2)

    return mse


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
    parser.add_argument(
        "-y_pred",
        help="The file containing the predicted probabilities of the model",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-y_true",
        help="The file containing the true labels",
        required=True,
        type=str,
    )
    args = parser.parse_args()

    # Set paths
    arr_file = Path(args.arr_file)
    y_pred_file = Path(args.y_pred)
    y_true_file = Path(args.y_true)

    # Load data
    arr_of_something = np.load(arr_file)
    y_pred = np.load(y_pred_file)
    y_true = np.load(y_true_file)

    # Set value from args
    myValue = args.value

    # Compute z-score
    myZ = z_score(arr=arr_of_something, y=myValue)

    # Compute mean squared error
    myMSE = mse(y_pred=y_pred, y_true=y_true)
