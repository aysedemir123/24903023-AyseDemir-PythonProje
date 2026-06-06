# -*- coding: utf-8 -*-
"""
Modül: gorsellestirme.py
Açıklama: Matplotlib kullanılarak finansal verilerin grafiklere dökülmesi.
"""
import matplotlib.pyplot as plt
import pandas as pd

def aylik_grafik(df: pd.DataFrame):
    """Aylık gelir ve giderleri karşılaştıran çizgi grafiği oluşturur."""
    if df.empty:
        print("[Uyarı] Grafik çizilecek veri bulunmuyor.")
        return
        
    df_temp = df.copy()
    df_temp['Ay'] = df_temp['tarih'].dt.to_period('M').astype(str)
    ozet = df_temp.groupby(['Ay', 'tip'])['tutar'].sum().unstack(fill_value=0)
    
    if 'gelir' not in ozet.columns: ozet['gelir'] = 0
    if 'gider' not in ozet.columns: ozet['gider'] = 0

    plt.figure(figsize=(10, 5))
    plt.plot(ozet.index, ozet['gelir'], marker='o', color='green', label='Gelir', linewidth=2)
    plt.plot(ozet.index, ozet['gider'], marker='s', color='red', label='Gider', linewidth=2)
    
    plt.title('Aylara Göre Gelir ve Gider Trendi')
    plt.xlabel('Dönem (Yıl-Ay)')
    plt.ylabel('Tutar (TL)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig('aylik_trend_grafigi.png')
    plt.show()

def gelir_gider_bar(df: pd.DataFrame):
    """Toplam gelir ve gider değerlerini karşılaştıran sütun grafiği oluşturur."""
    if df.empty: return
    
    toplam_gelir = df[df['tip'] == 'gelir']['tutar'].sum()
    toplam_gider = df[df['tip'] == 'gider']['tutar'].sum()
    
    kategoriler = ['Toplam Gelir', 'Toplam Gider']
    degerler = [toplam_gelir, toplam_gider]
    renkler = ['#2ecc71', '#e74c3c']
    
    plt.figure(figsize=(6, 5))
    bars = plt.bar(kategoriler, degerler, color=renkler, width=0.5)
    plt.title('Toplam Gelir vs Toplam Gider Karşılaştırması')
    plt.ylabel('Tutar (TL)')
    
    # Sütunların üzerine değerlerini yazma
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f} TL', va='bottom', ha='center', weight='bold')
        
    plt.savefig('gelir_gider_bar_grafigi.png')
    plt.show()

def pasta_grafik(df: pd.DataFrame):
    """Gelir ve gider oranlarını gösteren pasta grafiği oluşturur."""
    if df.empty: return
    
    toplam_gelir = df[df['tip'] == 'gelir']['tutar'].sum()
    toplam_gider = df[df['tip'] == 'gider']['tutar'].sum()
    
    if toplam_gelir == 0 and toplam_gider == 0:
        print("[Uyarı] Pasta grafiği için tutarlar sıfır olamaz.")
        return
        
    etiketler = ['Gelir Oranı', 'Gider Oranı']
    oranlar = [toplam_gelir, toplam_gider]
    renkler = ['#a2de96', '#f2a6a6']
    
    plt.figure(figsize=(5, 5))
    plt.pie(oranlar, labels=etiketler, autopct='%1.1f%%', startangle=140, colors=renkler, explode=(0.05, 0))
    plt.title('Finansal Dağılım Oranları')
    plt.savefig('finansal_dagilim_pasta_grafigi.png')
    plt.show()