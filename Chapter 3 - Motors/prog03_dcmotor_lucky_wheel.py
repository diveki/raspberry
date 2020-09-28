from gpiozero import Motor, Button
import random
import time

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
button_start = Button(17)


def start(button, m):
    t_rot = random.uniform(0, 5)
    speed = random.uniform(0.6, 1)
    m.forward(speed=speed)
    time.sleep(t_rot)
    m.stop()


button_start.when_pressed = start(button_start, motor)


while True:
    pass
