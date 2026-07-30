from models.kisi import Kisi

class Hasta(Kisi):
    def __init__(self, ad, soyad, yas, tc_kimlik_no, telefon, hasta_id, kan_grubu, aciliyet_durumu):
        super().__init__(ad, soyad, yas, tc_kimlik_no, telefon)
        self.hasta_id=hasta_id
        self.kan_grubu=kan_grubu
        self.aciliyet_durumu=aciliyet_durumu

    def __str__(self):
      return (
        f"{super().__str__()}\n"
        f"Hasta ID: {self.hasta_id}\n"
        f"Kan Grubu: {self.kan_grubu}\n"
        f"Aciliyet Durumu: {self.aciliyet_durumu}"
    )

    



 