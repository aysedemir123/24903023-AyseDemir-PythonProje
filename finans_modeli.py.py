# -*- coding: utf-8 -*-
"""
Modül: finans_modeli.py
Açıklama: Sistemdeki finansal işlemleri temsil eden nesne tabanlı sınıf yapısı.
"""

class Islem:
    """
    Sistemdeki her bir gelir veya gider kaydını temsil eden sınıf.
    """
    def __init__(self, id: int, tutar: float, tarih: str, aciklama: str, tip: str):
        """
        Islem sınıfının yapıcı (constructor) metodu.
        
        Parametreler:
        - id (int): İşleme ait benzersiz kimlik numarası.
        - tutar (float): İşlemin parasal değeri.
        - tarih (str): YYYY-MM-DD formatında işlem tarihi.
        - aciklama (str): İşlemin detay açıklaması.
        - tip (str): 'gelir' veya 'gider' değerini alır.
        """
        self.id = id
        self.tutar = tutar
        self.tarih = tarih
        self.aciklama = aciklama
        self.tip = tip

    def __str__(self):
        """Nesnenin ekrana düzenli yazdırılmasını sağlayan metot."""
        return f"[ID: {self.id}] | Tür: {self.tip.upper()} | Tutar: {self.tutar} TL | Tarih: {self.tarih} | Açıklama: {self.aciklama}"