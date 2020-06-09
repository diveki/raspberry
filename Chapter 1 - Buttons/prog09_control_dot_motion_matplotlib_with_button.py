from gpiozero import Button
from signal import pause
import time, random
import numpy as np
import sys, pygame, pygame.freetype
# import RPi.GPIO as io

# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

right = Button(2)
up_down = Button(3)
left = Button(17)

pygame.init( )
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

#Set canvas parameters
size = width, height = 500, 500
white = 255,255,255
step = 50

#Display title on canvas
pygame.display.set_caption("Running Picur Hamster")

screen = pygame.display.set_mode(size)
ball = pygame.image.load("hamster.png")
ball = pygame.transform.scale(ball, (step,step))
ballrect = ball.get_rect()
ballrect.centerx = width/2
ballrect.centery = height/2

carrot = pygame.image.load("carrot.png")
carrot = pygame.transform.scale(carrot, (step,step))
carrect = carrot.get_rect()

x_ran = random.randint(0, width)
y_ran = random.randint(0, height)
x_ran = x_ran - (x_ran % step)
y_ran = y_ran - (y_ran % step)

carrect.centerx = x_ran
carrect.centery = y_ran


def move_up():
    global ballrect, step
    ballrect = ballrect.move([0,-step])

def move_down():
    global ballrect, step
    ballrect = ballrect.move([0,step])

def move_right():
    global ballrect, step
    ballrect = ballrect.move([step,0])

def move_left():
    global ballrect, step
    ballrect = ballrect.move([-step,0])

def start():
	global press
	press = time.time()

def end():
	global release
	release = time.time()
	delay = release - press
	func = encoder(delay)
	func()

def encoder(delay):
    if delay < 1:
        return move_up
    else:
        return move_down

up_down.when_pressed = start
up_down.when_released = end


while 1:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    if right.is_pressed:#If button is pressed, move beachball
        move_right()
    if left.is_pressed:
        move_left()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ballrect = ballrect.move([step,0])
        #     if event.key == pygame.K_LEFT:
        #         ballrect = ballrect.move([-step,0])
        #     if event.key == pygame.K_DOWN:
        #         ballrect = ballrect.move([0,step])
        #     if event.key == pygame.K_UP:
        #         ballrect = ballrect.move([0,-step])
        if ballrect.left < 0:
            ballrect.left = 0
        if ballrect.right > width: #Move beachball up
            ballrect.right = width
        if ballrect.top < 0:
            ballrect.top = 0
        if ballrect.bottom > height: #Move beachball down
            ballrect.bottom = height



    screen.fill(white)#Set background of canvas
    if ballrect.centerx == carrect.centerx and ballrect.centery == carrect.centery:
        text_surface = font.render("Hm, Yummy!", True, (255, 0, 0))
        screen.blit(text_surface, (width/2-30, height/2))
    screen.blit(carrot, carrect)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.1)#Wait for 100ms before next button press
