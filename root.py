import stdio
import sys

# variable k, c and epsilon is assigned value as command line argument
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# t is assigned value of c
t=c

# while loop is runed to assign value upto epsilon value
while abs(1-c/t**k) > epsilon:
    t = t - (t**k - c)/ (k*t**(k-1))

# value of t is printed as standard output
stdio.writeln(t)