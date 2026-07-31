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


def hasta_listele():
    if not hastalar:
        print("Henüz kayıtlı hasta bulunmamaktadır.")
        return

    print("\n== KAYITLI HASTALAR ==")

    for hasta in hastalar:
        print(hasta)
        print("-" * 40)


def hasta_ara():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu=False
    for hasta in hastalar:
        if hasta.tc_kimlik_no == tc_kimlik:
            bulundu=True
            print("==HASTA==")
            break

    if not bulundu:
     print("Hasta Bulunamadı.")   


def hasta_sil():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu=False
    for hasta in hastalar:
        if hasta.tc_kimlik_no ==  tc_kimlik:
            bulundu=True
            print("== HASTA SİLİNDİ==")
            hastalar.remove(hasta)
            break

    if not bulundu:
     print("Hasta Bulunamadı")


def hasta_guncelle():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu= False
    for hasta in hastalar:
        if hasta.tc_kimlik_no == tc_kimlik:
            bulundu=True
            print("==YENİ BİLGİLER==")
            ad = input("Adınızı Giriniz: ")
            soyad = input("Soyadınızı Giriniz: ")
            yas = int(input("Yaşınızı Giriniz: "))
            telefon = input("Telefon Numaranızı Giriniz: ")
            kan_grubu = input("Kan Grubunuzu Giriniz: ")
            aciliyet_durumu = input("Aciliyet Durumunuzu Giriniz: ")
            hasta.ad = ad
            hasta.soyad = soyad
            hasta.yas = yas
            hasta.telefon = telefon
            hasta.kan_grubu = kan_grubu
            hasta.aciliyet_durumu = aciliyet_durumu
            print("\n== GÜNCELLENEN HASTA ==")
            print(hasta)
            break
            
            
            

    if not bulundu:
        print("==HASTA BULUNAMADI==")        

                 