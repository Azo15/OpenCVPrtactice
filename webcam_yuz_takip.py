import cv2
import os

# 1. XML dosyasının tam yolunu otomatik belirle
# Bu yöntem, dosya aynı klasörde olduğu sürece hata almanı engeller.
current_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(current_dir, 'haarcascade_frontalface_default.xml')

# 2. Yüz algılayıcısını yükle
face_cascade = cv2.CascadeClassifier(xml_path)

# Kontrol: XML dosyası yüklendi mi?
if face_cascade.empty():
    print(f"Hata: XML dosyasi bulunamadi! Lutfen su adreste oldugundan emin olun: {xml_path}")
    exit()

# 3. Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera acilamadi!")
    exit()

print("Kamera baslatildi. Yuz algilama aktif.")
print("Cikmak icin 'q' tusuna basin.")

while True:
    # Kameradan görüntü oku
    ret, frame = cap.read()
    
    if not ret:
        print("Hata: Goruntu alinamiyor.")
        break

    # Performans için gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Algılanan her yüz için kare çiz
    for (x, y, w, h) in faces:
        # Yeşil kare (BGR: 0, 255, 0)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Yuz Algilandi', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow('OpenCV Yuz Takip Testi', frame)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
print("Program kapatildi.")