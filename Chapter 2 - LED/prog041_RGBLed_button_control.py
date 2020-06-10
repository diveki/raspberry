from gpiozero import RGBLED, Button
from time import sleep


led = RGBLED(red=9, green=10, blue=11)

button1 = Button(2)
button2 = Button(3)
button3 = Button(17)


def red():
    led.color(1,0,0)

def magenta():
    led.color(1,0,1)

def cyan():
    led.color(0,1,1)

button1.when_pressed = red
button2.when_pressed = magenta
button3.when_pressed = cyan

while True:
    pass