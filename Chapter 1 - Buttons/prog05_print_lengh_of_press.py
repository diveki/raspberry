from gpiozero import Button
from signal import pause
import time

button = Button(2)

press = 0
release = 0

def start():
	global press
	press = time.time()
    
def end():
	global release
	release = time.time()

button.when_pressed = start
button.when_released = end

while True:
    button.wait_for_press()
    button.wait_for_release()
    
    delay = release - press
    
    print(f'The button was pressed for {delay} seconds')
