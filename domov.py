class Osobka:
    """
        Class that represents a person
    """

    def __init__(self, jmeno, prijmeni, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon

    def __str__(self):
        return "Hello I am " + self.jmeno

class Domov_duchodcu:
    """
            Class that represents retirement home
    """

    def __init__(self, ico, nazev, kapacita):
        self.ico = ico
        self.nazev = nazev
        self.kapacita = kapacita

    def __str__(self):
        return "Název zařízení" + self.nazev
class Adreska:
    """
            Class that represents persons address
    """

    def __init__(self, ulice, mesto, stat, psc):
        self.ulice = ulice
        self.mesto = mesto
        self.stat = stat
        self.psc = psc

    def __str__(self):
        return "Nacházím se v" + self.mesto

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
adresa1 = Adreska("Novoborská 2", "Praha", "Czechia", 19000)
domov1 = Domov_duchodcu("05159822", "Domov sv. Jany Beránkové", "1000")