import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    # length od the string is given to variable n
    n=len(s)
    # if th string is empty then it returns true because empty string is palindrome
    if n==0:
        return True
    # now the string's first and last character is checked and new function is called where the new string is passed removing the first and last character
    if s[0]==s[-1] and _isPalindrome(s[1:n-1]):
        #if it matches than returns true or else false
        return True
    else:
        return False

if __name__ == "__main__":
    main()
