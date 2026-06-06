# -*- coding: utf-8 -*-
"""
Modül: analiz.py
Açıklama: Pandas ve NumPy kütüphaneleri kullanılarak yapılan finansal analizler.
"""
import pandas as pd
import numpy as np

def verileri_dataframe_yap(gelirler: list, giderler: list) -> pd.DataFrame:
    """Gelir ve gider listelerini birleştirerek pandas DataFrame yapısına dönüştürür."""
    veri_listesi = []
    
    # Gelir nesnelerini sözlüğe çevirip listeye ekleme
    for g in gelirler:
        veri_listesi.append({
            'id': g.id, 'tutar': g.tutar, 'tarih': g.tarih, 'aciklama': g.aciklama, 'tip': g.tip
        })
        
    # Gider nesnelerini sözlüğe çevirip listeye ekleme
    for gd in giderler:
        veri_listesi.append({
            'id': gd.id, 'tutar': gd.tutar, 'tarih': gd.tarih, 'aciklama': gd.aciklama, 'tip': gd.tip
        })
        
    if not veri_listesi:
        return pd.DataFrame(columns=['id', 'tutar', 'tarih', 'aciklama', 'tip'])
        
    df = pd.DataFrame(veri_listesi)
    df['tarih'] = pd.to_datetime(df['tarih']) # Tarih sütununu datetime nesnesine dönüştürür
    return df

def toplam_gelir_gider(df: pd.DataFrame):
    """DataFrame üzerinden toplam gelir, toplam gider ve net bakiye değerlerini hesaplar."""
    if df.empty:
        return 0.0, 0.0, 0.0
        
    toplam_gelir = df[df['tip'] == 'gelir']['tutar'].sum()
    toplam_gider = df[df['tip'] == 'gider']['tutar'].sum()
    net_bakiye = toplam_gelir - toplam_gider
    
    return float(toplam_gelir), float(toplam_gider), float(net_bakiye)

def aylik_analiz(df: pd.DataFrame):
    """Verileri tarihe göre gruplayarak aylık bazda özet analiz oluşturur."""
    if df.empty:
        print("[Uyarı] Analiz edilecek veri bulunmuyor.")
        return None
        
    # Yıl-Ay bazında gruplama yapabilmek için geçici bir periyot sütunu ekleme
    df_temp = df.copy()
    df_temp['Ay'] = df_temp['tarih'].dt.to_period('M')
    
    # Ay ve Tip kırılımında tutarların toplamını hesaplama
    ozet = df_temp.groupby(['Ay', 'tip'])['tutar'].sum().unstack(fill_value=0)
    
    # Eksik sütunları garanti altına alma
    if 'gelir' not in ozet.columns:
        ozet['gelir'] = 0.0
    if 'gider' not in ozet.columns:
        ozet['gider'] = 0.0
        
    ozet['Net Fark'] = ozet['gelir'] - ozet['gider']
    return ozet

def numpy_istatistik(df: pd.DataFrame):
    """NumPy kullanarak işlem tutarları üzerinde istatistiksel hesaplamalar yapar."""
    if df.empty:
        print("[Uyarı] İstatistik hesaplamak için veri yok.")
        return
        
    tutarlar = df['tutar'].to_numpy()
    
    print("\n--- NUMPY GENEL İŞLEM İSTATİSTİKLERİ ---")
    print(f"Toplam İşlem Sayısı : {len(tutarlar)}")
    print(f"Ortalama İşlem Tutarı: {np.mean(tutarlar):.2f} TL")
    print(f"En Düşük İşlem Tutarı: {np.min(tutarlar):.2f} TL")
    print(f"En Yüksek İşlem Tutarı: {np.max(tutarlar):.2f} TL")
    print(f"Standart Sapma       : {np.std(tutarlar):.2f} TL")
    print("-" * 40)