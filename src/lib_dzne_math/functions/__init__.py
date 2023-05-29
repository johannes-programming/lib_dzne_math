import numpy as _np


def sigmoid(x):
    return 1.0 / (1.0 + _np.exp(-x))