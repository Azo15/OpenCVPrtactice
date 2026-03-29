import cv2
import mediapipe as mp
import serial
import time

# En temel başlatma yöntemi
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Arduino Bağlantısı (Aygıt Yöneticisindeki COM6 portun için)
try:
    arduino = serial.Serial('COM6', 9600, timeout=1)
    time.sleep(2)
    print("Arduino Bağlantısı Başarılı!")
except Exception as e:
    print(f"Bağlantı Hatası: {e}")
    arduino = None

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    # Görüntüyü RGB'ye çevirip işle
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Göz kapaklarını temsil eden noktalar arasındaki farkı ölç
            # Üst nokta: 159, Alt nokta: 145
            eye_diff = face_landmarks.landmark[145].y - face_landmarks.landmark[159].y

            # Göz kapalıysa (Eşik değerini 0.01 yaptım)
            if eye_diff < 0.01:
                print("YORGUNLUK TESPİT EDİLDİ!")
                if arduino: arduino.write(b'1')
            else:
                if arduino: arduino.write(b'0')

    cv2.imshow('Yorgunluk Takibi', image)
    if cv2.waitKey(5) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()
if arduino: arduino.close()