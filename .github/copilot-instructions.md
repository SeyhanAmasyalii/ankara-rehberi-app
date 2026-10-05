# Ankara Rehberi App - Copilot kurallari

## Dil
- Kod (degisken, fonksiyon adlari) Turkce karakter KULLANMADAN Turkce yazilir: acik_mi, lokanta, saat.
- Docstring ve yorumlar Turkce yazilir.
- Chat cevaplari Turkce verilir.

## Kod kurallari
- Python 3.12, tip ipuclari (type hints) zorunlu.
- Veri yapilari icin dataclass kullanilir.
- Harici kutuphane eklemeden once kullaniciya sor.

## Is kurallari
- Saatler 0-23 arasi tam sayidir.
- Kapanis saati DAHIL DEGILDIR: 22'de kapanan lokanta 22:00'de kapalidir.
- acilis == kapanis ise lokanta 7/24 aciktir.
- Gece yarisini gecen saatler desteklenir (orn. 18-02).

## Test
- Her yeni fonksiyon icin test_*.py dosyasina pytest testi yazilir.
- Sinir durumlari (gece yarisi, bos liste, esitlik) mutlaka test edilir.
- Degisiklikten sonra `python -m pytest -v` calistirilir.
- Liste alan her fonksiyon BOS LISTE icin ne dondurecegini docstring'de yazar ve bunu test eder. Bos listede hata firlatmaz; uygun bos degeri (None, [] veya 0) dondurur.
- Bir test basarisiz olursa once testin mi kodun mu yanlis oldugunu fonksiyonun imzasina ve docstring'ine bakarak belirle; sozlesmeyi degistirme.