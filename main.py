class Cesko:
        def hlavni_mesto(self):
            print("Hlavní město je: Praha")
        def pocet_obyvatel(self):
            print("Počet obyvatel je: 10 700 000")
        def jazyk(self):
            print("Jazyk je: Čeština")


class Slovensko:
    def hlavni_mesto(self):
        print("Hlavní město je: Bratislava")

    def pocet_obyvatel(self):
        print("Počet obyvatel je: 5 400 000")

    def jazyk(self):
        print("Jazyk je: Slovenština")

def zakladni_info(instance):
    instance.hlavni_mesto()
    instance.pocet_obyvatel()
    instance.jazyk()

staty = []

staty.append(Cesko())
staty.append(Slovensko())

for stat in staty:
    print(stat)
    stat.hlavni_mesto()
    stat.pocet_obyvatel()
    stat.jazyk()
    print()