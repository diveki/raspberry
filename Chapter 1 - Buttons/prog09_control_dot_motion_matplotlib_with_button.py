from gpiozero import Button
from signal import pause
import time
import numpy as np
import sys, pygame
# import RPi.GPIO as io

# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

# right = Button(2)
# up_down = Button(3)
# left = Button(17)

pygame.init( )

#Set canvas parameters
size = width, height = 500, 500
speed = [100, 100]
white = 255,255,255

#Display title on canvas
pygame.display.set_caption("Running Picur Hamster")

screen = pygame.display.set_mode(size)
ball = pygame.image.load("hamster.png")
ball = pygame.transform.scale(ball, (50,50))
ballrect = ball.get_rect()

ballrect.centerx = width/2
ballrect.centery = height/2


# def start_playing():
#     global path
#     print('Starting the song')
#     call(['mocp','-S'])
#     #call(['mocp','-p', path])
#     moc.find_and_play(path + '/*')
#
# def stop_playing():
#     print('Stopping the song')
#     call(['mocp','-s'])
#
# def play_next_song():
#     print('Playing the next song')
#     call(['mocp','--next'])
#
# def play_previous_song():
#     print('Playing the previous song')
#     call(['mocp','--previous'])
#
# def start():
# 	global press
# 	press = time.time()
#
# def end():
# 	global release
# 	release = time.time()
# 	delay = release - press
# 	func = encoder(delay)
# 	func()
#
# def encoder(delay):
#     if delay < 1:
#         return start_playing
#     else:
#         return stop_playing
#
# plst.when_pressed = start
# plst.when_released = end
#
# next_song.when_pressed = play_next_song
# previous_song.when_pressed = play_previous_song


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if right.is_pressed:#If button is pressed, move beachball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ballrect = ballrect.move([50,0])
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move([-50,0])
            if event.key == pygame.K_DOWN:
                ballrect = ballrect.move([0,50])
            if event.key == pygame.K_UP:
                ballrect = ballrect.move([0,-50])
        if ballrect.left < 0:
            ballrect.left = 0
        if ballrect.right > width: #Move beachball up
            ballrect.right = width
        if ballrect.top < 0:
            ballrect.top = 0
        if ballrect.bottom > height: #Move beachball down
            ballrect.bottom = height

    screen.fill(white)#Set background of canvas
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.1)#Wait for 100ms before next button press
