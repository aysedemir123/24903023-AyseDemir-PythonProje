# -*- coding: utf-8 -*-
"""
Modül: dosya_islemleri.py
Açıklama: Verilerin CSV dosyasına yazılması ve dosyadan okunması işlemleri.
"""
import csv
from finans_modeli import Islem

def csv_kaydet(dosya_adi: str, gelirler: list, giderler: list):
    """Tüm gelir ve gider verilerini belirtilen CSV dosyasına kaydeder."""
    try:
        with open(dosya_adi, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Başlık satırı (Header)
            writer.writerow(['id', 'tutar', 'tarih', 'aciklama', 'tip'])
            
            # Gelirleri yaz
            for g in gelirler:
                writer.writerow([g.id, g.tutar, g.tarih, g.aciklama, g.tip])
                
            # Giderleri yaz
            for gd in giderler:
                writer.writerow([gd.id, gd.tutar, gd.tarih, gd.aciklama, gd.tip])
                
        print(f"[Başarılı] Veriler '{dosya_adi}' dosyasına başarıyla kaydedildi.")
    except Exception as e:
        print(f"[Hata] Dosyaya yazılırken bir hata oluştu: {e}")

def csv_oku(dosya_adi: str):
    """CSV dosyasındaki verileri okuyarak gelir ve gider listelerini oluşturur."""
    gelirler = []
    giderler = []
    try:
        with open(dosya_adi, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader) # Başlık satırını atla
            
            for row in reader:
                if not row:
                    continue
                # Veri tiplerini dönüştürerek oku
                id_val = int(row[0])
                tutar_val = float(row[1])
                tarih_val = row[2]
                aciklama_val = row[3]
                tip_val = row[4]
                
                # Nesneyi oluştur
                islem_obj = Islem(id_val, tutar_val, tarih_val, aciklama_val, tip_val)
                
                # Tipine göre ilgili listeye ata
                if tip_val == 'gelir':
                    gelirler.append(islem_obj)
                elif tip_val == 'gider':
                    giderler.append(islem_obj)
                    
        print(f"[Başarılı] '{dosya_adi}' dosyasından veriler yüklendi. ({len(gelirler)} Gelir, {len(giderler)} Gider)")
    except FileNotFoundError:
        print(f"[Bilgi] '{dosya_adi}' dosyası bulunamadı. Yeni bir veri seti ile başlanıyor.")
    except Exception as e:
        print(f"[Hata] Dosya okunurken bir hata oluştu: {e}")
        
    return gelirler, giderler