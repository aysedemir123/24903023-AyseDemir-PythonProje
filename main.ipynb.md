# BGY210 - Python Programlama II Dersi Final Projesi
## Kişisel Finans ve Harcama Takip Sistemi

**Öğrenci Bilgileri:**
* **Adı Soyadı:** [Adınızı Yazın]
* **Öğrenci Numarası:** [Numaranızı Yazın]
* **Bölüm:** [Bölümünüzü Yazın]

**Proje Açıklaması ve Yapısı:**
Bu proje, kullanıcıların gelir ve gider kalemlerini nesne yönelimli mimariyle modelleyip yönetmelerini sağlayan modüler bir finans otomasyonudur. Veriler kalıcı olarak CSV dosyasında saklanır, Pandas/NumPy kütüphaneleriyle analiz edilir ve Matplotlib ile görselleştirilir.

**Kullanılan Modüller:**
1. `finans_modeli.py`: `Islem` sınıf yapısını barındırır.
2. `islem_yonetimi.py`: Gelir/gider yönetimi ve listeleme mantığını kapsar.
3. `dosya_islemleri.py`: CSV tabanlı okuma/yazma süreçlerini yönetir.
4. `analiz.py`: Verilerin istatistiksel özetlerini çıkarır.
5. `gorsellestirme.py`: Matplotlib grafiklerini çizer.
6. `utils.py`: Giriş doğrulama ve arayüz fonksiyonlarını barındırır.
# Modüllerin projeye dahil edilmesi
import utils
import islem_yonetimi
import dosya_islemleri
import analiz
import gorsellestirme

def main():
    dosya_adi = "finans_verileri.csv"
    
    # Program başlarken eski verileri otomatik olarak CSV dosyasından yükler
    gelirler, giderler = dosya_islemleri.csv_oku(dosya_adi)
    
    while True:
        # Menüyü ekrana basar
        utils.menu_goster()
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-7): ")
        
        try:
            if secim == "1":
                islem_yonetimi.gelir_ekle(gelirler)
            elif secim == "2":
                islem_yonetimi.gider_ekle(giderler)
            elif secim == "3":
                islem_yonetimi.islemleri_listele(gelirler, giderler)
            elif secim == "4":
                df = analiz.verileri_dataframe_yap(gelirler, giderler)
                top_gelir, top_gider, net_bakiye = analiz.toplam_gelir_gider(df)
                print(f"\n--- FİNANSAL ÖZET RAPORU ---")
                print(f"Toplam Gelir : {top_gelir:.2f} TL")
                print(f"Toplam Gider : {top_gider:.2f} TL")
                print(f"Net Durum    : {net_bakiye:.2f} TL")
                
                # NumPy istatistiklerini ekrana basar
                analiz.numpy_istatistik(df)
                
                # Aylık detay tablosunu basar
                print("--- AY BAZLI ÖZET TABLO (PANDAS) ---")
                print(analiz.aylik_analiz(df))
            elif secim == "5":
                df = analiz.verileri_dataframe_yap(gelirler, giderler)
                if df.empty:
                    print("[Hata] Grafik çizmek için sistemde veri bulunmalıdır.")
                else:
                    gorsellestirme.gelir_gider_bar(df)
                    gorsellestirme.pasta_grafik(df)
                    gorsellestirme.aylik_grafik(df)
            elif secim == "6":
                dosya_islemleri.csv_kaydet(dosya_adi, gelirler, giderler)
            elif secim == "7":
                # Çıkış yaparken veri kaybını önlemek için otomatik kaydeder
                print("\n[Bilgi] Sistemden çıkış yapılıyor... Verileriniz kaydediliyor.")
                dosya_islemleri.csv_kaydet(dosya_adi, gelirler, giderler)
                print("Program sonlandırıldı. İyi günler!")
                break
            else:
                print("[Hata] Geçersiz seçim! Lütfen 1 ile 7 arasında bir sayı giriniz.")
        except Exception as e:
            print(f"[Beklenmedik Hata]: {e}")

# Programı tetikleyen ana gövde
if __name__ == "__main__":
    main()