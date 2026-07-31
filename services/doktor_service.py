from models.doktor import Doktor

doktorlar = []


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
            break
    if not bulundu:
        print("== KAYITLI DOKTOR BULUNMADI.==")


def doktor_guncelle():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz:")
    bulundu = False

    for doktor in doktorlar:
        if doktor.tc_kimlik_no == tc_kimlik:
            bulundu = True

            print("== YENİ BİLGİLER ==")

            ad = input("Adınızı Giriniz: ")
            soyad = input("Soyadınızı Giriniz: ")
            yas = int(input("Yaşınızı Giriniz: "))
            telefon = input("Telefon Numaranızı Giriniz: ")
            brans = input("Branşınızı Giriniz: ")
            uzmanlik = input("Uzmanlığınızı Giriniz: ")
            poliklinik = input("Polikliniğinizi Giriniz: ")
            musaitlik = True

            doktor.ad = ad
            doktor.soyad = soyad
            doktor.yas = yas
            doktor.telefon = telefon
            doktor.brans = brans
            doktor.uzmanlik = uzmanlik
            doktor.poliklinik = poliklinik
            doktor.musaitlik = musaitlik

            print("\n== GÜNCELLENEN DOKTOR ==")
            print(doktor)
            break

    if not bulundu:
        print("\n== KAYITLI DOKTOR BULUNAMADI ==")