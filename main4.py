import os
import numpy as np

cwd = os.getcwd()
path = os.path.join(cwd, 'input.txt')

file = open(path, 'r')
lines = file.readlines()

c = 0
for i in lines:
    elf1, elf2 = i[:-1].split(',')
    elf1_ll, elf1_ul = elf1.split('-')
    elf2_ll, elf2_ul = elf2.split('-')
    elf1_contains_elf2 = (int(elf1_ul) >= int(elf2_ul)) and (int(elf1_ll) <= int(elf2_ll))
    elf2_contains_efl1 = (int(elf2_ul) >= int(elf1_ul)) and (int(elf2_ll) <= int(elf1_ll))
    if elf1_contains_elf2 or elf2_contains_efl1:
        c += 1
print(c)

c = 0
for i in lines:
    elf1, elf2 = i[:-1].split(',')
    elf1_ll, elf1_ul = elf1.split('-')
    elf2_ll, elf2_ul = elf2.split('-')
    elf1 = np.linspace(int(elf1_ll), int(elf1_ul), int(elf1_ul)-int(elf1_ll)+1)
    elf2 = np.linspace(int(elf2_ll), int(elf2_ul), int(elf2_ul)-int(elf2_ll)+1)
    common = np.intersect1d(elf1, elf2)
    if len(common) > 0:
        c += 1
print(c)

