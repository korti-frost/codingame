import sys
import math

l = int(input())
h = int(input())
t = input()
t = t.upper()
atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
atoz_ascii = []

for i in range(h):
    row = input()
    atoz_ascii.append([row[i:i+l] for i in range(0, len(row), l)])
