def rapor_olustur(hastalar=None, doktorlar=None, randevular=None, poliklinikler=None):
    hastalar = hastalar or []
    doktorlar = doktorlar or []
    randevular = randevular or []
    poliklinikler = poliklinikler or []

    aktif_randevu_sayisi = sum(1 for r in randevular if r.get("durum") == "Aktif")

    return {
        "hasta_sayisi": len(hastalar),
        "doktor_sayisi": len(doktorlar),
        "aktif_randevu_sayisi": aktif_randevu_sayisi,
        "poliklinik_sayisi": len(poliklinikler),
    }
