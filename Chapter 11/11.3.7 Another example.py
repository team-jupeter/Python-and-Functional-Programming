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

# Code 1
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        if self.hours > time2.hours:
            return True
        if self.hours < time2.hours:
            return False

        if self.minutes > time2.minutes:
            return True
        if self.minutes < time2.minutes:
            return False
        if self.seconds > time2.seconds:
            return True

        return False

# Code 2
    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

# if current_time.after(done_time):
#     print("The bread will be done before it starts!")

# Code 3
def after(time1, time2):
    """ Return True if I am strictly greater than time2 """
    return time1.to_seconds() > time2.to_seconds()

t1 = MyTime(10, 55, 12)
t2 = MyTime(10, 48, 22)
after(t1, t2)