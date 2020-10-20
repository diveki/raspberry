from gpiozero import Motor, Button
import random
import time

motor_left = Motor(forward=23, backward = 24, enable=25)  #
motor_right = Motor(forward=9, backward = 10, enable=11)  #

button_forward = Button(14)
button_backward = Button(15)
button_left = Button(18)
button_right = Button(21)


def move_forward(button, m1, m2, speed=0.7):
    m1.forward(speed=speed)
    m2.forward(speed=speed)

def move_backward(button, m1, m2, speed=0.7):
    m1.backward(speed=speed)
    m2.backward(speed=speed)

def move_left(button, mleft, mright, speed=0.6):
    mleft.backward(speed=speed)
    mright.forward(speed=speed)

def move_right(button, m1, m2, speed=0.6):
    mleft.forward(speed=speed)
    mright.backward(speed=speed)

def stop_motors(button, m1, m2):
    m1.stop()
    m2.stop()

button_forward.when_held = lambda : move_forward(button_forward, motor_left, motor_right)
button_forward.when_released = lambda : stop_motors(button_forward, motor_left, motor_right)

button_backward.when_held = lambda : move_backward(button_backward, motor_left, motor_right)
button_backward.when_released = lambda : stop_motors(button_backward, motor_left, motor_right)

button_left.when_held = lambda : move_left(button_left, motor_left, motor_right)
button_left.when_released = lambda : stop_motors(button_left, motor_left, motor_right)

button_right.when_held = lambda : move_right(button_right, motor_left, motor_right)
button_right.when_released = lambda : stop_motors(button_right, motor_left, motor_right)


while True:
    pass
