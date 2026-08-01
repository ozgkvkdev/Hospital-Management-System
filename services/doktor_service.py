from models.doktor import Doktor
from utils.database import verileri_kaydet, verileri_yukle

veriler = verileri_yukle()

doktorlar = []

for veri in veriler["doktorlar"]:
    doktor = Doktor(
        ad=veri["ad"],
        soyad=veri["soyad"],
        yas=veri["yas"],
        tc_kimlik_no=veri["tc_kimlik_no"],
        telefon=veri["telefon"],
        doktor_id=veri["doktor_id"],
        brans=veri["brans"],
        uzmanlik=veri["uzmanlik"],
        poliklinik=veri["poliklinik"],
        musaitlik=veri["musaitlik"]
    )
    doktorlar.append(doktor)


def doktor_ekle():
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    yas = int(input("Yaşınızı Giriniz: "))
    tc_kimlik_no = input("TC Kimlik Numaranızı Giriniz: ")
    telefon = input("Telefon Numaranızı Giriniz: ")
    brans = input("Branşınızı Giriniz: ")
    uzmanlik = input("Uzmanlığınızı Giriniz: ")
    poliklinik = input("Polikliniğinizi Giriniz: ")
    musaitlik = True

    doktor_id = len(doktorlar) + 5001

    doktor = Doktor(
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
    )

    doktorlar.append(doktor)
    veriler["doktorlar"].append(doktor.to_dict())
    verileri_kaydet(veriler)

    print("Doktor başarıyla eklendi.")


def doktor_listele():
    if not doktorlar:
        print("Henüz kayıtlı doktor bulunmamaktadır.")
        return

    print("\n==KAYITLI DOKTORLAR==")
    for doktor in doktorlar:
        print(doktor)
        print("="*30)

def doktor_ara():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu=False
    for doktor in doktorlar:
        if doktor.tc_kimlik_no == tc_kimlik:
            bulundu=True
            print(doktor)
            break

    if not bulundu:
        print("DOKTOR BULUNMADI.") 


def doktor_sil():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu=False
    for doktor in doktorlar:
        if doktor.tc_kimlik_no == tc_kimlik:
            bulundu=True
            print("==DOKTOR SİLİNDİ==")
            doktorlar.remove(doktor)

            veriler["doktorlar"] = [
           d for d in veriler["doktorlar"]
           if d["tc_kimlik_no"] != tc_kimlik
           ]
            verileri_kaydet(veriler)

            print("== DOKTOR SİLİNDİ ==")
            break
    if not bulundu:
        print("== KAYITLI DOKTOR BULUNMADI.==")

def doktor_guncelle():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    bulundu = False

    for doktor in doktorlar:
        if doktor.tc_kimlik_no == tc_kimlik:
            bulundu = True

            print("== YENİ BİLGİLER ==")

            doktor.ad = input("Adınızı Giriniz: ")
            doktor.soyad = input("Soyadınızı Giriniz: ")
            doktor.yas = int(input("Yaşınızı Giriniz: "))
            doktor.telefon = input("Telefon Numaranızı Giriniz: ")
            doktor.brans = input("Branşınızı Giriniz: ")
            doktor.uzmanlik = input("Uzmanlığınızı Giriniz: ")
            doktor.poliklinik = input("Polikliniğinizi Giriniz: ")
            doktor.musaitlik = True

            
            for i, veri in enumerate(veriler["doktorlar"]):
                if veri["tc_kimlik_no"] == tc_kimlik:
                    veriler["doktorlar"][i] = doktor.to_dict()
                    break

            verileri_kaydet(veriler)

            print("\n== GÜNCELLENEN DOKTOR ==")
            print(doktor)
            break

    if not bulundu:
        print("\n== KAYITLI DOKTOR BULUNAMADI ==")