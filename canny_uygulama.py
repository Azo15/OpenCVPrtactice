import cv2
import numpy as np

# Boş bir fonksiyon tanımlıyoruz (Trackbar için gerekli)
def nothing(x):
    pass

# 1. Kamerayı başlat
cap = cv2.VideoCapture(0)

# 2. Bir pencere oluştur ve Trackbar'ları ekle [cite: 175]
cv2.namedWindow("Canny Kenar Algilama")
cv2.createTrackbar("Threshold1", "Canny Kenar Algilama", 100, 500, nothing)
cv2.createTrackbar("Threshold2", "Canny Kenar Algilama", 200, 500, nothing)

print("Uygulamadan çıkmak için 'q' tuşuna basınız.")

while True:
    # Kameradan kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü gri tonlamaya çevir (Canny gri resimde daha iyi çalışır)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Trackbar'lardaki anlık değerleri oku [cite: 175]
    t1 = cv2.getTrackbarPos("Threshold1", "Canny Kenar Algilama")
    t2 = cv2.getTrackbarPos("Threshold2", "Canny Kenar Algilama")

    # Canny algoritmasını uygula [cite: 153, 168]
    # threshold1 ve threshold2 değerleri trackbar'dan geliyor
    edges = cv2.Canny(gray, t1, t2)

    # Orijinal görüntüyü ve kenar görüntüsünü göster [cite: 169]
    cv2.imshow("Orijinal Kamera", frame)
    cv2.imshow("Canny Kenar Algilama", edges)

    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()