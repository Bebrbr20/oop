
class Person:

    """
    Class hat represents a person
    """

    def __init__(self, _name, _birth, _email):
        self.name = _name
        self.__birth = _birth
        self.email = _email
        self.__address = None

    def __str__(self):
        return "Hello I am " + self.name
    def purchase_parking_pass(self):
        print("Parking purchased!")

    def get_age(self):
        return 2022 - self.__birth

    def set_address(self, _address):
        self.__address = _address

    def get_address(self):
        return self.__address
class Professor(Person):
    """
    Class that represents teacher in our school
    """
    def __init__(self, _name, _birth, _email, _salary, _num):
        super().__init__(_name, _birth, _email)
        self.salary = _salary
        self.staff_num = _num

    def teach(self):
        print("I am teching")

class Address:
    """
    class...s.s.s..s
    """
    def __init__(self, _street, _city, _postal_code):
     self.street = _street
     self.city = _city
     self.postal_code = _postal_code

    def __str__(self):
        return self.street + "," + self.city

    def Validate(self):
        return True


peter = Person("Peter Parker", 1900, "pani@berankova.mcdonalds")
peter.purchase_parking_pass()

skola = Address("Novoborská 2", "praha", 19000)

jana = Person("Jana Beránková", 1443, "jana@berankova.mcdonalds")

peter.set_address(skola)
print(peter.get_address())
jana.set_address(skola)

print(jana.get_address())




