"""
Kişi Sınıfı

Bu sınıf, hastane yönetim sistemindeki tüm kişilerin ortak özelliklerini temsil eder.

Bu sınıftan türetilecek sınıflar:
- Hasta
- Doktor
"""


class Kisi:
    def __init__(self, ad, soyad, yas, tc_kimlik_no, telefon):
        self.ad = ad
        self.soyad = soyad

        
        if yas < 0 or yas > 120:
            raise ValueError("Yaş kabul edilemez.")

        self.yas = yas
        self.tc_kimlik_no = tc_kimlik_no
        self.telefon = telefon

    def kisi_bilgileri_goster(self):
        print("\n= Kişi Bilgileri =")
        print(f"AD: {self.ad}")
        print(f"SOYAD: {self.soyad}")
        print(f"YAŞ: {self.yas}")
        print(f"TC KİMLİK NO: {self.tc_kimlik_no}")
        print(f"TELEFON: {self.telefon}")

    def __str__(self):
        return (
            f"Ad: {self.ad}\n"
            f"Soyad: {self.soyad}\n"
            f"Yaş: {self.yas}\n"
            f"TC Kimlik No: {self.tc_kimlik_no}\n"
            f"Telefon: {self.telefon}"
        )