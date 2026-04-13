import cv2
import numpy as np

img = cv2.imread('Currency.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 7)

# Parametrelerle paraları bul
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100,
                           param1=100, param2=40, minRadius=50, maxRadius=150)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        radius = i[2] # Yarıçap bilgisini al [cite: 214, 273]
        center = (i[0], i[1])
        
        # Yarıçapa göre basit mantık (Değerleri görsele göre ayarlayabilirsin)
        if radius > 115:
            renk = (0, 255, 0) # Büyük paralar (1 TL) Yeşil
            etiket = "Buyuk"
        elif radius > 90:
            renk = (255, 0, 0) # Orta paralar (25 Kuruş) Mavi
            etiket = "Orta"
        else:
            renk = (0, 0, 255) # Küçük paralar (5 Kuruş) Kırmızı
            etiket = "Kucuk"
            
        cv2.circle(img, center, radius, renk, 4)
        cv2.putText(img, etiket, (i[0]-20, i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

cv2.imshow('Boyut Sınıflandırma', img)
cv2.waitKey(0)
cv2.destroyAllWindows()