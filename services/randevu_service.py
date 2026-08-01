from models.randevu import Randevu

from services.hasta_service import hastalar
from services.doktor_service import doktorlar

randevular=[

]

def randevu_olustur():
    secilen_hasta = None
    secilen_doktor = None
    hasta_tc = input("Hastanın TC Kimlik Numarasını Giriniz: ")
    bulundu=False
    for hasta in hastalar:
     if hasta.tc_kimlik_no == hasta_tc:
        bulundu = True
        secilen_hasta = hasta
        print("Hasta bulundu.")
        print(hasta)
        break

    if not bulundu:
     print("Hasta bulunamadı. Lütfen önce hasta kaydı oluşturun.")
     return




    doktor_tc = input("Doktorun TC Kimlik Numarasını Giriniz: ") 
    bulundu=False
    for doktor in doktorlar:
     if doktor.tc_kimlik_no == doktor_tc:
        bulundu = True
        secilen_doktor = doktor
        print("== DOKTOR BULUNDU ==")
        print(doktor)
        break

    if not bulundu:
     print("Doktor bulunamadı. Lütfen önce doktor kaydı oluşturun.")
     return 

    tarih = input("Randevu Tarihini Giriniz (YYYY-AA-GG): ")
    saat = input("Randevu Saatini Giriniz (HH:MM:) ")

    randevu_id = len(randevular) + 1
    durum = "Aktif"

    randevu = Randevu(randevu_id, secilen_hasta, secilen_doktor, tarih, saat, durum)
    randevular.append(randevu)
    print("Randevu başarıyla oluşturuldu.")
    print(randevu)