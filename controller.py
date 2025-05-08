import pyfirmata

comport = 'COM9'  # Ganti jika bukan COM9
board = pyfirmata.Arduino(comport)

# LED 1–10: kanan = pin 8–12, kiri = pin 3–7
led_pins = [
    board.get_pin('d:8:o'),   # LED 1 (kanan)
    board.get_pin('d:9:o'),   # LED 2
    board.get_pin('d:10:o'),  # LED 3
    board.get_pin('d:11:o'),  # LED 4
    board.get_pin('d:12:o'),  # LED 5
    board.get_pin('d:7:o'),   # LED 6 (kiri)
    board.get_pin('d:6:o'),   # LED 7
    board.get_pin('d:5:o'),   # LED 8
    board.get_pin('d:4:o'),   # LED 9
    board.get_pin('d:3:o'),   # LED 10
]

def led(fingerUp):
    for i in range(10):
        led_pins[i].write(fingerUp[i])
