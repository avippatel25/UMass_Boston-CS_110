import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    n = int(sys.argv[1])
    stdio.writeln(_sumOfInts(n))


# Returns the sum 1 + 2 + ... + n.
def _sumOfInts(n):
    # the sum of integers if the number is one is one but if its greater than one recursion is used to pass the previous number than given number
    if n==1:
        return 1
    else:
        return n+_sumOfInts(n-1)


if __name__ == "__main__":
    main()
