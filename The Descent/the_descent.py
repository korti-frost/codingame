import sys
import math

# game loop
while True:

    num_m = 0 # index of the tallest mountain
    tallest_m = 0 # height of the tallest mountain

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        if (mountain_h > tallest_m):
            tallest_m = mountain_h
            num_m = i

    # The index of the mountain to fire on.
    print(num_m)
