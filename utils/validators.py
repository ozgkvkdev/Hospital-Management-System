import re
from datetime import datetime


def tc_kimlik_gecerli(tc_kimlik):
    return bool(re.fullmatch(r"\d{11}", tc_kimlik or ""))


def yas_gecerli(yas):
    return isinstance(yas, int) and 0 <= yas <= 120


def telefon_gecerli(telefon):
    return bool(re.fullmatch(r"\d{10,11}", telefon or ""))


def tarih_gecerli(tarih):
    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def saat_gecerli(saat):
    try:
        datetime.strptime(saat, "%H:%M")
        return True
    except ValueError:
        return False
