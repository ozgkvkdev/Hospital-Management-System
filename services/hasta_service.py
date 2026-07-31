from models.hasta import Hasta

hastalar = []


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

    hastalar.append(hasta)
    print("Hasta başarıyla eklendi.")