class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print(f"Virhe: Kohdekerros {kohde_kerros} ei ole sallitulla alueella.")
            return

        while self.nykyinen_kerros != kohde_kerros:
            if self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}:")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero on virheellinen.")

    def palohalytys(self):
        print("\nPalohälytys! Kaikki hissit siirretään pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i}:")
            hissi.siirry_kerrokseen(hissi.alin_kerros)


if __name__ == "__main__":


    talo = Talo(1, 10, 3)


    talo.aja_hissia(0, 5)
    talo.aja_hissia(1, 7)
    talo.aja_hissia(2, 3)

    talo.palohalytys()
