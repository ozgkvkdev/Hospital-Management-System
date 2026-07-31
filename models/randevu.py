from models.hasta import Hasta
from models.doktor import Doktor


class Randevu:

    def __init__(self, randevu_id, hasta, doktor, tarih, saat, durum):
        self.randevu_id = randevu_id
        self.hasta = hasta
        self.doktor = doktor
        self.tarih = tarih
        self.saat = saat
        self.durum = durum

    def __str__(self):
        return (
            f"========== RANDEVU ==========\n"
            f"Randevu ID : {self.randevu_id}\n\n"

            f"Hasta Bilgileri\n"
            f"----------------\n"
            f"Ad Soyad : {self.hasta.ad} {self.hasta.soyad}\n"
            f"Hasta ID : {self.hasta.hasta_id}\n"
            f"Kan Grubu: {self.hasta.kan_grubu}\n\n"

            f"Doktor Bilgileri\n"
            f"-----------------\n"
            f"Ad Soyad : {self.doktor.ad} {self.doktor.soyad}\n"
            f"Doktor ID: {self.doktor.doktor_id}\n"
            f"Branş    : {self.doktor.brans}\n\n"

            f"Tarih : {self.tarih}\n"
            f"Saat  : {self.saat}\n"
            f"Durum : {self.durum}"
        )