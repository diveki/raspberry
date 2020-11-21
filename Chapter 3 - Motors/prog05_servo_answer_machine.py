from gpiozero import Servo, AngularServo, Button
import unidecode  # pip or conda install might be needed
import sys, random
import time

# determine the angle range for the servo
# motor = Servo(18)
# motor.min()  # measure angle
# motor.max()  # measure angle again

angle_min = -90
angle_max = 90

motor = AngularServo(18, min_angle = angle_min, max_angle=angle_max)
button_quit = Button(22)

motor.angle = None
yes_angle = -45
no_angle = 45
maybe_angle = 0
angle_list = [yes_angle, no_angle, maybe_angle]


question_words = ['hogy', 'hogyan', 'miként', 'hol', 'kinél', 'kitől', 'hol', 'honnan', 
                    'honnét', 'hová', 'hova', 'Meddig', 'Merre', 'Mettől', 'Minél',
                    'Mitől', 'Ki', 'Kié', 'Kiért', 'Kiig', 'Kihez', 'Kiként', 'Kinek',
                    'Kitől', 'Kivel', 'Mennyi', 'Hány', 'Mi', 'Mié', 'Miért', 'Miig',
                    'Mihez', 'Miként', 'Minek', 'Mitől', 'Mivel', 'Mikor', 'Hánykor',
                    'Hányig', 'Hánytól', 'Meddig', 'Mettől', 'Mikor', 'Mikortól', 
                    'Milyen']


def exit_program():
    sys.exit(0)

# check if the question contains any of the above words
def check_for_words(txt, word_list = question_words):
    txt = txt.lower()
    txt = unidecode.unidecode(txt)
    txt = txt.replace('?','')
    txt_list = txt.split(' ')

    for word in word_list:
        wl = unidecode.unidecode(word.lower())
        if wl in txt_list:
            return True
    return False

def answer_the_question(motor, angle_list):
    answer = random.choice(angle_list)
    print(answer)
    motor.angle = answer
    time.sleep(1)
    motor.angle = None


button_quit.when_pressed = exit_program

while True:
    txt = input('Mire vagy kíváncsi halandó?\n\t')
    proper = check_for_words(txt)
    if proper:
        print('*'*10)
        print('Olyan kérdést tegyél fel, amire igennel, nemmel vagy talánnal tudok válaszolni!')
        print('*'*10 + '\n')
        continue
    answer_the_question(motor, angle_list)
    
