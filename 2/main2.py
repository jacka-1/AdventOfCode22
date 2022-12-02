import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
path = os.path.join(cwd, 'input.txt')

data = pd.read_csv(path, header=None, skip_blank_lines=False, delimiter=' ')
played = np.asarray(data[0])
guide = np.asarray(data[1])

points = 0
for i in range(len(played)):
    if played[i] == 'A':
        if guide[i] == 'X':
            points += 4
        elif guide[i] == 'Y':
            points += 8
        else:
            points += 3
    elif played[i] == 'B':
        if guide[i] == 'X':
            points += 1
        elif guide[i] == 'Y':
            points += 5
        else:
            points += 9
    else:
        if guide[i] == 'X':
            points += 7
        elif guide[i] == 'Y':
            points += 2
        else:
            points += 6
print(points)

points2 = 0
for i in range(len(played)):
    if played[i] == 'A':
        if guide[i] == 'X':
            points2 += 3
        elif guide[i] == 'Y':
            points2 += 4
        else:
            points2 += 8
    elif played[i] == 'B':
        if guide[i] == 'X':
            points2 += 1
        elif guide[i] == 'Y':
            points2 += 5
        else:
            points2 += 9
    else:
        if guide[i] == 'X':
            points2 += 2
        elif guide[i] == 'Y':
            points2 += 6
        else:
            points2 += 7
print(points2)