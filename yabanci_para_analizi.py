import cv2
import numpy as np
import os

klasor = os.path.dirname(os.path.abspath(__file__))
dosya_adi = 'euro_coins.jpg'
yol = os.path.join(klasor, dosya_adi)

img = cv2.imread(yol)

if img is None:
    print(f"\n[HATA]: {dosya_adi} bulunamadı!")
else:
    # Pencere ayarı
    cv2.namedWindow('Final Analiz', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Final Analiz', 1000, 600)

    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    gray = cv2.medianBlur(gray, 11)

    # minDist=350: Sahte daire oluşmasını engellemeye devam eder
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=350,
                               param1=100, param2=45, minRadius=100, maxRadius=300)

    toplam_euro = 0.0

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            x, y, r = i[0], i[1], i[2]

            # --- FİNAL HASSAS AYAR (2 Euro vs 1 Euro) ---
            # r=225 sınırı sayesinde 2 Euro ve 1 Euro artık asla karışmayacak
            if r >= 225:
                deger, renk = 2.00, (0, 255, 0)  # 2 Euro (Yeşil)
            elif r >= 190:
                deger, renk = 1.00, (255, 0, 0)  # 1 Euro (Mavi)
            elif r >= 160:
                deger, renk = 0.10, (255, 255, 0)  # 10 Cent (Turkuaz)
            else:
                deger, renk = 0.02, (0, 0, 255)  # 2 Cent (Kırmızı)

            toplam_euro += deger
            cv2.circle(output, (x, y), r, renk, 6)
            cv2.putText(output, f"{deger:.2f}", (x - 70, y + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 4)

        # Final Toplam (Sol Üst)
        cv2.putText(output, f"Final Toplam: {toplam_euro:.2f} EUR", (50, 120),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 0), 7)

        print(f"\nİşlem Başarıyla Tamamlandı! Toplam: {toplam_euro:.2f} EUR")

        cv2.imshow('Final Analiz', output)
        cv2.imwrite('odev_final_euro_kusursuz.jpg', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()