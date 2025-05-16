from sifrele import sifrele, coz

if __name__ == "__main__":
    # Şifreleme örneği
    orjinal_metin = "aşık"
    sifreli = sifrele(orjinal_metin)
    print(f"Şifreli: {sifreli}")  # [2, 83, 37, 43, 3]

    # Çözme örneği
    cozulen = coz(sifreli)
    print(f"Çözülen: {cozulen}")  # "aşıkb"