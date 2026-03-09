import cv2
import numpy as np

def nothing(x):
    pass

# 1. Resmi yükle ve ikili (binary) hale getir [cite: 774]
# Not: Resimlerin yoksa beyaz zemin üzerine siyah şekiller olarak düşünebilirsin
img = cv2.imread('8.jpg', 0) 
if img is None:
    # Eğer resim yoksa test için siyah bir kare oluşturuyoruz
    img = np.zeros((300, 300), np.uint8)
    cv2.putText(img, '8', (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 7, 255, 15)

# Pencereyi oluştur ve Trackbar'ları ekle [cite: 1184]
cv2.namedWindow('Morfolojik Islemler')
# Islem: 0:Erosion, 1:Dilation, 2:Opening, 3:Closing, 4:Gradient, 5:TopHat, 6:BlackHat [cite: 1185]
cv2.createTrackbar('Islem', 'Morfolojik Islemler', 0, 6, nothing)
# Kernel Boyutu: 1-25 arası [cite: 1186]
cv2.createTrackbar('Kernel', 'Morfolojik Islemler', 3, 25, nothing)

while True:
    # Trackbar değerlerini oku
    islem_idx = cv2.getTrackbarPos('Islem', 'Morfolojik Islemler')
    k_size = cv2.getTrackbarPos('Kernel', 'Morfolojik Islemler')
    
    # Kernel boyutu en az 1 olmalı
    if k_size < 1: k_size = 1
    kernel = np.ones((k_size, k_size), np.uint8) [cite: 986]

    # İşlemi seç [cite: 1185]
    if islem_idx == 0:
        res = cv2.erode(img, kernel, iterations=1) [cite: 966, 987]
        title = "Asindirma (Erosion)"
    elif islem_idx == 1:
        res = cv2.dilate(img, kernel, iterations=1) [cite: 968, 988]
        title = "Yayma (Dilation)"
    elif islem_idx == 2:
        res = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) [cite: 1038, 1042]
        title = "Acma (Opening)"
    elif islem_idx == 3:
        res = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) [cite: 1066, 1069]
        title = "Kapama (Closing)"
    elif islem_idx == 4:
        res = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) [cite: 1091, 1093]
        title = "Gradyan (Gradient)"
    elif islem_idx == 5:
        res = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) [cite: 1119, 1123]
        title = "Top Hat"
    elif islem_idx == 6:
        res = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel) [cite: 1122, 1126]
        title = "Black Hat"

    # Sonuçları yan yana göster (Hoca tek plot istemişti) [cite: 1183]
    combined = np.hstack((img, res))
    cv2.putText(combined, f"Orijinal | {title}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    
    cv2.imshow('Morfolojik Islemler', combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()