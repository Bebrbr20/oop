def ucase(text):
    return text.upper()

print(ucase("\n  ahoj"))


class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 18

print(mark.age)