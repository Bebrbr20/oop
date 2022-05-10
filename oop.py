
class Person:

    """
    Class hat represents a person
    """

    def __init__(self, _name, _birth, _email):
        self.name = _name
        self.__birth = _birth
        self.email = _email

    def purchase_parking_pass(self):
        print("Parking purchased!")


peter = Person("Peter Parker", 1900, "pani@berankova.mcdonalds")
peter.purchase_parking_pass()







