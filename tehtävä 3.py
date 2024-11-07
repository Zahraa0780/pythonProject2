class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        return f"Nimi: {self.nimi}"

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        return f"{super().tulosta_tiedot()}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}"

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        return f"{super().tulosta_tiedot()}, Päätoimittaja: {self.paatoimittaja}"



if __name__ == "__main__":

    aku_anka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)


    print(aku_anka.tulosta_tiedot())
    print(hytti_6.tulosta_tiedot())

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
        self.nopeus = max(0, min(self.nopeus + nopeuden_muutos, self.huippunopeus))

    def kulje(self, tuntimäärä):
        """Kasvattaa kuljettua matkaa sen mukaan, kuinka paljon auto kulkee tunnissa."""
        self.kuljettu_matka += self.nopeus * tuntimäärä


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def __str__(self):
        return f"{super().__str__()}, Akkukapasiteetti = {self.akkukapasiteetti} kWh"


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def __str__(self):
        return f"{super().__str__()}, Bensatankin koko = {self.bensatankin_koko} l"



if __name__ == "__main__":

    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)


    sahkoauto.kiihdytä(30)
    sahkoauto.kulje(3)
    polttomoottoriauto.kiihdytä(40)
    polttomoottoriauto.kulje(3)


    print(sahkoauto)
    print(polttomoottoriauto)
