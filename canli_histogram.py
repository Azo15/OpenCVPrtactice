import cv2
import numpy as np
from matplotlib import pyplot as plt

# Kamerayi baslat
cap = cv2.VideoCapture(0)

print("Histogram uygulamasi baslatildi. Cikmak icin 'q' tusuna basin.")
  
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Goruntuyu Gri Seviyeye cevir (Tek kanal histogrami daha kolay anlasilir)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Histogram hesapla
    # [gray]: kaynak goruntu, [0]: kanal indeksi, None: maske yok
    # [256]: her renk degeri icin bir kutu, [0, 256]: deger araligi
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # 3. Histogrami gosterilecek bir "goruntu"ye donustur
    # Bu adim grafigi ayri bir pencere gibi gormemizi saglar
    hist_img = np.zeros((300, 256), dtype="uint8")
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    
    for i in range(1, 256):
        cv2.line(hist_img, (i - 1, 300 - int(hist[i - 1])),
                 (i, 300 - int(hist[i])), (255), 2)

    # Orijinal gri goruntuyu ve histogram grafigini goster
    cv2.imshow('Gri Goruntu', gray)
    cv2.imshow('Anlik Histogram', hist_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()