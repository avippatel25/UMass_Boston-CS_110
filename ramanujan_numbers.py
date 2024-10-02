import stdio
import sys

# variable n is assigned value as command line argument
n=int(sys.argv[1])

#value of new variable a is assigned
a=1

#multiple while loops are created to find the sum of perfect cubes
while a**3<=n:
    b=a+1
    while (a**3+b**3)<=n:
        c=a+1
        while c**3<=n:
            d=c+1
            while (c**3+d**3)<=n:
                x=a**3+b**3
                y=c**3+d**3
                if x==y:
                    # value of the sum of perfect cubes are printed as standard output in the given format
                    stdio.writeln(str(x)+" = "+str(a)+"^3 + "+str(b)+"^3 = "+str(c)+"^3 + "+str(d)+"^3")
                d+=1
            c+=1
        b+=1
    a+=1