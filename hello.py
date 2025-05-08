import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt  # File controller.py

# Inisialisasi detektor tangan (maks 2 tangan)
detector = HandDetector(detectionCon=0.8, maxHands=2)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    hands, img = detector.findHands(frame)

    # Default: semua LED mati
    led_data = [0]*10
    led_data = [0,0,0,0,0,0,0,0,0,0]

    if hands:
        for hand in hands:
            fingerUp = detector.fingersUp(hand)
            jumlah_jari = fingerUp.count(1)

            # Cek tangan kanan atau kiri
            if hand["type"] == "Right":
                for i in range(jumlah_jari):
                    led_data[i] = 1  # LED 1-5
            elif hand["type"] == "Left":
                for i in range(jumlah_jari):
                    led_data[5 + i] = 1  # LED 6-10

        # Tampilkan total jari kedua tangan
        total_jari = led_data.count(1)
        cv2.putText(frame, f'Jari Anda: {total_jari}', (20, 460),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cnt.led(led_data)

    cv2.imshow("LED PROGRAM BY KELOMPOK 1", frame)

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
