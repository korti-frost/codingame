import sys
import math

l = int(input()) # width of the ASCII art
h = int(input()) # height of the ASCII art
t = input() # line of text that composed the ASCII art
t = t.upper() # Make all characters Upper Case because all ASCII are Upper Case

atoz_ascii = [] # Content is Liste of Liste with all characters in ASCII art

# Takes every string witch is 1 line, split it and add to atoz_ascii
for i in range(h):
    row = input()
    atoz_ascii.append([row[i:i+l] for i in range(0, len(row), l)])

atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alphabet to Compare the indevedual char to
char_pos = -1 # the position of the char in the Alphabet (if -1 mean not present so use last ASCII art of liste (ASCII art of '?'))
answer = [] # Liste of text transforme into ASCII art

# Do the answer Line by Line
for i in range(h):
    row = ""
    # On each Line do Every Char
    for char in t:
        char_pos = atoz.find(char) # find the index on the alphabet because same index as in atoz_ascii
        if (char_pos == -1): # if char not found in alphabet then do ASCII '?'
            row += str(atoz_ascii[i][26])
        else: # if char found add to the answer line
            row += str(atoz_ascii[i][char_pos])
    answer.append(row)

# Print the answer Line by Line
for i in answer:
    print(str(i))
