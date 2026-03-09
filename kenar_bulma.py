import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# 1. Resim yolunu ayarla
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'shoes.png')

# Resmi yükle
img0 = cv2.imread(file_path)

# Kontrol: Resim yüklendi mi?
if img0 is None:
    print("Hata: shoes.png bulunamadı! Lütfen dosya adını kontrol et.")
else:
    # 2. Gri ölçeğine çevir
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

    # 3. Gürültü gider (Gaussian Blur)
    img = cv2.GaussianBlur(gray, (3, 3), 0)

    # 4. Sobel Birleştirme (ksize: 1, 3, 5, 7 denenebilir)
    k_val = 5
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=k_val)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=k_val)

    # Gradyanları birleştirme (L2 Normu)
    sobel_combined = cv2.sqrt(cv2.addWeighted(cv2.pow(sobelx, 2.0), 1.0, cv2.pow(sobely, 2.0), 1.0, 0.0))

    # 5. Scharr Birleştirme (ksize=-1 Sobel'de Scharr demektir)
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)

    # Mutlak değerleri alıp birleştirme
    scharr_absX = cv2.convertScaleAbs(scharrx)
    scharr_absY = cv2.convertScaleAbs(scharry)
    scharr_combined = cv2.addWeighted(scharr_absX, 0.5, scharr_absY, 0.5, 0)

    # Görselleştirme
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.subplot(1, 3, 2), plt.imshow(sobel_combined, cmap='gray'), plt.title(f'Sobel (k={k_val})')
    plt.subplot(1, 3, 3), plt.imshow(scharr_combined, cmap='gray'), plt.title('Scharr Combined')
    plt.show()