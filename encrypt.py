import rsa
import stdio
import sys


# Entry point.
def main():
    #n and e variable are assigned value as command line argument
    n=int(sys.argv[1])
    e=int(sys.argv[2])

    #width is given number of bits per character for encryption
    width=rsa.bitLength(n)

    #message is given value as standard input
    message=stdio.readAll()

    #for loop is used for encryption of every character in message given
    for c in message:
        x = ord(c)
        y = rsa.encrypt(x, n, e)
        stdio.write(rsa.dec2bin(y, width))
    stdio.writeln()


if __name__ == "__main__":
    main()
