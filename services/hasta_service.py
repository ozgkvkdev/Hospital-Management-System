from models.hasta import Hasta
from utils.database import verileri_yukle, verileri_kaydet

# JSON'dan verileri yükle
veriler = verileri_yukle()

# Hafızadaki hasta listesi
hastalar = []

# JSON'daki hastaları tekrar Hasta nesnesine dönüştür
for veri in veriler["hastalar"]:
    hasta = Hasta(
        ad=veri["ad"],
        soyad=veri["soyad"],
        yas=veri["yas"],
        tc_kimlik_no=veri["tc_kimlik_no"],
        telefon=veri["telefon"],
        hasta_id=veri["hasta_id"],
        kan_grubu=veri["kan_grubu"],
        aciliyet_durumu=veri["aciliyet_durumu"]
    )
    hastalar.append(hasta)


def hasta_ekle():
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    yas = int(input("Yaşınızı Giriniz: "))
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    telefon = input("Telefon Numaranızı Giriniz: ")
    kan_grubu = input("Kan Grubunuzu Giriniz: ")
    aciliyet_durumu = input("Aciliyet Durumunuzu Giriniz: ")

    hasta_id = len(hastalar) + 1001

    hasta = Hasta(
        ad=ad,
        soyad=soyad,
        yas=yas,
        tc_kimlik_no=tc_kimlik,
        telefon=telefon,
        hasta_id=hasta_id,
        kan_grubu=kan_grubu,
        aciliyet_durumu=aciliyet_durumu
    )

    # RAM'e ekle
    hastalar.append(hasta)

    # JSON'a ekle
    veriler["hastalar"].append(hasta.to_dict())
    verileri_kaydet(veriler)

    print("Hasta başarıyla eklendi.")


def hasta_listele():
    if not hastalar:
        print("Henüz kayıtlı hasta bulunmamaktadır.")
        return

    print("\n== KAYITLI HASTALAR ==")
    for hasta in hastalar:
        print(hasta)
        print("-" * 40)


def hasta_ara():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    bulundu = False

    for hasta in hastalar:
        if hasta.tc_kimlik_no == tc_kimlik:
            bulundu = True
            print("== HASTA BULUNDU ==")
            print(hasta)
            break

    if not bulundu:
        print("Hasta Bulunamadı.")


def hasta_sil():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    bulundu = False

    for hasta in hastalar:
        if hasta.tc_kimlik_no == tc_kimlik:
            bulundu = True

            hastalar.remove(hasta)

            # JSON'dan da sil
            veriler["hastalar"] = [
                h for h in veriler["hastalar"]
                if h["tc_kimlik_no"] != tc_kimlik
            ]
            verileri_kaydet(veriler)

            print("== HASTA SİLİNDİ ==")
            break

    if not bulundu:
        print("Hasta Bulunamadı.")


def hasta_guncelle():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    bulundu = False

    for hasta in hastalar:
        if hasta.tc_kimlik_no == tc_kimlik:
            bulundu = True

            print("== YENİ BİLGİLER ==")

            hasta.ad = input("Adınızı Giriniz: ")
            hasta.soyad = input("Soyadınızı Giriniz: ")
            hasta.yas = int(input("Yaşınızı Giriniz: "))
            hasta.telefon = input("Telefon Numaranızı Giriniz: ")
            hasta.kan_grubu = input("Kan Grubunuzu Giriniz: ")
            hasta.aciliyet_durumu = input("Aciliyet Durumunuzu Giriniz: ")

            # JSON'u güncelle
            for i, veri in enumerate(veriler["hastalar"]):
                if veri["tc_kimlik_no"] == tc_kimlik:
                    veriler["hastalar"][i] = hasta.to_dict()
                    break

            verileri_kaydet(veriler)

            print("\n== GÜNCELLENEN HASTA ==")
            print(hasta)
            break

    if not bulundu:
        print("== HASTA BULUNAMADI ==")