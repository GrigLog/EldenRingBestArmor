import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from find_best import find_best, read_pieces


WEIGHT = 70


def draw():
    pieces = read_pieces()
    fig, axes = plt.subplots()
    weights = [round(w * 0.1, 3) for w in range(WEIGHT * 10 + 1)]
    for (func, label, color) in [
        (lambda set: set.physical, 'physical', 'black'),
        (lambda set: set.strike, 'strike', 'orchid'),
        (lambda set: set.slash, 'slash', 'magenta'),
        (lambda set: set.pierce, 'pierce', 'purple'),
        (lambda set: set.fire, 'fire', 'red'),
        (lambda set: set.magic, 'magic', 'blue'),
        (lambda set: set.lightning, 'lightning', 'yellow'),
        (lambda set: set.holy, 'holy', 'gold')]:
        axes.plot(weights, find_best(pieces.copy(), WEIGHT, func), color, label=label)
    axes.legend()
    axes.xaxis.set_ticks(range(0, WEIGHT+1, 1))
    axes.yaxis.set_ticks(range(0, 40+1, 1))
    axes.margins(x=0, y=0)
    plt.grid(True)
    plt.xlabel("Weight")
    plt.ylabel("Highest negation %")
    plt.show()


if __name__ == "__main__":
    draw()
