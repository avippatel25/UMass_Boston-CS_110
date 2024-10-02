import stdio
import sys

# variable n is assigned value as command line argument
n= int(sys.argv[1])

#value 0 is assigned to varible count
count=0

# for loop is runed for range 2 to n so that every number is tried to divide n
for i in range(2,n+1):
   j=2
   #another while loop is runed to find the prime number
   while j<= (i/j):
       if i%j==0:
           break
       j=j+1
   # id the prime number is found the value of the variable count increases by one
   if j>(i/j):
       count+=1

#value of the count is printed as standard output
stdio.writeln(count)