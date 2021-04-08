# pip install pygame==1.9.4
from gpiozero import Motor, Button
import numpy as np
import sys, pygame, pygame.freetype
import time
import cv2

# motor_left = Motor(forward=23, backward = 24, enable=25)  #
# motor_right = Motor(forward=27, backward = 22, enable=17)  #
cap = cv2.VideoCapture(0)

pygame.init( )

# button_forward = Button(14)
# button_backward = Button(15)
# button_left = Button(18)
# button_right = Button(21)

#Set canvas parameters
size = 500, 500

#Display size
screen = pygame.display.set_mode(size)

def move_forward(m1, m2, speed=0.8):
    m1.forward(speed=speed)
    m2.forward(speed=speed)

def move_backward(m1, m2, speed=0.8):
    m1.backward(speed=speed)
    m2.backward(speed=speed)

def move_left(mleft, mright, speed=0.8):
    mleft.backward(speed=speed)
    #mright.forward(speed=speed)

def move_right(mleft, mright, speed=0.8):
    #mleft.forward(speed=speed)
    mright.backward(speed=speed)

def stop_motors(m1, m2):
    m1.stop()
    m2.stop()

# button_forward.when_held = lambda : move_forward(button_forward, motor_left, motor_right)
# button_forward.when_released = lambda : stop_motors(button_forward, motor_left, motor_right)
#
# button_backward.when_held = lambda : move_backward(button_backward, motor_left, motor_right)
# button_backward.when_released = lambda : stop_motors(button_backward, motor_left, motor_right)
#
# button_left.when_held = lambda : move_left(button_left, motor_left, motor_right)
# button_left.when_released = lambda : stop_motors(button_left, motor_left, motor_right)
#
# button_right.when_held = lambda : move_right(button_right, motor_left, motor_right)
# button_right.when_released = lambda : stop_motors(button_right, motor_left, motor_right)


while 1:
    ret, frame = cap.read()
    frame = np.rot90(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame=pygame.surfarray.make_surface(frame)
    screen.blit(frame,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('Move right...')
                # move_right(motor_left, motor_right, speed=1)
            if event.key == pygame.K_LEFT:
                print('Move left...')
                # move_left(motor_left, motor_right, speed=1)
            if event.key == pygame.K_DOWN:
                print('Move backward...')
                # move_backward(motor_left, motor_right, speed=1)
            if event.key == pygame.K_UP:
                print('Move forward...')
                # move_forward(motor_left, motor_right, speed=1)

        if event.type == pygame.KEYUP:
            print('Stop motors...')
            # stop_motors(motor_left, motor_right)

    time.sleep(0.1)#Wait for 100ms before next button press
