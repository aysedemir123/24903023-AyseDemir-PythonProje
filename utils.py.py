# -*- coding: utf-8 -*-
"""
Modül: utils.py
Açıklama: Girdi kontrolleri, ID üretimi ve menü yönetimi için yardımcı fonksiyonlar.
"""
from datetime import datetime

def yeni_id_olustur(liste: list) -> int:
    """
    Verilen listedeki en büyük ID'yi bulup bir artırarak yeni benzersiz ID üretir.
    Eğer liste boşsa 1 değerini döner.
    """
    if not liste:
        return 1
    # Listedeki tüm işlem nesnelerinin id'leri arasından en büyüğünü bulur
    en_buyuk_id = max(islem.id for islem in liste)
    return en_buyuk_id + 1

def tarih_kontrol(tarih: str) -> bool:
    """
    Girilen tarihin doğru formatta (YYYY-MM-DD) olup olmadığını kontrol eder.
    Doğruysa True, hatalıysa False döner.
    """
    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def sayi_kontrol(deger: str) -> bool:
    """
    Kullanıcıdan alınan değerin pozitif bir sayıya (float/int) 
    dönüştürülebilir olup olmadığını kontrol eder.
    try:
        sayi = float(deger)
        return sayi > 0
    except ValueError:
        return False

def menu_goster():
    """Programın ana menüsünü kullanıcıya ekrana yazdırır."""
    print("\n" + "="*40)
    print(" KİŞİSEL FİNANS VE HARCAMA TAKİP SİSTEMİ")
    print("="*40)
    print("1. Gelir Ekle")
    print("2. Gider Ekle")
    print("3. İşlemleri Listele")
    print("4. Finansal Analiz Yap (Pandas/NumPy)")
    print("5. Grafikleri Göster (Matplotlib)")
    print("6. Verileri CSV Dosyasına Kaydet")
    print("7. Çıkış")
    print("="*40)