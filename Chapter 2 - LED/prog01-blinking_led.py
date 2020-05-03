from gpiozero import LED
from time import sleep

led = LED(25)

ii = 0

while ii < 10:
    print(ii, end=' ')
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    ii = ii + 1
