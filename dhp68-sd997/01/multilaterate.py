import sys
from scipy.optimize import fsolve
import math
import numpy as np


def multilaterate(distances):
    (x1, y1, z1, d1) = distances[0]
    (x2, y2, z2, d2) = distances[1]
    (x3, y3, z3, d3) = distances[2]
    (x4, y4, z4, d4) = distances[3]

    vector = [
        d1 ** 2 - d2 ** 2 - x1 ** 2 - y1 ** 2 - z1 ** 2 + x2 ** 2 + y2 ** 2 + z2 ** 2,
        d2 ** 2 - d3 ** 2 - x2 ** 2 - y2 ** 2 - z2 ** 2 + x3 ** 2 + y3 ** 2 + z3 ** 2,
        d3 ** 2 - d4 ** 2 - x3 ** 2 - y3 ** 2 - z3 ** 2 + x4 ** 2 + y4 ** 2 + z4 ** 2,
    ]

    matrix = [
        [-2 * x1 + 2 * x2, -2 * y1 + 2 * y2, -2 * z1 + 2 * z2],
        [-2 * x2 + 2 * x3, -2 * y2 + 2 * y3, -2 * z2 + 2 * z3],
        [-2 * x3 + 2 * x4, -2 * y3 + 2 * y4, -2 * z3 + 2 * z4]
    ]

    return np.linalg.solve(matrix, vector)


if __name__ == "__main__":

    # Retrieve file name for input data
    if len(sys.argv) == 1:
        print("Please enter data file name.")
        exit()

    filename = sys.argv[1]

    # Read data
    lines = [line.rstrip('\n') for line in open(filename)]
    distances = []
    for line in range(0, len(lines)):
        distances.append(list(map(float, lines[line].split(' '))))

    # Print out the data
    print("The input four points and distances, in the format of [x, y, z, d], are:")
    for p in range(0, len(distances)):
        print(*distances[p])

        # Call the function and compute the location
    location = multilaterate(distances)
    print("The location of the point is: " + str(location))
