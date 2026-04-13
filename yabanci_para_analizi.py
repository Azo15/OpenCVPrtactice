import cv2
import numpy as np
import os

klasor = os.path.dirname(os.path.abspath(__file__))
# Dosya adını kontrol et (euro_coins.jpg veya Currency.jpg mi?)
dosya_adi = 'euro_coins.jpg' 
yol = os.path.join(klasor, dosya_adi)

img = cv2.imread(yol)

if img is None:
    print(f"HATA: {dosya_adi} bulunamadi!")
else:
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 9)

    # Daireleri bulma
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=120,
                               param1=100, param2=50, minRadius=30, maxRadius=150)

    toplam_euro = 0.0

    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        for i in circles[0, :]:
            x, y, r = i[0], i[1], i[2]
            
            # EURO PARALARI İÇİN HASSAS YARIÇAP AYARLARI
            # Senin görselindeki boyutlara göre (image_c87177.jpg)
            if r >= 105: 
                etiket, deger, renk = "2 Euro", 2.0, (0, 255, 0)
            elif r >= 92: 
                etiket, deger, renk = "1 Euro", 1.0, (255, 0, 0)
            elif r >= 85: 
                etiket, deger, renk = "50 Cent", 0.50, (0, 165, 255) # Turuncu
            elif r >= 75: 
                etiket, deger, renk = "20 Cent", 0.20, (255, 255, 0) # Sarı
            elif r >= 68: 
                etiket, deger, renk = "10 Cent", 0.10, (0, 0, 255) # Kırmızı
            elif r >= 60: 
                etiket, deger, renk = "5 Cent", 0.05, (128, 0, 128) # Mor
            else: 
                etiket, deger, renk = "Cent (Kucuk)", 0.01, (255, 255, 255) # Beyaz

            toplam_euro += deger
            cv2.circle(output, (x, y), r, renk, 4)
            cv2.putText(output, etiket, (x-40, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
            print(f"Para: {etiket} | Radius: {r}")

        # Ekrana ve terminale yazdır
        print("-" * 30)
        print(f"TOPLAM TUTAR: {toplam_euro:.2f} EUR")

        cv2.putText(output, f"Toplam: {toplam_euro:.2f} EUR", (30, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)
        
        cv2.imshow('Euro Analizi - Hassas Ayar', output)
        cv2.imwrite('yabanci_para_sonuc_final.jpg', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()