import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def __str__(self):

        return f"{self.rekisteritunnus}: Huippunopeus = {self.huippunopeus} km/h, " \
               f"Nopeus = {self.nopeus} km/h, Kuljettu matka = {self.kuljettu_matka} km"

    def kiihdytä(self, nopeuden_muutos):
        """Muutetaan auton nopeutta. Nopeus ei saa ylittää huippunopeutta eikä mennä alle nollan."""
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        """Kasvattaa kuljettua matkaa sen mukaan, kuinka paljon auto kulkee tunnissa."""
        self.kuljettu_matka += self.nopeus * tuntimäärä


def suorita_kilpailu(autot, kilpailumatka=10000):
    tunti = 0
    while True:
        tunti += 1
        print(f"\nKilpailun tunti: {tunti}")

        for auto in autot:

            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)


            auto.kulje(1)


            print(auto)


        if any(auto.kuljettu_matka >= kilpailumatka for auto in autot):
            break


if __name__ == "__main__":

    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)


    suorita_kilpailu(autot)


    print("\nKilpailu päättyi!")
    print(f"{'Rekisteritunnus':<15}{'Huippunopeus':<15}{'Nopeus':<10}{'Kuljettu matka':<15}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka}")
