from gpiozero import Button
from signal import pause

button = Button(2)

press = 0
release = 0

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
    code = encoder(delay, msg)

def encoder(delay, msg):
    if delay >= 1 and delay < 4:
        return 'l'
    elif delay < 1:
        return 's'
    elif delay >= 4 and delay < 7:
        msg.write('\n')
    else:
        msg.close()
        print('Encripted message saved')


button.when_pressed = start
button.when_released = end

while True:
    button.wait_for_press()
    button.wait_for_release()
