class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
        The values of mins and secs may be outside the range 0-59,
        but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Return the number of seconds represented
        by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())


t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print(t3) # 05:06:12

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other): # scalar multiplication
        return Point(other * self.x, other * self.y)

p1 = Point(3, 4)
p2 = Point(5, 7)
print(p1 * p2) # 43
print(2 * p2) # (10, 14)
# print(p2 * 2) # AttributeError: 'int' object has no attribute 'x'