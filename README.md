# OpenCV Antrenmanları

Bu depo, görüntü işleme temellerini öğrenmek amacıyla hazırlanmış çeşitli OpenCV projelerini ve denemelerini içerir.

## 🚀 İçerik

Aşağıda depoda bulunan scriptlerin özetleri yer almaktadır:

| Dosya | Açıklama |
| :--- | :--- |
| `webcam_yuz_takip.py` | Kameradan canlı yüz algılama. |
| `canli_histogram.py` | Kamera görüntüsünün anlık renk histogramı. |
| `kenar_algilama.py` | Görüntü üzerinde kenar tespiti (Canny vb.). |
| `renk_secici.py` | Görüntüden renk seçme ve HSV takibi. |
| `roi_secimi.py` | Görüntü üzerinde ROI (İlgi Bölgesi) seçimi. |
| `first.py` | OpenCV temelleri ve şekil çizme. |

## 🛠️ Kurulum

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/Azo15/OpenCVPrtactice.git
   cd OpenCVPrtactice
   ```

2. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install opencv-python numpy
   ```

## 📖 Kullanım

Herhangi bir scripti çalıştırmak için:

```bash
python webcam_yuz_takip.py
```

> [!NOTE]
> Yüz algılama projeleri için `haarcascade_frontalface_default.xml` dosyasının script ile aynı dizinde olduğundan emin olun.

## 📄 Lisans
Bu proje eğitim amaçlıdır.

---

# OpenCV Practice

This repository contains various OpenCV projects and experiments designed for learning image processing fundamentals.

## 🚀 Contents

Below are summaries of the scripts found in this repository:

| File | Description |
| :--- | :--- |
| `webcam_yuz_takip.py` | Live face detection via webcam. |
| `canli_histogram.py` | Real-time color histogram of webcam feed. |
| `kenar_algilama.py` | Edge detection on images (Canny, etc.). |
| `renk_secici.py` | Color selection and HSV tracking. |
| `roi_secimi.py` | Region of Interest (ROI) selection. |
| `first.py` | OpenCV basics and shape drawing. |

## 🛠️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Azo15/OpenCVPrtactice.git
   cd OpenCVPrtactice
   ```

2. **Install requirements:**
   ```bash
   pip install opencv-python numpy
   ```

## 📖 Usage

To run any script:

```bash
python webcam_yuz_takip.py
```

> [!NOTE]
> Ensure that `haarcascade_frontalface_default.xml` is in the same directory as the script for face detection projects.

## 📄 License
This project is for educational purposes.
