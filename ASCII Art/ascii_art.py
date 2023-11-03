import sys
import math

l = int(input())
h = int(input())
t = input()
t = t.upper()
atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
atoz_ascii = []
char_pos = -1
answer = []

for i in range(h):
    row = input()
    atoz_ascii.append([row[i:i+l] for i in range(0, len(row), l)])

for i in range(h):
    row = ""
    for char in t:
        char_pos = atoz.find(char)
        if (char_pos == -1):
            row += str(atoz_ascii[i][26])
        else:
            row += str(atoz_ascii[i][char_pos])
    answer.append(row)

for i in answer:
    print(str(i))
