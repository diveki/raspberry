from gpiozero import RGBLED
from time import sleep

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

def set_color(color, cm = colors_dict):
    col = colors_dict.get(color, None)
    return col

while True:
    answer = input('What color do you want to see? ')
    color = set_color(answer)
    if color:
        led.color = color
    else:
        continue
