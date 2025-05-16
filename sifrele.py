from sozluk import ASAL_ALFABE, TERS_ALFABE

def sifrele(metin: str) -> list[int]:
    """Metni asal sayı listesine çevirir."""
    return [ASAL_ALFABE[harf] for harf in metin.lower() if harf in ASAL_ALFABE]

def coz(asal_liste: list[int]) -> str:
    """Asal sayı listesini metne çevirir."""
    return ''.join([TERS_ALFABE[sayi] for sayi in asal_liste if sayi in TERS_ALFABE])