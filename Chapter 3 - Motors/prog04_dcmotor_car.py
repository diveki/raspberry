from gpiozero import Motor, Button
import random
import time

motor_left = Motor(forward=7, backward = 8, enable=25)  #
motor_right = Motor(forward=9, backward = 10, enable=11)  # 

button_forward = Button(14)
button_backward = Button(15)
button_left = Button(18)
button_right = Button(23)

def move_forward(button, m1, m2):
    pass

def move_backward(button, m1, m2):
    pass

def move_left(button, m1, m2):
    pass

def move_right(button, m1, m2):
    pass


while True:
    pass
