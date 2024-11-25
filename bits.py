from numpy.matlib import empty

import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef("zeros = %d, ones = %d, total = %d\n", _zeros(s), _ones(s), len(s))


# Return the number of zeros in s.
def _zeros(s):
    # if the string is empty it will return 0
    if s=="":
        return 0
    #first element of the given array is checked whether it's 0 or not and if it is then new array from the 2nd element is passed and same function is called
    if s[0]=='0':
        return 1+_zeros(s[1:])
    else:
        return _zeros(s[1:])



# Return the number of ones in s.
def _ones(s):
    # if the string is empty it will return 0
    if s=="":
        return 0
    #first element of the given array is checked whether it's 1 or not and if it is then new array from the 2nd element is passed and same function is called
    if s[0]=='1':
        return 1+_ones(s[1:])
    else:
        return _ones(s[1:])


if __name__ == "__main__":
    main()
