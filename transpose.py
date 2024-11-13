import stdarray
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()


# Returns the transpose of a.
def _transpose(a):
    # m and n variable are assigned no of rows and no of coulmns in array
    m=len(a)
    n=len(a[0])
    # new array of length nXm is created
    c=stdarray.create2D(n,m)
    #for loop is runed to find the transpose of the given array
    for i in range(n):
        for j in range(m):
            c[i][j] = a[j][i]
    return c



if __name__ == "__main__":
    main()
