from gpiozero import Button
from signal import pause
from subprocess import call
import time
# play, stop, next, previous songs on button press

plst = Button(2)
next_song = Button(3)
previous_song = Button(4)

path = './Music'
press = 0

def start_playing():
    global path
    call(['mocp','-p', path])

def stop_playing():
    call(['mocp','-s'])

def play_next_song():
    call(['mocp','--next'])

def play_previous_song():
    call(['mocp','--previous'])

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
        return start_playing
    else:
        return stop_playing

plst.when_pressed = start
plst.when_released = end

next_song.when_pressed = play_next_song
previous_song.when_pressed = play_previous_song

while True:
    pass