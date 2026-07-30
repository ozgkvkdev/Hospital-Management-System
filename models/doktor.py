from models.kisi import Kisi

class Doktor (Kisi):
    def __init__(self, ad, soyad, yas, tc_kimlik_no, telefon,doktor_id,brans,uzmanlik,poliklinik,musaitlik):
        super().__init__(ad,soyad,yas,tc_kimlik_no,telefon)
        self.doktor_id=doktor_id
        self.brans=brans
        self.uzmanlık=uzmanlik
        self.poliklinik=poliklinik
        self.musaitlik=musaitlik

    def __str__(self):
              return (
                f"{super().__str__()}\n"
                f"Doktor ID: {self.doktor_id}\n"
                f"Branş: {self.brans}\n"
                f"Uzmanlık: {self.uzmanlık}\n"
                f"Polikilinik: {self.poliklinik}\n"
                f"Müsaitlik: {self.musaitlik}"
            )     
        