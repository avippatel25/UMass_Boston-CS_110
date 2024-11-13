import rsa
import stdio
import sys


# Entry point.
def main():
    #low and high value are assigned value from command line argument
    lo=int(sys.argv[1])
    hi=int(sys.argv[2])

    #n,e,d are assigned value using function from rsa file
    n,e,d=rsa.keygen(lo,hi)
    #values are printed as standard output
    stdio.writeln(str(n)+" "+str(e)+" "+str(d))

if __name__ == "__main__":
    main()
