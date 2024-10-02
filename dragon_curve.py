import stdio
import sys

# variable n is assigned value as command line argument
n=int(sys.argv[1])

# new variables dragon and nogard are assigned string F
dragon="F"
nogard="F"

# loop is used for range n to draw the dragon curve direction in variable dragon using temp variable
for i in range(n):
    temp=dragon
    dragon=dragon+"L"+nogard
    nogard=temp+"R"+nogard

# value of dragon is printed as standard output
stdio.writeln(dragon)