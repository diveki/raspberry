from gpiozero import Servo, Button
import unidecode  # pip or conda install might be needed
import random
import time

question_words = ['hogy', 'hogyan', 'miként', 'hol', 'kinél', 'kitől', 'hol', 'honnan', 
                    'honnét', 'hová', 'hova', 'Meddig', 'Merre', 'Mettől', 'Minél',
                    'Mitől', 'Ki', 'Kié', 'Kiért', 'Kiig', 'Kihez', 'Kiként', 'Kinek',
                    'Kitől', 'Kivel', 'Mennyi', 'Hány', 'Mi', 'Mié', 'Miért', 'Miig',
                    'Mihez', 'Miként', 'Minek', 'Mitől', 'Mivel', 'Mikor', 'Hánykor',
                    'Hányig', 'Hánytól', 'Meddig', 'Mettől', 'Mikor', 'Mikortól', 
                    'Milyen']

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



while True:
    pass
