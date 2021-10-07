import numpy as np

class RandomData:

    def __init__(self, num):
        self.num = num

    def create_data(self):
        return np.random.randn(self.num)

    def color_labels(self):
        return np.random.randint(0, 5, self.num)
