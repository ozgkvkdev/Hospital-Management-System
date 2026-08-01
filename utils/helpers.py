def baslik_yaz(title):
    print("\n" + "=" * 30)
    print(title)
    print("=" * 30)


def bos_mu(deger):
    return deger is None or str(deger).strip() == ""
