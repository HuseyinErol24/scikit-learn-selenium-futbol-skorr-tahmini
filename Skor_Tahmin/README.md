# SkorTahmin

SkorTahmin, nesine.com web sitesinden alınan geçmiş maç verilerini kullanarak gelecekteki futbol maçları için skor tahmini yapmak amacıyla yazılmış bir Python script'idir.

## Açıklama
Bu Python kodu, web scraping (web sitesinden veri çekme) ve basit bir regresyon analizi kullanarak futbol takımlarının gol performansını tahmin etmeye çalışan bir sınıf içerir. Kod, Selenium kütüphanesini kullanarak bir web tarayıcısı başlatır, belirli bir futbol takımının son maçlarına ait verileri çeker, ardından bu verileri kullanarak ev sahibi ve deplasman takımlarının gelecekteki gol tahminlerini yapar. Ayrıca, bu tahminleri görselleştirmek için matplotlib kütüphanesini kullanarak bir grafik oluşturur.


## Gereksinimler

- Python 3.x
- Gerekli Python paketleri: selenium, scikit-learn, numpy, matplotlib

## Bağımlılıklar

Projenin çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:

- selenium
- numpy
- matplotlib
- scikit-learn

Bu kütüphaneleri yüklemek için terminalde şu komutu kullanabilirsiniz:

- pip install selenium
- pip install numpy
- pip install matplotlib
- pip install scikit-learn

## Kullanımı

SkorTahmin sınıfını içeren skor_tahmin.py dosyasını çalıştırın.
Program, Firefox tarayıcısını başlatarak belirli bir futbol takımının son maçlarına ait verileri çekecektir.
Regresyon analizi yaparak ev sahibi ve deplasman takımlarının gelecekteki gol tahminlerini gösterecek ve bu tahminleri bir grafik üzerinde görselleştirecektir.


## Hüseyin Erol