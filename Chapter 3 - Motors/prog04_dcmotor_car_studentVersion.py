from gpiozero import Motor
import sys, pygame
import time

motor_left = Motor(forward=23, backward = 24, enable=25)  #
motor_right = Motor(forward=27, backward = 22, enable=17)  #

pygame.init( )

#Set canvas parameters
size = 500, 500

#Display size
screen = pygame.display.set_mode(size)

# put the functions here
def move_forward(m1, m2, speed=0.8):
    pass

############

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass        # replace it with code that exits the program
        if event.type == pygame.KEYDOWN:
### write here the code that checks which button was pressed
            if event.key == pygame.K_RIGHT:
                pass

        if event.type == pygame.KEYUP:
            pass

    time.sleep(0.1)#Wait for 100ms before next button press
