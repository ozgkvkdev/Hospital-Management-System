class Poliklinik:
    def __init__(self, poliklinik_id, ad, kapasite, doktor_sayisi):
        self.poliklinik_id = poliklinik_id
        self.ad = ad
        self.kapasite = kapasite
        self.doktor_sayisi = doktor_sayisi

    def __str__(self):
        return (
            f"Poliklinik ID: {self.poliklinik_id}\n"
            f"Ad: {self.ad}\n"
            f"Kapasite: {self.kapasite}\n"
            f"Doktor Sayısı: {self.doktor_sayisi}"
        )

    def to_dict(self):
        return {
            "poliklinik_id": self.poliklinik_id,
            "ad": self.ad,
            "kapasite": self.kapasite,
            "doktor_sayisi": self.doktor_sayisi,
        }
