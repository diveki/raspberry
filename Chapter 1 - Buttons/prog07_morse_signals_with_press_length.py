from gpiozero import Button
from signal import pause
import time

button = Button(2)

press = 0
release = 0

# open file for the secret message
msg = open('message.txt','w')

code_map = {'trambulin':'lsls',
            'szia':'l',
            'gyere':'ll',
            'mizu':'sl',
            'siess':'sss',
}

def start():
	global press
	press = time.time()

def end():
	global release, msg
	release = time.time()
	delay = release - press
	code = encoder(delay)
	if code == 'close':
		msg.close()
		print('Encripted message saved')
		print('Please exit the program!')
	if not msg.closed:
		msg.write(code)

def encoder(delay):
    if delay >= 1 and delay < 3:
        return 'l'
    elif delay < 1:
        return 's'
    elif delay >= 3 and delay < 7:
        return '\n'
    else:
        return 'close'


button.when_pressed = start
button.when_released = end

while True:
    pass
