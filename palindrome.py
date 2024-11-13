import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    #length of a string is given to n variable
    n=len(s)
    #for loop is used till half the length of n so that the first element is not same as the last one than it returns false or else true
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            return False
    return True


if __name__ == "__main__":
    main()
