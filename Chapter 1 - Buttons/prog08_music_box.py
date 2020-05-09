from gpiozero import Button
from signal import pause
from subprocess import call
import time
import moc
# https://www.mankier.com/1/mocp
# play, stop, next, previous songs on button press

plst = Button(2)
next_song = Button(3)
previous_song = Button(17)

path = './Music'
press = 0

def start_playing():
    global path
    print('Starting the song')
    call(['mocp','-S'])
    #call(['mocp','-p', path])
    moc.find_and_play(path + '/*')

def stop_playing():
    print('Stopping the song')
    call(['mocp','-s'])

def play_next_song():
    print('Playing the next song')
    call(['mocp','--next'])

def play_previous_song():
    print('Playing the previous song')
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
