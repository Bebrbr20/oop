class Osobka:
    """
        Class that represents a person
    """

    def __init__(self, jmeno, prijmeni, telefon, _rodne_cislo, _datum_narozeni, pohlavi):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.__rodne_cislo = _rodne_cislo
        self.__datum_narozeni = _datum_narozeni
        self.pohlavi = pohlavi

    def __str__(self):
        return "Hello I am " + self.jmeno

    def get_age(self):
        return 2022 - self.__datum_narozeni

    def Validate(self):
        return True


class DomovDuchodcu:
    """
            Class that represents retirement home
    """

    def __init__(self, ico, nazev, kapacita):
        self.ico = ico
        self.nazev = nazev
        self.kapacita = kapacita
        self.__adreska = None
        self.klienti = []

    def __str__(self):
        return "Název zařízení" + self.nazev

    def registrace_dd(self, klienti):
        self.klienti.append(klienti)

    def volna_mista(self):
        cap = (self.kapacita - len(self.klienti))
        print("Počet volných míst v " + self.nazev + " je "+ str(cap))

    def set_address(self, _adreska):
        self.__adreska = _adreska

    def get_address(self):
        print(self.nazev + " je " + str(self.__adreska))

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
        return "v " + self.mesto

    def Validate(self):
            return True


peter = Osobka("Peter", "Parker", 123456789, "0711044719", 1910, "Muž")
jana = Osobka("Jana", "Bránková", 123456789, "0711044719", 1920, "Atraktivní žena")
michaela = Osobka("Michaela", "Moniková", 987654321, "0711044719", 1500, "Není známo")
iveta = Osobka("Iveta", "Bráberolá", 123456789, "0711044719", 2000, "Velice atraktivní žena")

adresa1 = Adreska("Novoborská 2", "Praha", "Czechia", 19000)
adresa2 = Adreska("Nymburská 68", "Poděbrady", "Czechia", 29001)

domov1 = DomovDuchodcu("05159822", "Domov sv. Jany Beránkové", 1000)
domov2 = DomovDuchodcu("05157622", "Domov sv. Lucie Ubrouskové", 100)

domov1.registrace_dd(peter)
domov1.registrace_dd(michaela)
domov1.registrace_dd(iveta)
domov2.registrace_dd(jana)

domov1.set_address(adresa1)
domov2.set_address(adresa2)


domov1.get_address()
domov2.get_address()

domov1.volna_mista()
domov2.volna_mista()
