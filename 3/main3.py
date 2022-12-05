import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
path = os.path.join(cwd, 'input.txt')

file = open(path, 'r')
lines = file.readlines()

priorities = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
    'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
    'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40,
    'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52,
}

p = 0
for i in lines:
    l = len(i)
    half1, half2 = i[:l//2], i[l//2:]
    (common,) = set(half1) & set(half2)
    p += priorities[common]
print(p)

p = 0
for i in range(len(lines)):
    if i % 3 == 0:
        print(i)
        first, second, third = lines[i][:-1], lines[i+1][:-1], lines[i+2][:-1]
        print(first)
        print(second)
        print(third)
        (common,) = set(first) & set(second) & set(third)
        print(common)
        p += priorities[common]
    else:
        p += 0
print(p)