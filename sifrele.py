from sozluk import *

def sifrele(metin: str, kaydirma: bool = False) -> list[int]:
    """Metni asal sayılara çevirir (4 kaydırmalı veya temel)"""
    sozluk = KAYDIRMALI_ALFABE if kaydirma else TEMEL_ALFABE
    return [sozluk[harf] for harf in metin.lower() if harf in sozluk]

def coz(asal_liste: list[int], kaydirma: bool = False) -> str:
    """Asal sayıları metne çevirir (4 kaydırmalı veya temel)"""
    sozluk = TERS_KAYDIRMALI if kaydirma else TERS_TEMEL
    return ''.join([sozluk[sayi] for sayi in asal_liste if sayi in sozluk])
