# https://realpython.com/python-speech-recognition/

from gpiozero.output_devices import RGBLED
import pyaudio
import sys
import wave
import numpy as np
import threading
import matplotlib.pyplot as plt
from raspberry_functions import Recording
import speech_recognition as sr

#rgbled = RGBLED(red=2, green=3, blue=7)
rgbled=1
instructions = ['switch the blue light on', 'turn the green light off', 'make dark', 'give me light', 'lights up', 'leds down', 'switch the red led off', 'turn the yellow diode on', 'turn the led up', 'make the white lights blink', 'blink the leds', 'turn the bulb up', 'switch the bulb off']
colour_defs = ['red', 'blue', 'green', 'yellow', 'white', 'black', 'orange', 'purple', 'pink', 'cyan', 'brown']
color_mapping = {
    'red': (1,0,0),
    'blue': (0,0,1),
    'green': (0,1,0),
    'yellow': (1,1,0),
    'white': (1,1,1),
    'black': (0.1,0.1,0.1),
    'orange': (1,165/255,0),
    'purple': (0.5,0,0.5),
    'pink': (1,192/255,203/255),
    'cyan': (0,1,1),
    'brown': (165/255,42/255,42/255),
}

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response
    

def find_color(text, color = colour_defs):
    words = text.split(' ')
    chosen_color = list(set(words) & set(color))
    return chosen_color[0]

def light_operation(text):
    words = text.split(' ')
    tmp = set(words) & set(['on', 'off', 'up', 'down'])
    if tmp == set():
        chosen_operation = []
    else:
        chosen_operation = list(tmp)[0]
    return chosen_operation

def light_action(chosen_color, chosen_operation, rgbled, RGBcode = color_mapping):
    if chosen_operation in ['on', 'up']:
        color = RGBcode[chosen_color]
        #rgbled.value = color
        print(f'{chosen_color} is {chosen_operation}')
    if chosen_operation in ['off', 'down']:
        # rgbled.value = (0,0,0)
        print('Light is off')


rec = sr.Recognizer()
mic = sr.Microphone()

while True:
    answer = input('Nyomj Entert a beszedhez; `q`-t a kilepeshez: ')
    if answer == 'q':
        sys.exit(0)
    else: 
        text_object = recognize_speech_from_mic(rec, mic)
        text = text_object['transcription']
        print(text)
        chosen_color = find_color(text, color = colour_defs)
        chosen_operation = light_operation(text)
        if chosen_color == [] or chosen_operation == []:
            print('Nem ertettem meg! Probald ujra!')
            continue
        else:
            light_action(chosen_color, chosen_operation, rgbled, RGBcode = color_mapping)
