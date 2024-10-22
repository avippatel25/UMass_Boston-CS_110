import stdarray
import stdio
import sys

# m and n are assigned value as command line argument
m=int(sys.argv[1])
n=int(sys.argv[2])

# an array of two dimensional is created
a=stdarray.create2D(m,n,"None")

# for loops are runed to add the value to array
for i in range(0,m):
    for j in range(0,n):
        a[i][j]=stdio.readFloat()

# new array named c is created of 2 dimensional
c=stdarray.create2D(n,m,"None")

#for loops are runed till the value of array is matched
for i in range(0,n):
    for j in range(0,m):
        c[i][j]=a[j][i]

#for loops are runed and correct value are printed in correct format
for i in range(0,n):
    for j in range(0,m):
        if j<m-1:
            stdio.write(str(c[i][j]) + " ")
        else:
            stdio.writeln(str(c[i][j]))