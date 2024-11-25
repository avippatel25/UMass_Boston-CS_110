import stdio
from interval import Interval


# A data type to represent a rectangle as two (x and y) intervals.
class Rectangle:
    # Constructs a new rectangle given the x and y intervals.
    def __init__(self, xint, yint):
        #initialisation of instance variable-xint
        self._xint = xint
        #initialisation of instance variable-yint
        self._yint = yint

    # Returns the area of this rectangle.
    def area(self):
        # width variable is assigned taking two points as upper and lower
        width = self._xint.upper() - self._xint.lower()
        # height variable is assigned taking two points as upper and lower
        height = self._yint.upper() - self._yint.lower()
        #area of rectangle is returned
        return width * height

    # Returns the perimeter of this rectangle.
    def perimeter(self):
        #width variable is assigned taking two points as upper and lower
        width = self._xint.upper() - self._xint.lower()
        # height variable is assigned taking two points as upper and lower
        height = self._yint.upper() - self._yint.lower()
        # the perimeter of rectangle is returned
        return 2 * (height + width)

    # Returns True if this rectangle contains the point (x, y), and False otherwise.
    def contains(self, x, y):
        # if x is in between of the xint instance variable and y is in between of yint instance variable than it returns true or false otherwise
        if self._xint.contains(x) and self._yint.contains(y):
            return True
        else:
            return False

    # Returns True if this rectangle intersects other, and False otherwise.
    def intersects(self, other):
        #using function from previous program (Interval) me see if the other rectangle intersects the self triangle and it returns true if it does or else false
        if self._xint.intersects(other._xint) and self._yint.intersects(other._yint):
            return True
        else:
            return False

    # Returns a string representation of this rectangle.
    def __str__(self):
        return str(self._xint) + " x " + str(self._yint)


# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Rectangle(Interval(-1, 1), Interval(-1, 1))
    b = Rectangle(Interval(0, 2), Interval(0, 3))
    stdio.writeln("a                = " + str(a))
    stdio.writeln("b                = " + str(b))
    stdio.writeln("area(a)          = " + str(a.area()))
    stdio.writeln("perimeter(b)     = " + str(b.perimeter()))
    stdio.writeln("a.contains(1, 5) = " + str(a.contains(1, 5)))
    stdio.writeln("a.intersects(b)  = " + str(a.intersects(b)))


if __name__ == "__main__":
    _main()
