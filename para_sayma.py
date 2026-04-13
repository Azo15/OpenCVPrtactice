import cv2
import numpy as np
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya_adi = 'Currency.png'
yol = os.path.join(klasor, dosya_adi)

img = cv2.imread(yol)

if img is None:
    print(f"HATA: Dosya bulunamadi!")
else:
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 9)

    # Parametreleri biraz daha sıktık (minDist=150 ve param2=50)
    # Boylece o bosluktaki hayalet dairelerden kurtulacagiz.
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=150,
                               param1=100, param2=50, minRadius=50, maxRadius=120)

    adet_1tl, adet_25kr, adet_5kr = 0, 0, 0
    toplam_tutar = 0.0

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            x, y, r = i[0], i[1], i[2]

            # SENIN EKRANINDAKI RAKAMLARA GORE TAM AYAR (image_c80ff8.jpg verisi)
            if r >= 80:  # 84, 90, 92 olanlar buraya girer
                etiket = "1 TL"
                renk = (0, 255, 0)
                adet_1tl += 1
                toplam_tutar += 1.0
            elif r >= 66:  # 67 olan buraya girer
                etiket = "25 Kurus"
                renk = (255, 0, 0)
                adet_25kr += 1
                toplam_tutar += 0.25
            else:  # 62, 64 olanlar buraya kalır
                etiket = "5 Kurus"
                renk = (0, 0, 255)
                adet_5kr += 1
                toplam_tutar += 0.05

            cv2.circle(output, (x, y), r, renk, 3)
            cv2.putText(output, etiket, (x - 35, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        # Terminal Çıktısı (Ödev Maddesi 2) [cite: 126, 128]
        print(f"\nSONUC: 1 TL: {adet_1tl} | 25 Kr: {adet_25kr} | 5 Kr: {adet_5kr}")
        print(f"HESAPLANAN TOPLAM: {toplam_tutar:.2f} TL")

        # Görsel Üzerine Yazdır
        cv2.putText(output, f"Toplam Tutar: {toplam_tutar:.2f} TL", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 3)

        cv2.imwrite('odev_teslim_sonuc.jpg', output)  # Kaydet [cite: 189]
        cv2.imshow('Uygulama II - Final', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()