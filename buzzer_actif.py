from machine import Pin
import time

buzzer = Pin(12, mode=Pin.OUT)

while True:
    buzzer.on()
    time.sleep_ms(100)
    buzzer.off()
    time.sleep_ms(100)