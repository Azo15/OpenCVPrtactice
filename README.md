# OpenCV Antrenmanları | OpenCV Practice

Bu depo, görüntü işleme temellerini öğrenmek amacıyla hazırlanmış çeşitli OpenCV projelerini ve denemelerini içerir.

This repository contains various OpenCV projects and experiments designed for learning image processing fundamentals.

## 🚀 İçerik | Contents

Aşağıda depoda bulunan scriptlerin özetleri yer almaktadır:
Below are summaries of the scripts found in this repository:

| Dosya / File | Açıklama | Description |
| :--- | :--- | :--- |
| `webcam_yuz_takip.py` | Kameradan canlı yüz algılama. | Live face detection via webcam. |
| `canli_histogram.py` | Kamera görüntüsünün anlık renk histogramı. | Real-time color histogram of webcam feed. |
| `kenar_algilama.py` | Görüntü üzerinde kenar tespiti (Canny vb.). | Edge detection on images (Canny, etc.). |
| `renk_secici.py` | Görüntüden renk seçme ve HSV takibi. | Color selection and HSV tracking. |
| `roi_secimi.py` | Görüntü üzerinde ROI (İlgi Bölgesi) seçimi. | Region of Interest (ROI) selection. |
| `first.py` | OpenCV temelleri ve şekil çizme. | OpenCV basics and shape drawing. |

## 🛠️ Kurulum | Installation

1. **Depoyu klonlayın | Clone the repo:**
   ```bash
   git clone https://github.com/Azo15/OpenCVPrtactice.git
   cd OpenCVPrtactice
   ```

2. **Gerekli kütüphaneleri yükleyin | Install requirements:**
   ```bash
   pip install opencv-python numpy
   ```

## 📖 Kullanım | Usage

Herhangi bir scripti çalıştırmak için:
To run any script:

```bash
python webcam_yuz_takip.py
```

> [!NOTE]
> Yüz algılama projeleri için `haarcascade_frontalface_default.xml` dosyasının script ile aynı dizinde olduğundan emin olun.
> Ensure that `haarcascade_frontalface_default.xml` is in the same directory as the script for face detection projects.

## 📄 Lisans | License
Bu proje eğitim amaçlıdır.
This project is for educational purposes.
