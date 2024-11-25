import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))


# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    # we need to check 5 condition so initial vlue of 5 new variables are set to true
    check1=False
    check2=False
    check3=False
    check4=False
    check5=False
    #if the length of password is at least 8 than the first condition is true
    if len(pwd) >= 8:
        check1=True
    #for loop is used because we need to check condition of each character of password(string)
    for c in pwd:
        #if any character is digit than the condition is true
        if c.isdigit():
            check2=True
        # if any character is upper case than the condition is true
        elif c.isupper():
            check3=True
        #if any character is lower case than the condition is true
        elif c.islower():
            check4=True
        # if any character is not alphanumeric than the condition is true
        elif not c.isalnum():
            check5=True
    # using logical and : true or false is returned
    return check1 and check2 and check3 and check4 and check5


if __name__ == "__main__":
    main()
