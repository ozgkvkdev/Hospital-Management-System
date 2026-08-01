from models.kisi import Kisi


class Doktor(Kisi):
    def __init__(
        self,
        ad,
        soyad,
        yas,
        tc_kimlik_no,
        telefon,
        doktor_id,
        brans,
        uzmanlik,
        poliklinik,
        musaitlik
    ):
        super().__init__(ad, soyad, yas, tc_kimlik_no, telefon)

        self.doktor_id = doktor_id
        self.brans = brans
        self.uzmanlik = uzmanlik
        self.poliklinik = poliklinik
        self.musaitlik = musaitlik

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Doktor ID: {self.doktor_id}\n"
            f"Branş: {self.brans}\n"
            f"Uzmanlık: {self.uzmanlik}\n"
            f"Poliklinik: {self.poliklinik}\n"
            f"Müsaitlik: {self.musaitlik}"
        )

    def to_dict(self):
     return {
        "ad": self.ad,
        "soyad": self.soyad,
        "yas": self.yas,
        "tc_kimlik_no": self.tc_kimlik_no,
        "telefon": self.telefon,
        "doktor_id": self.doktor_id,
        "brans": self.brans,
        "uzmanlik": self.uzmanlik,
        "poliklinik": self.poliklinik,
        "musaitlik": self.musaitlik
    }