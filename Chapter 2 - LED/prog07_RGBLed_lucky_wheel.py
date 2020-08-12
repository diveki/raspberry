from gpiozero import RGBLED, Button
import time

button = Button(2)
led = RGBLED(red=9, green=10, blue=11)

colors_dict = {'red': (1,0,0),
          'green': (0,1,0),
          'blue': (0,0,1),
          'white': (1,1,1),
          'black': (0,0,0),
          'yellow': (1,1,0),
          'cyan': (0,1,1),
          'magenta': (1,0,1),
          'silver': (192/255,192/255,192/255),
          'gray': (128/255,128/255,128/255),
          'deep pink': (255/255,20/255,147/255),
}

select = ''
wait = 1
target = 'red'

# def set_color(color, cm = colors_dict):
#     col = cm.get(color, None)
#     return col

def pressed():
    global select, target
    if select == target:
        print('You have won!')
    else:
        print('You lost!')

button.when_pressed = pressed

while True:
    for key, value in colors_dict.items():
        select = key
        led.color = value
        time.sleep(wait)
