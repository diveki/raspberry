import pyaudio
import struct
import wave
import numpy as np
import threading
import matplotlib.pyplot as plt
from raspberry_functions import Recording, voice2signal
from scipy.signal import savgol_filter
import sys


fname = [('zsolt','zsolt1.npy'), ('zsolt','zsolt2.npy'), 
         ('kriszta', 'kriszta1.npy'), ('kriszta', 'kriszta2.npy'), 
         ('peti', 'peti1.npy'), ('peti', 'peti2.npy'), ('zsolt','zsolt_nev.npy')]
device_index = 1


sounds = {}
for key, name in fname:
    with open(name, 'rb') as f:
        t1 = np.load(f)
        d1 = np.load(f)
        filt = voice2signal(d1, window=1000, normalize=2**15, limit=0.06)
        d_filter = filt * d1
        spectrum = np.abs(np.fft.fftshift(np.fft.fft(d_filter)))
        freq = np.fft.fftshift(np.fft.fftfreq(len(d_filter)))*44100
        if key in sounds.keys():
            sounds[key]['t'].append(t1)
            sounds[key]['data'].append(d1)
            sounds[key]['spectrum'].append(spectrum)
            sounds[key]['frequency'].append(freq)
        else:
            sounds[key] = {'t': [t1], 'data': [d1], 'spectrum': [spectrum], 'frequency': [freq]}


class Voice_Recognizer(Recording):
    def __init__(self, device_index=1, records={}):
        super().__init__(device_index=device_index)
        self.names = list(records.keys())
        self.records = records
        self.window = 1000
        self.limit = 0.06

    def process_voice(self):
        filtered = voice2signal(self.data, window=self.window, normalize=2**15, limit=self.limit)
        data_filtered = self.data * filtered
        self.spectrum = np.abs(np.fft.fftshift(np.fft.fft(data_filtered)))
        self.frequency = np.fft.fftshift(np.fft.fftfreq(len(data_filtered)))*self.rate

    def get_coefs(self):
        self.coef = {}
        for name in self.names:
            reference = self.records[name]['spectrum']
            result = 0
            for spec in reference:
                result = result + np.min(np.corrcoef(spec, self.spectrum))
            self.coef[name] = result/len(reference)


rec = Voice_Recognizer(device_index=device_index, records=sounds)

while True:
    answer = input('Nyomd le az Entert vagy a q-t: ')
    if answer == 'q':
        sys.exit(0)
    else:
        print('Felvetel indul')
        rec.fix_recording(4)
        rec.process_voice()
        rec.get_coefs()
        print(rec.coef)

