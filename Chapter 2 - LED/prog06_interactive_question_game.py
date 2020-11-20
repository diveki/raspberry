from gpiozero import Button, LED
from time import sleep
import random

blue = LED(9)
red = LED(10)

yes = Button(2)
no  = Button(3)

qa = {
    'Törökország': 'Ankara',
    'Albánia'    : 'Tirana',
    'Argentína'  : 'Buenos Aires',
    'Ausztria'   : 'Bécs',
    'Görögország': 'Athén',
    'Szerbia'    : 'Belgrád',
    'Németország': 'Berlin',
    'Ausztrália' : 'Canberra',
    'Írország'   : 'Dublin',
    'Norvégia'   : 'Oslo',
}

press = False
right_answer = 0

def question(country):
    txt = f'Mi {country} fővárosa?'
    return txt

def options(city, opt):
    global right_answer
    a = [random.choice(opt)]
    a.append(city)
    random.shuffle(a)
    txt = f'1) {a[0]}      2) {a[1]}'
    right_answer = a.index(city) + 1
    return txt

def pressed(button, pos = 0):
    global press, right_answer
    if pos == right_answer:
        blue.on()
        sleep(3)
        blue.off()
    else:
        red.on()
        sleep(3)
        red.off()
    press = False

yes.when_pressed = pressed(yes, pos = 1)
no.when_pressed  = pressed(no, pos = 2)

while True:
    if not press:
        press = True
        country = random.choice(list(qa.keys()))
        city    = qa[country]
        wrong_answers = list(qa.values())
        wrong_answers.remove(city)
        print(question(country))
        print('='*10)
        print(options(city, wrong_answers))
        print('='*10)
