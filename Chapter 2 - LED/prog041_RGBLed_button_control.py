from gpiozero import RGBLED, Button
from time import sleep


led = RGBLED(red=10, green=9, blue=11)

button1 = Button(2)
button2 = Button(3)
button3 = Button(17)


def red():
    led.color = (0.5,0,0)

def magenta():
    led.color = (0.5,0,0.5)

def cyan():
    led.color = (0,0.5,0.5)

button1.when_pressed = red
button2.when_pressed = magenta
button3.when_pressed = cyan

while True:
    pass
