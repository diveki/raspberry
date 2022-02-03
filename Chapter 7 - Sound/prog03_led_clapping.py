import numpy as np
import matplotlib.pyplot as plt
from raspberry_functions import Recording
from gpiozero import LED
import time

device_index = 1
led = LED(2)
rec = Recording(device_index=device_index)


def voice2signal(voice, window=500, normalize=2**15, limit=0.1):
    filtered = np.convolve(np.abs(voice), np.ones(window), 'same')
    filtered = filtered/(normalize*window)
    filtered[filtered<limit] = 0
    filtered[filtered>0] = 1
    return filtered

def led_control(light, value, limit=100):
    if value > limit:
        if light.is_lit:
            light.off()
            print('LED off')
        else:
            light.on()
            print('LED on')


while True:
    rec.fix_recording(2)
    signal = voice2signal(rec.data, window=1000, limit=0.06)
    value = np.sum(signal)
    print(value)
    led_control(led, value, limit=100)
    time.sleep(0.1)

