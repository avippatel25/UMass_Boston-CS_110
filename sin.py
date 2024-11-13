import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))


# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def _sin(x):
    # total is given 0 , term, sign and i are given 1 as value
    total=0.0
    term=1.0
    sign=1
    i=1
    #using while loop we will find the value of sin using the logic of formula: x - ((x^3)/3!) + ((x^5)/5!) - ((x^7)/7!) +...
    while total!=(total+term):
        term *= (x/i)
        if i%2!=0:
            total+=(sign*term)
            if sign > 0:
                sign=-1
            else:
                sign=1
        i+=1
    return total


if __name__ == "__main__":
    main()
