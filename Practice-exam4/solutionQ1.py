import math

#       A mix of what we have learned.

def create_point(x, y):
    return (x, y)


def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])** 2 + (point2[1] - point1[0])**2)


def is_equal(point1, point2):
    return point1 == point2


def create_figure(point1, point2):
    if is_equal(point1, point2):
        return None
    return [point1, point2]


def add_point(figure, point):
    if is_equal(figure[-1], point):
        return False
    figure.append(point)
    return True


def lengths(figure):
    lengths = []
    for i in range(len(figure) - 1):
        length = math.ceil(distance(figure[i], figure[i+1]))
        lengths.append(length)
    return lengths