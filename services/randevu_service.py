from models.randevu import Randevu
from services.hasta_service import hastalar
from services.doktor_service import doktorlar
from utils.database import verileri_yukle, verileri_kaydet
from utils.validators import tarih_gecerli, saat_gecerli

veriler = verileri_yukle()

randevular = []

for veri in veriler["randevular"]:
    hasta = None
    doktor = None

    for h in hastalar:
        if h.tc_kimlik_no == veri["hasta_tc"]:
            hasta = h
            break

    for d in doktorlar:
        if d.tc_kimlik_no == veri["doktor_tc"]:
            doktor = d
            break

    if hasta and doktor:
        randevu = Randevu(
            randevu_id=veri["randevu_id"],
            hasta=hasta,
            doktor=doktor,
            tarih=veri["tarih"],
            saat=veri["saat"],
            durum=veri["durum"]
        )
        randevular.append(randevu)


def randevu_olustur():
    secilen_hasta = None
    secilen_doktor = None

    hasta_tc = input("Hastanın TC Kimlik Numarasını Giriniz: ")
    for hasta in hastalar:
        if hasta.tc_kimlik_no == hasta_tc:
            secilen_hasta = hasta
            print("Hasta bulundu.")
            print(hasta)
            break

    if secilen_hasta is None:
        print("Hasta bulunamadı. Lütfen önce hasta kaydı oluşturun.")
        return

    doktor_tc = input("Doktorun TC Kimlik Numarasını Giriniz: ")
    for doktor in doktorlar:
        if doktor.tc_kimlik_no == doktor_tc:
            secilen_doktor = doktor
            print("== DOKTOR BULUNDU ==")
            print(doktor)
            break

    if secilen_doktor is None:
        print("Doktor bulunamadı. Lütfen önce doktor kaydı oluşturun.")
        return

    tarih = input("Randevu Tarihini Giriniz (YYYY-MM-DD): ")
    saat = input("Randevu Saatini Giriniz (HH:MM): ")

    if not tarih_gecerli(tarih):
        print("Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatında girin.")
        return

    if not saat_gecerli(saat):
        print("Geçersiz saat formatı. Lütfen HH:MM formatında girin.")
        return

    randevu_id = len(randevular) + 1
    durum = "Aktif"

    randevu = Randevu(randevu_id, secilen_hasta, secilen_doktor, tarih, saat, durum)
    randevular.append(randevu)

    veriler["randevular"].append(randevu.to_dict())
    verileri_kaydet(veriler)

    print("Randevu başarıyla oluşturuldu.")
    print(randevu)

def randevu_listele():
  if not randevular:
    print("Henüz kayıtlı randevu bulunamamaktadır.")
    return

  print("\n== KAYITLI RANDEVULAR ==")
  for randevu in randevular:
    print(randevu)
    print("="*40)

def randevu_ara():
    tc_kimlik=input("TC Kimlik Numaranızı Giriniz:")
    bulundu=False
    for randevu in randevular:
        if randevu.hasta.tc_kimlik_no == tc_kimlik:
            bulundu=True
            print("== RANDEVU BULUNDU ==")
            print(randevu)
            break
    if not bulundu:
        print("Randevu bulunamadı.")

def randevu_iptal_et():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz: ")
    bulundu = False

    for randevu in randevular:
        if randevu.hasta.tc_kimlik_no == tc_kimlik:
            bulundu = True

            randevu.durum = "İptal Edildi"

            # JSON'u güncelle
            for i, veri in enumerate(veriler["randevular"]):
                if veri["randevu_id"] == randevu.randevu_id:
                    veriler["randevular"][i] = randevu.to_dict()
                    break

            verileri_kaydet(veriler)

            print("== RANDEVU İPTAL EDİLDİ ==")
            break

    if not bulundu:
        print("Randevu bulunamadı.")


def randevu_guncelle():
    tc_kimlik = input("TC Kimlik Numaranızı Giriniz:")
    bulundu = False

    for randevu in randevular:
        if randevu.hasta.tc_kimlik_no == tc_kimlik:
            bulundu = True
            print("== RANDEVU GÜNCELLENDİ ==")
            yeni_tarih = input("Yeni Randevu Tarihini Giriniz (YYYY-MM-DD): ")
            yeni_saat = input("Yeni Randevu Saatini Giriniz (HH:MM): ")

            if not tarih_gecerli(yeni_tarih):
                print("Geçersiz tarih formatı. İşlem iptal edildi.")
                return

            if not saat_gecerli(yeni_saat):
                print("Geçersiz saat formatı. İşlem iptal edildi.")
                return

            randevu.tarih = yeni_tarih
            randevu.saat = yeni_saat

            for i, veri in enumerate(veriler["randevular"]):
                if veri["randevu_id"] == randevu.randevu_id:
                    veriler["randevular"][i] = randevu.to_dict()
                    break

            verileri_kaydet(veriler)
            break

    if not bulundu:
        print("Randevu bulunamadı.")
