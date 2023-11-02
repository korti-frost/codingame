import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp_close = 6000 # the number close to zero (ranging from -273 to 5526)
temp_n = "" # If it is negatif or not


for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if (n == 0):
        exit()

    # Compare the new number to the current best if better then replace
    if (abs(t) < temp_close):
        temp_close = abs(t)
        if (t < 0):
            temp_n = "-"
    elif (abs(t) == temp_close and t > 0):
        temp_n = ""

# If temp_close is still 6000 the no temperature given so return 0 else return answer
if (temp_close == 6000):
    print(0)
else:
    print(temp_n + str(temp_close))
