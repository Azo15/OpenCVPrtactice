import cv2
import numpy as np


def nothing(x):
    pass


# 1. '8.jpg' dosyasını yükleeref
# Görüntü ikili (binary) olmalıdır [cite: 774]
img = cv2.imread('8.jpg', 0)

# Resim bulunamazsa uyarı ver ve boş bir görüntü oluştur
if img is None:
    print("Uyarı: '8.jpg' bulunamadı! Lütfen dosya yolunu kontrol edin.")
    img = np.zeros((300, 300), np.uint8)
    cv2.putText(img, '8', (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 7, 255, 15)

# Pencere oluştur ve Trackbar'ları ekle [cite: 1184]
cv2.namedWindow('Morfolojik Islemler')

# İşlem seçimi için trackbar (0-6 arası) [cite: 1185]
cv2.createTrackbar('Islem', 'Morfolojik Islemler', 0, 6, nothing)
# Kernel boyutu seçimi için trackbar [cite: 1186]
cv2.createTrackbar('Kernel', 'Morfolojik Islemler', 3, 25, nothing)

print("Çıkmak için 'q' tuşuna basın.")

while True:
    # Trackbar değerlerini oku
    islem_idx = cv2.getTrackbarPos('Islem', 'Morfolojik Islemler')
    k_size = cv2.getTrackbarPos('Kernel', 'Morfolojik Islemler')

    # Kernel boyutu en az 1 olmalı [cite: 991]
    if k_size < 1: k_size = 1
    # Yapı elemanı (kernel) oluşturuluyor [cite: 777, 986]
    kernel = np.ones((k_size, k_size), np.uint8)

    # Morfolojik işlemleri uygula [cite: 1181]
    if islem_idx == 0:
        res = cv2.erode(img, kernel, iterations=1)  # Aşındırma [cite: 966]
        title = "Asindirma (Erosion)"
    elif islem_idx == 1:
        res = cv2.dilate(img, kernel, iterations=1)  # Yayma [cite: 968]
        title = "Yayma (Dilation)"
    elif islem_idx == 2:
        res = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # Açma [cite: 1038]
        title = "Acma (Opening)"
    elif islem_idx == 3:
        res = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # Kapama [cite: 1066]
        title = "Kapama (Closing)"
    elif islem_idx == 4:
        res = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # Gradyan [cite: 1091]
        title = "Gradyan (Gradient)"
    elif islem_idx == 5:
        res = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)  # Top Hat [cite: 1119]
        title = "Top Hat"
    else:
        res = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)  # Black Hat [cite: 1122]
        title = "Black Hat"

    # Orijinal ve sonucu yan yana birleştir
    combined = np.hstack((img, res))
    cv2.putText(combined, f"Orijinal | {title}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, 255, 2)

    cv2.imshow('Morfolojik Islemler', combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()