import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. Resimleri yükle
img_rgb = cv.imread('messi5.jpeg')
# Hata Payını Bitirmek İçin: Ana resmi OpenCV standart boyutuna getiriyoruz
img_rgb = cv.resize(img_rgb, (448, 300))
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

template = cv.imread('messi_face.png', 0)
# Şablonu da standart boyuta getiriyoruz (Ders notundaki tam boyut)
template = cv.resize(template, (52, 58))

w, h = template.shape[::-1]

# En kararlı yöntem: TM_CCOEFF_NORMED
method = cv.TM_CCOEFF_NORMED

# Şablon Eşleştirmeyi Uygula
res = cv.matchTemplate(img_gray, template, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# Çizim
cv.rectangle(img_rgb, top_left, bottom_right, (0, 255, 0), 2)

# Gösterim
plt.figure(figsize=(10,5))
plt.subplot(121), plt.imshow(res, cmap='gray'), plt.title('Eşleşme Isı Haritası')
plt.subplot(122), plt.imshow(cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)), plt.title('Hedef Tespit Edildi')
plt.show()