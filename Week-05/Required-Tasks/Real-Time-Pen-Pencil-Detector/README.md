# Real-Time Pen/Pencil Detector

YOLOv8n tabanlı, webcam görüntüsünde kalem tespiti projesi. Eğitim ve test akışı `real-time-pen-pencil-detector.ipynb` dosyasındadır; canlı kamera uygulaması `webcam_detector.py` dosyasıdır.

## Klasörler ve dosyalar

- `real-time-pen-pencil-detector.ipynb`: Veri kümesini hazırlama, YOLOv8n ince ayarı ve test değerlendirmesi.
- `webcam_detector.py`: OpenCV ile canlı webcam tahmini; kutu, sınıf güveni, canlı FPS ve değiştirilebilir eşik gösterir.
- `models/best.pt`: Eğittiğiniz model ağırlığını buraya kendiniz ekleyin. Büyük dosya ZIP'e dahil edilmemiştir.
- `dataset/`: Veri kümesi dosyalarını buraya yerleştirin; büyük veri ZIP'e dahil edilmemiştir.
- `REQUIRED-TASK.md`: Görev tanımının özgün metni.

## Çalıştırma

Python 3.10 veya 3.11 önerilir. Proje klasöründe terminal açıp bağımlılıkları kurun:

```bash
pip install ultralytics opencv-python
```

Eğitilmiş `best.pt` dosyasını `models/best.pt` konumuna koyun ve başlatın:

```bash
python webcam_detector.py
```

`Q` ile çıkın. `+` veya `=` güven eşiğini yükseltir, `-` düşürür. Kamera açılmazsa uygulama varsayılan kamera API'sine geçer; gerekirse `webcam_detector.py` içindeki `CAMERA_INDEX` değerini değiştirin. Kod CPU üzerinde çalışacak şekilde ayarlanmıştır.

## Veri kümesi ve atıf

Notebook, ZIP biçimindeki YOLO veri kümesini `/content` dizinine yüklemenizi ister. Veri kümesinin lisansını ve kaynağını burada belirtin; dataset dosyaları bu teslim ZIP'ine dahil değildir. Notebook, boş veya eksik etiketleri inceler, tek sınıflı eğitim düzenini hazırlar ve `best.pt` ağırlığını test kümesinde değerlendirir.

## Değerlendirme notları

Notebook içindeki kayıtlı test özeti 40 test görseli için Precision 0.9508, Recall 0.9104, mAP@50 0.9695 ve mAP@50–95 0.6962 olarak verilmiştir. Notebook, bazı anotasyonların eksik olabileceğini, test kümesinin küçük olduğunu, arka plan-only örnek bulunmadığını ve kalem türlerinin (pencil) doğrulanmadığını da not eder.

Notebook'ta üç canlı test koşulu için 15.6, 15.2 ve 14.8 FPS değerleri yer alıyor. Bunlar bu ortamda bağımsız olarak doğrulanmadı; kendi bilgisayarında tekrar ölçüp sonuçları buna göre güncelle. FPS donanım, çözünürlük ve kamera koşullarına göre değişir. Farklı ışık/arka plan testlerini gerçekten yaptıktan sonra gözlemlerini ekle.

## Sınırlamalar

- Tek özel sınıf hedeflenmiştir; modelinizin sınıf adını ve etiket kapsamını veri kümenizle doğrulayın.
- Statik test metrikleri, yeni ortamlarda webcam başarısını garanti etmez.
- Bu teslimde ağırlık dosyası ve veri kümesi boyut nedeniyle bulunmaz; kendi dosyalarınızı belirtilen klasörlere ekleyin.
