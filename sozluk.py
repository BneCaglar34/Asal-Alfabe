# Temel Asal Alfabe
TEMEL_ALFABE = {
    'a': 2, 'b': 3, 'c': 5, 'ç': 7, 'd': 11,
    'e': 13, 'f': 17, 'g': 19, 'ğ': 23, 'h': 29,
    'ı': 31, 'i': 37, 'j': 41, 'k': 43, 'l': 47,
    'm': 53, 'n': 59, 'o': 61, 'ö': 67, 'p': 71,
    'r': 73, 's': 79, 'ş': 83, 't': 89, 'u': 97,
    'ü': 101, 'v': 103, 'y': 107, 'z': 109
}

# 4 Kaydırmalı Asal Alfabe (Sonraki 4 asal sayı)
KAYDIRMALI_ALFABE = {
    'a': 11, 'b': 13, 'c': 17, 'ç': 19, 'd': 23,
    'e': 29, 'f': 31, 'g': 37, 'ğ': 41, 'h': 43,
    'ı': 47, 'i': 53, 'j': 59, 'k': 61, 'l': 67,
    'm': 71, 'n': 73, 'o': 79, 'ö': 83, 'p': 89,
    'r': 97, 's': 101, 'ş': 103, 't': 107, 'u': 109,
    'ü': 2, 'v': 3, 'y': 5, 'z': 7
}

# Ters eşlemeler
TERS_TEMEL = {v: k for k, v in TEMEL_ALFABE.items()}
TERS_KAYDIRMALI = {v: k for k, v in KAYDIRMALI_ALFABE.items()}
