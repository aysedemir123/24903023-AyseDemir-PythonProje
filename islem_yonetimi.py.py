# -*- coding: utf-8 -*-
"""
Modül: islem_yonetimi.py
Açıklama: Gelir ve gider ekleme, listeleme ve silme iş mantığı fonksiyonları.
"""
from finans_modeli import Islem
import utils

def gelir_ekle(gelirler: list):
    """Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gelir kaydı oluşturur ve listeye ekler."""
    print("\n--- YENİ GELİR EKLEME ---")
    
    # Tutar Alımı ve Kontrolü
    while True:
        tutar_input = input("Gelir tutarını giriniz (Örn: 1500.50): ")
        if utils.sayi_kontrol(tutar_input):
            tutar = float(tutar_input)
            break
        print("[Hata] Geçersiz tutar! Lütfen pozitif bir sayı giriniz.")
        
    # Tarih Alımı ve Kontrolü
    while True:
        tarih = input("Tarih giriniz (YYYY-MM-DD): ")
        if utils.tarih_kontrol(tarih):
            break
        print("[Hata] Geçersiz tarih formatı! YYYY-MM-DD şeklinde giriniz.")
        
    aciklama = input("Gelir açıklaması yazınız: ")
    
    # Benzersiz ID üretimi (Tüm gelir ve giderler arasında eşsiz olabilmesi için mevcut gelirler listesi baz alınır)
    yeni_id = utils.yeni_id_olustur(gelirler)
    
    # Nesne oluşturma ve listeye ekleme
    yeni_gelir = Islem(id=yeni_id, tutar=tutar, tarih=tarih, aciklama=aciklama, tip='gelir')
    gelirler.append(yeni_gelir)
    print(f"[Başarılı] Gelir kaydı başarıyla eklendi. (ID: {yeni_id})")

def gider_ekle(giderler: list):
    """Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gider kaydı oluşturur ve listeye ekler."""
    print("\n--- YENİ GIDER EKLEME ---")
    
    # Tutar Alımı ve Kontrolü
    while True:
        tutar_input = input("Gider tutarını giriniz (Örn: 250.00): ")
        if utils.sayi_kontrol(tutar_input):
            tutar = float(tutar_input)
            break
        print("[Hata] Geçersiz tutar! Lütfen pozitif bir sayı giriniz.")
        
    # Tarih Alımı ve Kontrolü
    while True:
        tarih = input("Tarih giriniz (YYYY-MM-DD): ")
        if utils.tarih_kontrol(tarih):
            break
        print("[Hata] Geçersiz tarih formatı! YYYY-MM-DD şeklinde giriniz.")
        
    aciklama = input("Gider açıklaması yazınız: ")
    
    # Benzersiz ID üretimi
    yeni_id = utils.yeni_id_olustur(giderler)
    
    # Nesne oluşturma ve listeye ekleme
    yeni_gider = Islem(id=yeni_id, tutar=tutar, tarih=tarih, aciklama=aciklama, tip='gider')
    giderler.append(yeni_gider)
    print(f"[Başarılı] Gider kaydı başarıyla eklendi. (ID: {yeni_id})")

def islemleri_listele(gelirler: list, giderler: list):
    """Tüm gelir ve gider kayıtlarını düzenli bir formatta ekrana yazdırır."""
    print("\n================== TÜM İŞLEMLER LİSTESİ ==================")
    
    if not gelirler and not giderler:
        print("Sistemde kayıtlı herhangi bir işlem bulunmamaktadır.")
        print("==========================================================")
        return

    print("\n--- GELİRLER ---")
    if not gelirler:
        print("Kayıtlı gelir bulunmuyor.")
    else:
        for gelir in gelirler:
            print(gelir)
            
    print("\n--- GİDERLER ---")
    if not giderler:
        print("Kayıtlı gider bulunmuyor.")
    else:
        for gider in giderler:
            print(gider)
    print("==========================================================")

def islem_sil(gelirler: list, giderler: list, id: int):
    """Verilen ID'ye sahip işlemi bularak ilgili listeden siler."""
    # Gelirler listesinde ara
    for i, gelir in enumerate(gelirler):
        if gelir.id == id:
            del gelirler[i]
            print(f"[Başarılı] ID: {id} olan gelir kaydı silindi.")
            return True
            
    # Giderler listesinde ara
    for i, gider in enumerate(giderler):
        if gider.id == id:
            del giderler[i]
            print(f"[Başarılı] ID: {id} olan gider kaydı silindi.")
            return True
            
    print(f"[Hata] ID: {id} olan herhangi bir işlem bulunamadı.")
    return False