import cv2
import numpy as np

drawing = False 
ix, iy = -1, -1

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # Cizim sirasinda gecici bir dikdortgen gosterimi istersen burasi kullanilir
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

# Siyah bir tuval olustur
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Cizim_Ekrani')
cv2.setMouseCallback('Cizim_Ekrani', draw_rectangle)

print("Fareyle basili tutup surukleyerek dikdortgenler cizin. Cikmak icin 'q'.")

while True:
    cv2.imshow('Cizim_Ekrani', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()