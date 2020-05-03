from gpiozero import Button
from signal import pause
import os

button = Button(2)

browser = ['google-chrome', 'firefox', 'chromium-browser']

while True:
    button.wait_for_press()
    os.system(f'{browser[0]} www.facebook.com')  # this assumes you have google-chrome installed
