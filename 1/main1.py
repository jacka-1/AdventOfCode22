import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
path = os.path.join(cwd, 'input.csv')

data = pd.read_csv(path, header=None, skip_blank_lines=False)
data = list(data[0])

c = 0
totals = []
for i in data:
    if np.isnan(i):
        totals.append(c)
        c = 0
    else:
        c += i
totals.sort()

print(sum(totals[-3:]))




        