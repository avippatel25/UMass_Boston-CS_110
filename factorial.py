import stdio
import sys

# variable n is assigned value as command line argument
n = int(sys.argv[1])

# if and else are used as if n is 0 than ite fact is 1 and loop is used for rest of the numbers
if n==0:
    stdio.writeln("1")
else:
    # variable fact is assigned 1 as value
    fact=1
    #loop is runed for range n+1 to assign value of fact
    for i in range(1,n+1):
        fact=fact*i

    # value of fact is printed as standard output
    stdio.writeln(fact)