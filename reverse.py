import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    # length of string is given to variable n
    n=len(s)
    # if string is empty then empty string is returned or else the same function is called to reverse the string
    if n==0:
        return s
    else:
        return s[n-1]+_reverse(s[:n-1])


if __name__ == "__main__":
    main()
