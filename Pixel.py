import math

class Pixel:
    def __init__(self, row, col, rgb, center, weight, weight_sum):
        self.row = row
        self.col = col
        self.r, self.g, self.b = rgb
        self.center = center
        self.weight = weight
        self.weight_sum = weight_sum

    def set_center(self, center):
        self.center = center

    def set_weight(self, weight):
        self.weight = weight

    def set_weight_sum(self, weight_sum):
        self.weight_sum = weight_sum

    def rgb(self):
        return self.r, self.g, self.b

    def __eq__(self, other):
        return (self.r == other.r
                and self.g == other.g
                and self.b == other.b
                and self.center == other.center)

    def __repr__(self):
        return f"({self.rgb()})\nCenter: {self.center}\nWeight: {self.weight}\nWeightSum: {self.weight_sum}"



