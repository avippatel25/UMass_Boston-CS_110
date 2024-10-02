import stdio
import sys

# variable n and k is assigned value as command line argument
n=int(sys.argv[1])
k=int(sys.argv[2])

# variable sum is assigned 0 value
sum=0

#loop is runed for range n+1 to get the value in variable sum
for i in range(1,n+1):
    sum=sum+pow(i,k)

# value of sum is printed as standard output
stdio.writeln(sum)