import json

DOSYA_YOLU = "data/database.json"


def verileri_yukle():
    with open(DOSYA_YOLU, "r", encoding="utf-8") as dosya:
        veriler = json.load(dosya)

    return veriler

def verileri_kaydet(veriler):
    with open(DOSYA_YOLU, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, ensure_ascii=False, indent=4)