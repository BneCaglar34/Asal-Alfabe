# Türkçe Asal Şifreleyici (Temel + 4 Kaydırmalı)

## 🔢 Alfabe Sistemleri
1. **Temel Asal Alfabe**  
   `a=2, b=3, c=5,..., z=109`

2. **4 Kaydırmalı Asal Alfabe**  
   `a=113, b=127, c=131,..., z=271`  
   *(Temel alfabenin devamındaki 4. asal sayılar)*

## 🎯 Kullanım
```python
# Temel alfabe ile şifrele
sifrele("merhaba", kaydirma=False) → [53, 13, 73, 29, 3, 2, 2]

# 4 kaydırmalı alfabe ile şifrele
sifrele("merhaba", kaydirma=True) → [197, 149, 229, 167, 127, 113, 113]

# Çözme (kaydirma parametresi eşleşmeli)
coz([197, 149, 229], kaydirma=True) → "mer"
