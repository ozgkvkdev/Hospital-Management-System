from services.hasta_service import (
    hasta_ekle,
    hasta_listele,
    hasta_ara,
    hasta_sil,
    hasta_guncelle
)

from services.doktor_service import (
    doktor_ekle,
    doktor_listele,
    doktor_ara,
    doktor_sil,
    doktor_guncelle
)

from services.randevu_service import (
    randevu_olustur,
    randevu_listele,
    randevu_ara,
    randevu_guncelle,
    randevu_iptal_et
)


def hasta_menu():
    while True:
        print("\n=== HASTA İŞLEMLERİ ===")
        print("1- Hasta Ekle")
        print("2- Hasta Listele")
        print("3- Hasta Ara")
        print("4- Hasta Sil")
        print("5- Hasta Güncelle")
        print("0- Ana Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            hasta_ekle()
        elif secim == "2":
            hasta_listele()
        elif secim == "3":
            hasta_ara()
        elif secim == "4":
            hasta_sil()
        elif secim == "5":
            hasta_guncelle()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")


def doktor_menu():
    while True:
        print("\n=== DOKTOR İŞLEMLERİ ===")
        print("1- Doktor Ekle")
        print("2- Doktor Listele")
        print("3- Doktor Ara")
        print("4- Doktor Sil")
        print("5- Doktor Güncelle")
        print("0- Ana Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            doktor_ekle()
        elif secim == "2":
            doktor_listele()
        elif secim == "3":
            doktor_ara()
        elif secim == "4":
            doktor_sil()
        elif secim == "5":
            doktor_guncelle()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")


def randevu_menu():
    while True:
        print("\n=== RANDEVU İŞLEMLERİ ===")
        print("1- Randevu Oluştur")
        print("2- Randevu Listele")
        print("3- Randevu Ara")
        print("4- Randevu Güncelle")
        print("5- Randevu İptal Et")
        print("0- Ana Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            randevu_olustur()
        elif secim == "2":
            randevu_listele()
        elif secim == "3":
            randevu_ara()
        elif secim == "4":
            randevu_guncelle()
        elif secim == "5":
            randevu_iptal_et()
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")


def ana_menu():
    while True:
        print("\n===================================")
        print("     HASTANE YÖNETİM SİSTEMİ")
        print("===================================")
        print("1- Hasta İşlemleri")
        print("2- Doktor İşlemleri")
        print("3- Randevu İşlemleri")
        print("4- Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            hasta_menu()
        elif secim == "2":
            doktor_menu()
        elif secim == "3":
            randevu_menu()
        elif secim == "4":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    ana_menu()