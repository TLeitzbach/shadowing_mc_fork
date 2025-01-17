import numpy as np
from scipy.special import softmax


class DiscreteProba:
    def __init__(self, w):
        self.w = w

    def avg(self, x, axis, keepdims=False):
        return np.average(x, axis, self.w, keepdims=keepdims)

    def variance(self, x, axis):
        xmean = self.avg(x, axis, keepdims=True)
        return self.avg((x - xmean) ** 2, axis)

    def std(self, x, axis):
        return self.variance(x, axis) ** 0.5


class Softmax(DiscreteProba):
    def __init__(self, l2s, eta):
        weights = softmax(-l2s ** 2 / 2 / eta ** 2)
        super(Softmax, self).__init__(weights)


class Uniform(DiscreteProba):
    def __init__(self):
        super(Uniform, self).__init__(None)

    def avg(self, x, axis, keepdims=False):
        return x.mean(axis, keepdims=keepdims)
