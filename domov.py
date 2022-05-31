class Osobka:
    """
        Class that represents a person
    """

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def __str__(self):
        return "Hello I am " + self.name

class Domov_duchodcu:
    """
            Class that represents retirement home
    """

    def __init__(self, ico, nazev, kapacita):
        self.ico = ico
        self.nazev = nazev
        self.kapacita = kapacita
class Adreska:
    """
            Class that represents persons address
    """

    def __init__(self):
        self.ulice = ulice
        self.mesto = mesto
        self.stat = stat
        self.psc = psc

    def Validate(self):
            return True

class Rodne_cislo:
    """
            Class that represents persons brith number
    """

    def __init__(self, rodne_cislo, datum_narozeni, pohlavi):
        self.rodne_cislo = rodne_cislo
        self.datum_narozeni = datum_narozeni
        self.pohlavi = pohlavi

    def Validate(self):
        return True

peter = Osobka("Peter", "Parker", 123456789)