import cv2
import numpy as np

# 1. Boş (siyah) bir görüntü oluştur (512x512 piksel)
# Görüntü işleme dersinde her şey bir matristir!
canvas = np.zeros((512, 512, 3), dtype="uint8")

# 2. Üzerine bir dikdörtgen çiz (Mavi renk)
# OpenCV'de renkler BGR sırasıyla verilir: (Mavi, Yeşil, Kırmızı)
cv2.rectangle(canvas, (100, 100), (400, 400), (255, 0, 0), 3)

# 3. Üzerine bir yazı yaz
cv2.putText(canvas, "OpenCV Hazir!", (150, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 4. Görüntüyü bir pencerede göster
cv2.imshow("Ders 1: Merhaba OpenCV", canvas)

# 5. Bir tuşa basana kadar pencereyi kapatma
cv2.waitKey(0)
cv2.destroyAllWindows() 