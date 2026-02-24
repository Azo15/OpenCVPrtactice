import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Tiklanan yerdeki BGR degerlerini al
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        
        print(f"Koordinat: ({x}, {y}) -> B:{blue}, G:{green}, R:{red}")
        
        # Ekrana yazdir
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = f"{blue},{green},{red}"
        cv2.putText(img, strBGR, (x, y), font, 0.5, (255, 255, 255), 2)
        cv2.imshow('Renk_Secici', img)

# 512x512 mavi-yesil karisimi bir test ekrani olustur
img = np.zeros((512, 512, 3), np.uint8)
img[:] = [100, 200, 50] # Arkaplan rengi

cv2.imshow('Renk_Secici', img)
cv2.setMouseCallback('Renk_Secici', click_event)

print("Ekranda bir yere tiklayin. Cikmak icin bir tusa basin.")
cv2.waitKey(0)
cv2.destroyAllWindows()