# In the Settings tab, change the Application type to Read, Write and Access direct messages
# In the Reset keys tab, press the Reset button, update the consumer key and secret in your application accordingly.

import cv2, time
import numpy as np
import datetime as dt
import json, tweepy
from gpiozero import Button
from random import choice

# inicializald a kamerat
cap = 
# inicializald a nyomogombot
button = 

# ird be a kep lokaciojat es nevet a ... helyere
with open(...) as f:
    details = json.load(f)

auth = tweepy.OAuthHandler(details['consumer_key'], details['consumer_secret'])
auth.set_access_token(details['access_token'], details['access_token_secret'])

api = tweepy.API(auth)


design = [(cv2.edgePreservingFilter, {'flags':1, 'sigma_s':60, 'sigma_r':0.4}, 'My eyes are hazy'),
          (cv2.detailEnhance,        {'sigma_s':10, 'sigma_r':0.15},           'I am so sharp'),
          (cv2.stylization,          {'sigma_s':60, 'sigma_r':0.07},           'I got some style :)'),
]

def snapshot():
    # rogzits egy kepet
    ret, frame = 
    func, kwargs, text = choice(design)
    frame = func(frame, **kwargs)
    # mentsd el a kepet a 'twitter/image.png' helyre
    cv2.imwrite(...)
    return text

def send_tweet(text, obj):
    obj.update_with_media('twitter/image.png', text)

def action():
    # hivd meg a snapshot fuggvenyt hogy keszitsen kepet es kivalassza a hozzaillo textet
    text = 
    # hivd meg a send_tweet fuggvenyt hogy posztolj a twitteren
    se
    print('Tweet has been sent!')

# rendeld hozza a megfelelo muveletet a nyomogombhoz
button.when_pressed = 

while True:
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

