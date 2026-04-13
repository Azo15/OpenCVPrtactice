import cv2
import numpy as np
import os

# 1. DOSYA YOLU KONTROLÜ
# Kodu ve görseli aynı klasöre koyarsan bu kısım hatasız çalışacaktır.
script_dir = os.path.dirname(__file__)
img_path = os.path.join(script_dir, 'Currency.jpg')  # Eğer dosyan png ise 'Currency.png' yap

img = cv2.imread(img_path)

if img is None:
    print(f"HATA: {img_path} bulunamadı! Lütfen görselin kodla aynı klasörde olduğundan emin ol.")
else:
    # 2. ÖN İŞLEME
    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # PDF Tavsiyesi: Gürültü azaltma [cite: 209, 210, 261]
    gray = cv2.medianBlur(gray, 7)

    # 3. HOUGH DAİRE DÖNÜŞÜMÜ [cite: 208, 264, 265]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=80,
                               param1=100, param2=35, minRadius=40, maxRadius=150)

    # Sayaçlar ve Toplam Değer
    sayac_1tl = 0
    sayac_25kr = 0
    sayac_5kr = 0
    toplam_tl = 0.0

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            radius = i[2]
            center = (i[0], i[1])

            # 4. YARIÇAPA GÖRE PARALARI TANIMA VE DEĞERLENDİRME
            # (Bu değerleri kendi görselindeki piksel boyutuna göre ufakça ayarlayabilirsin)
            if radius > 110:  # 1 TL en büyük olandır
                etiket = "1 TL"
                renk = (0, 255, 0)  # Yeşil
                sayac_1tl += 1
                toplam_tl += 1.0
            elif radius > 85:  # 25 Kuruş orta boydur
                etiket = "25 Kurus"
                renk = (255, 0, 0)  # Mavi
                sayac_25kr += 1
                toplam_tl += 0.25
            else:  # 5 Kuruş en küçüğüdür
                etiket = "5 Kurus"
                renk = (0, 0, 255)  # Kırmızı
                sayac_5kr += 1
                toplam_tl += 0.05

            # Ekrana çizim yap
            cv2.circle(output, center, radius, renk, 3)
            cv2.circle(output, center, 2, (0, 255, 255), 3)  # Merkez noktası
            cv2.putText(output, etiket, (i[0] - 30, i[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # 5. SONUÇLARI YAZDIR (Ödev 2. Aşama)
        print("-" * 30)
        print(f"1 TL Sayısı: {sayac_1tl}")
        print(f"25 Kurus Sayısı: {sayac_25kr}")
        print(f"5 Kurus Sayısı: {sayac_5kr}")
        print(f"TOPLAM PARA DEGERI: {toplam_tl:.2f} TL")
        print("-" * 30)

        # Sonucu kaydet (Ödevin son maddesi) [cite: 89, 159]
        cv2.putText(output, f"Toplam: {toplam_tl:.2f} TL", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)
        cv2.imwrite('sonuc_goruntusu.jpg', output)

        cv2.imshow('Uygulama II - Para Sayma', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()