import cv2
import numpy as np

# Görseli yükle
img = cv2.imread('Currency.jpg')
output = img.copy()
# Gri tonlamaya çevir (HoughCircles için gereklidir) [cite: 208, 213]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# PDF'te tavsiye edilen gürültü azaltma [cite: 209, 210]
gray = cv2.medianBlur(gray, 7)

# Hough Daire Dönüşümü
# dp=1.2: Akümülatör çözünürlüğü [cite: 217, 218]
# minDist=100: Paralar arası min mesafe [cite: 222]
# param1=100: Canny üst eşiği [cite: 226]
# param2=40: Akümülatör eşiği (Düşürürseniz daha çok daire bulur) [cite: 228, 229]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                           param1=100, param2=40, minRadius=50, maxRadius=150)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Dış çerçeveyi çiz (Yeşil) [cite: 247]
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 4)
        # Merkezi çiz (Kırmızı) [cite: 249]
        cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Madeni Para Tespiti', output)
cv2.waitKey(0)
cv2.destroyAllWindows()