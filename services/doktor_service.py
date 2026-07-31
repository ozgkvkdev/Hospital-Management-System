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