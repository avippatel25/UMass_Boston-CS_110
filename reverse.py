import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()


# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    # length of a is given to n variable so that the loop can be runed
    n=len(a)
    #loop is runed till the half the length of a
    for i in range(0,n//2):
        # temp variable is used to exchange value of first and last variable
        temp=a[i]
        a[i]=a[n-i-1]
        a[n-i-1]=temp
    return a


if __name__ == "__main__":
    main()
