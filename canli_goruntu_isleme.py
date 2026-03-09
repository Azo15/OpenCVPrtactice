import cv2
import numpy as np

def nothing(x):
    pass

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

# Kontrol penceresi oluştur ve konumlandır
cv2.namedWindow("Ayarlar")
cv2.moveWindow("Ayarlar", 0, 0)
cv2.resizeWindow("Ayarlar", 400, 200)

# Trackbar'ları oluştur
cv2.createTrackbar("Canny Min", "Ayarlar", 100, 500, nothing)
cv2.createTrackbar("Canny Max", "Ayarlar", 200, 500, nothing)
cv2.createTrackbar("Kernel Boyutu", "Ayarlar", 1, 15, nothing)

print("Çıkış yapmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü işlemlere hazırlamak için gri tonlamaya çeviriyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Trackbar değerlerini oku
    t_min = cv2.getTrackbarPos("Canny Min", "Ayarlar")
    t_max = cv2.getTrackbarPos("Canny Max", "Ayarlar")
    k_size = cv2.getTrackbarPos("Kernel Boyutu", "Ayarlar")
    
    # Kernel boyutu en az 1 olmalı
    if k_size < 1: k_size = 1
    kernel = np.ones((k_size, k_size), np.uint8)

    # --- GÖRÜNTÜ İŞLEME ---
    # 1. Kenar Çıkarma
    edges = cv2.Canny(gray, t_min, t_max)

    # 2. Aşındırma (Erosion)
    erosion = cv2.erode(edges, kernel, iterations=1)

    # 3. Yayma (Dilation)
    dilation = cv2.dilate(edges, kernel, iterations=1)

    # Görüntüleri 3 kanallı (renkli format) yap
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    erosion_bgr = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)
    dilation_bgr = cv2.cvtColor(dilation, cv2.COLOR_GRAY2BGR)

    # --- BOŞLUK EKLEME ---
    # Görüntüler arasına 10 piksellik siyah bir boşluk (ayraç) oluşturalım
    h, w, _ = edges_bgr.shape
    spacer = np.zeros((h, 15, 3), np.uint8) # 15 piksel genişliğinde siyah şerit

    # Görüntüleri yan yana, aralara spacer koyarak birleştir
    # Format: [Edges] | [Spacer] | [Erosion] | [Spacer] | [Dilation]
    result = np.concatenate((edges_bgr, spacer, erosion_bgr, spacer, dilation_bgr), axis=1)

    # Başlıkları ekle
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result, "KENAR (Canny)", (10, 30), font, 0.7, (0, 255, 0), 2)
    cv2.putText(result, "ASINDIRMA (Erosion)", (w + 25, 30), font, 0.7, (0, 255, 0), 2)
    cv2.putText(result, "YAYMA (Dilation)", (w * 2 + 40, 30), font, 0.7, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow("Webcam Analiz Paneli", result)
    cv2.moveWindow("Webcam Analiz Paneli", 0, 250)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()