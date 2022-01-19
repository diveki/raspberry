import pyaudio
import struct
import wave
import numpy as np
import threading
import matplotlib.pyplot as plt


class Recording():
    def __init__(self, device_index=1, rate=44100, channels=1, format=pyaudio.paInt16, frames_per_buffer=2**10):
        self.device_index = device_index
        self.rate = rate
        self.channels = channels
        self.format = format
        self.frames_per_buffer = frames_per_buffer
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=self.format, channels=self.channels, input_device_index=self.device_index, rate=self.rate, input=True, frames_per_buffer=self.frames_per_buffer)
        self.event = threading.Event()

    def fix_recording(self, duration=1):
        self.data = np.array([])
        for i in range(0, round(self.rate*duration / self.frames_per_buffer)):
            frame = self.stream.read(self.frames_per_buffer)
            new_data = np.frombuffer(frame, dtype=np.int16)
            self.data = np.append(self.data, new_data)
        self.time = np.arange(0,len(self.data))/self.rate

    def continuous_recording(self):
        self.event.clear()
        print('Start recording')
        t = threading.Thread(target=self._start)
        t.start()

    def _start(self):
        self.data = np.array([])
        while not self.event.is_set():
            frame = self.stream.read(self.frames_per_buffer)
            new_data = np.frombuffer(frame, dtype=np.int16)
            self.data = np.append(self.data, new_data)

    def stop_recording(self):
        self.time = np.arange(0,len(self.data))/self.rate
        self.event.set()
        print('Recording stopped')

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
