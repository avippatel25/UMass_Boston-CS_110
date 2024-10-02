import stdio
import sys

# variable n is assigned value as command line arguments
n = int(sys.argv[1])

# three variables a, b and c are assigned values
a=-1
b=1
i=0

# while loop is created to add the value of the previous number to the new third number
while (i<=n):
    c=a+b
    a=b
    b=c
    i+=1

# value of the last number is than printed as standard output
stdio.writeln(b)