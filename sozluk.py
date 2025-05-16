# Türkçe harfler ve asal sayı eşleşmeleri
ASAL_ALFABE = {
    ' ': 0,
    'a': 2, 'b': 3, 'c': 5, 'ç': 7, 'd': 11,
    'e': 13, 'f': 17, 'g': 19, 'ğ': 23, 'h': 29,
    'ı': 31, 'i': 37, 'j': 41, 'k': 43, 'l': 47,
    'm': 53, 'n': 59, 'o': 61, 'ö': 67, 'p': 71,
    'r': 73, 's': 79, 'ş': 83, 't': 89, 'u': 97,
    'ü': 101, 'v': 103, 'y': 107, 'z': 109
}

# Ters eşleme (sayı → harf)
TERS_ALFABE = {sayi: harf for harf, sayi in ASAL_ALFABE.items()}