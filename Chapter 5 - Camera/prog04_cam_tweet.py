import cv2, time
import numpy as np
import datetime as dt
import json, tweepy
from gpiozero import Button
from random import choice

cap = cv2.VideoCapture(0)
button = Button(2)

with open('twitter.json') as f:
    details = json.open(f)

auth = tweepy.OAuthHandler(details['consumer_key'], details['consumer_secret'])
auth.set_access_token(details['access_token'], details['access_token_secret'])

api = tweepy.API(auth)

design = [(cv2.edgePreservingFilter, {'flags':1, 'sigma_s':60, 'sigma_r':0.4}, 'My eyes are hazy'),
          (cv2.detailEnhance,        {'sigma_s':10, 'sigma_r':0.15},           'I am so sharp'),
          (cv2.stylization,          {'sigma_s':60, 'sigma_r':0.07},           'I got some style :)'),
]

def snapshot():
    ret, frame = cap.read()
    func, kwargs, text = choice(design)
    frame = func(frame, **kwargs)
    cv2.imwrite('twitter/image.png', frame)
    return text

def send_tweet(text):
    twitter.update_with_media('twitter/image.png', text)

def action():
    text = snapshot()
    send_tweet(text)
    print('Tweet has been sent!')

button.when_pressed = action

while True:
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

