import stdio
import sys

# variable p and q are created to accept commnd line argument
p=int(sys.argv[1])
q=int(sys.argv[2])

# maximum number is assigned to mx so that we could use the loop
mx=max(p,q)

#gcd is a variable to store the greatest common divisor
gcd=1

#loop is fired to find all the numbers that divide the p and q
for i in range(1,mx):
    if p%i==0 and q%i==0:
        gcd=i

# gcd value is printed as the standard output
stdio.writeln(gcd)