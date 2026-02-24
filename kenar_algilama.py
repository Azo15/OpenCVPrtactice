import cv2

# Kamerayi baslat
cap = cv2.VideoCapture(0)

print("Kenar Algilama Aktif. Cikmak icin 'q' tusuna basin.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Adim: Goruntuyu Gri Seviyeye Cevir (Kenar algilama icin sarttir)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Adim: Gurultuyu azaltmak icin hafif bir Bulaniklastirma (Gaussian Blur) uygula
    # Bu adim, sahte kenarlari (parazitleri) engeller.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Adim: Canny Algoritmasi ile kenarlari bul
    # 100 ve 200 degerleri 'threshold' (esik) degerleridir. 
    # Bunlari degistirerek hassasiyeti ayarlayabilirsin.
    edges = cv2.Canny(blurred, 100, 200)

    # Hem orijinali hem de kenarlari goster
    cv2.imshow('Orijinal Kamera', frame)
    cv2.imshow('Kenar Algilama (Canny)', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()