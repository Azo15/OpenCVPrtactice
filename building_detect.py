import cv2
import numpy as np

# 1. Görüntüyü yükle
img = cv2.imread('building.jpeg')
# 2. Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3. Kenar tespiti (Canny) uygula
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 4. Olasılıksal Hough Çizgi Dönüşümü parametreleri [cite: 154, 155]
minLineLength = 100
maxLineGap = 10

# Fonksiyonu uygula [cite: 156]
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

# 5. Tespit edilen çizgileri görsel üzerine çiz [cite: 158]
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2) # Kırmızı renkte çizim

# Sonucu göster
cv2.imshow('Bina Hat Tespiti', img)
cv2.waitKey(0)
cv2.destroyAllWindows()