import pyaudio
import struct
import wave
import numpy as np
import threading
import matplotlib.pyplot as plt
from raspberry_functions import Recording
from scipy.signal import savgol_filter


rec = Recording()

rec.fix_recording(4)

fname = ['zsolt1.npy', 'zsolt2.npy', 'kriszta1.npy', 'kriszta2.npy', 'peti1.npy', 'peti2.npy', 'zsolt_nev.npy']

class Voice_Recognizer(Recording):
    def __init__(self)

tt = []
dd = []
for name in fname:
    with open(name, 'rb') as f:
        t1 = np.load(f)
        d1 = np.load(f)
        tt.append(t1)
        dd.append(d1)

window=1000
rate = 44100

dd_filtered = []
for sound in dd:
    filtered = np.convolve(np.abs(sound), np.ones(window), 'same')
    filtered = filtered/filtered.max()
    filtered[filtered<0.1] = 0
    filtered[filtered>0] = 1
    dd_filtered.append(filtered*sound)

ff = []
kk = []

for sound in dd_filtered:
    f = np.abs(np.fft.fftshift(np.fft.fft(sound)))
    f = savgol_filter(f, 101, 3)
    k = np.fft.fftshift(np.fft.fftfreq(len(sound)))*rate
    ff.append(f)
    kk.append(k)

np.corrcoef(ff)