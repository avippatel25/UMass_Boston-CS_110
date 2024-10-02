import stdio
import sys

#variable n is assigned value as command line argument
n=int(sys.argv[1])

#for loop is runed for range 2 to n for assigning value to total
for i in range(2,n+1):
    total=0
    # another for loop is runed for range 1 to i/2 to assign value to total
    for j in range(1,int((i/2))+1):
        if i%j==0:
            total+=j
    # if value of total is equal to perfect number it is printed as standard output
    if total==i:
        stdio.writeln(i)