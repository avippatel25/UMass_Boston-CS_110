import stdarray
import stdio
import sys

# n is assigned value as command line argument
n=int(sys.argv[1])

# an array is created of 1 dimensions
a=stdarray.create1D(n+1,"None")

# for loop is runed till range n+1 and new array is created
for i in range(0,n+1):
    a[i]=stdarray.create1D(i+1,1)

# for loop is runed till range n+1
for i in range(0,n+1):
    # for loop is runed till range i and sum of the value of two elements is added in 2D array
    for j in range(1,i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]

# for loops are used to print the correct value in correct format
for i in range(0,n+1):
    for j in range(0,i+1):
        if j<i:
            stdio.write(str(a[i][j])+" ")
        else:
            stdio.writeln(str(a[i][j]))