from sifrele import sifrele, coz

if __name__ == "__main__":
    # Temel alfabe ile
    sifreli_temel = sifrele("aşıkb", kaydirma=False)
    print(f"Temel Şifre: {sifreli_temel}")  # [2, 83, 37, 43, 3]

    # 4 kaydırmalı alfabe ile
    sifreli_kaydirma = sifrele("aşıkb", kaydirma=True)
    print(f"Kaydırmalı Şifre: {sifreli_kaydirma}")  # [113, 239, 179, 191, 127]

    # Çözme örnekleri
    print(coz(sifreli_temel, kaydirma=False))  # "aşıkb"
    print(coz(sifreli_kaydirma, kaydirma=True))  # "aşıkb"
