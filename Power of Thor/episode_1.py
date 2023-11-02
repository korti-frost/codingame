import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx # Current X position of Thor
thor_y = initial_ty # Current Y position of Thor

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    thor_move = "" # The move Thor will make

    # If Thor needs to go Up or Down
    if (thor_y > light_y):
        thor_move += "N"
        thor_y -= 1
    elif (thor_y < light_y):
        thor_move += "S"
        thor_y += 1

    # If Thor needs to go Left of Right
    if (thor_x > light_x):
        thor_move += "W"
        thor_x -= 1
    elif (thor_x < light_x):
        thor_move += "E"
        thor_x += 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(thor_move)
