import stdio
import sys

# variable n is assigned value as command line argument
n= int(sys.argv[1])

#vaue of i is assigned
i=2

# while loop is created to find the prime number
while i<= (n//i+1):
    if n%i == 0:
        break
    i+=1

#if prime number is found than we print True else we print False as Standard output
if i>(n/i):
    stdio.writeln("True")
else:
    stdio.writeln("False")