#### Chapter 4 - Temperature functions
from time import sleep 

def read_temp_raw(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(file_name):
    lines = read_temp_raw(file_name)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(file_name)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def get_temp(dev):
	try:
		t = dev.temperature
	except:
		t = 0
	return t

def get_hum(dev):
	try:
		hum = dev.humidity
	except:
		hum = 0
	return hum

def ventillation(m, temp, hum):
	if temp and hum:
		if temp > 30 or hum > 50:
			m.forward()
		else:
			m.stop()


# Chapter 5 - Camera functions
import cv2

def traffic_light_sequence(red, amber, green, dt = 3):
    sleep(dt)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(dt)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()	

def prepare_data(date, value, dplot, tplot, maxlen=20):
	dplot.append(date)
	tplot.append(value)
	if len(dplot) > maxlen:
		dplot.pop(0)
		tplot.pop(0)
	return dplot, tplot

def frame2grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# Chapter 6 - IR functions
from scipy.interpolate import interp1d
import numpy as np
import threading
import time
import datetime as dt
import matplotlib.pyplot as plt

def read_2column_files(name, header=True):
    lines = read_temp_raw(name)
    if header:
        lines.pop(0)
    distance = []
    voltage = []
    for line in lines:
        if line.strip() != '':
            data = line.strip().split(',')
            voltage.append(float(data[0]))
            distance.append(float(data[1]))
    return np.array(voltage), np.array(distance)

def interpolate1d(x, y, target):
	f = interp1d(x,y)
	return f(target)


class ActiveSensor:
	def __init__(self, led, mcp, calibname, sampling_rate=1):
		self.led = led
		self.mcp = mcp
		self.calibfile = calibname
		self.sampling_rate = sampling_rate
		self.plot_length = 20
		self.initialize_calibration(self.calibfile)
		self.event = threading.Event()
		self.event_plot = threading.Event()
		self.dlist = []
		self.ylist = []
		
	def start(self):
		self.event.clear()
		self.led.on()
		t = threading.Thread(target=self.start_measurement)
		t.start()

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			dd = dt.datetime.now()
			self.current_voltage = self.mcp.voltage
			self.current_distance = interpolate1d(self.calib_volt, self.calib_distance, self.current_voltage)
			print(f'Current distance from object is: {self.current_distance:.2} cm')
			self.prepare_data(dd, self.current_distance)
			time.sleep(self.sampling_rate)
		
	def stop(self):
		self.event.set()
		self.led.off()
		print('Measurement is stopped')

	def initialize_calibration(self, filename):
		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)

	def prepare_data(self, dd, yy):
		self.dlist, self.ylist = prepare_data(dd, yy, self.dlist, self.ylist, maxlen=self.plot_length)

	def plot_initialize(self):
		plt.ion()
		self.figure, self.ax = plt.subplots(figsize=(8,6))
		self.line1, = self.ax.plot(self.dlist, self.ylist, 'o-')
		plt.title("Dynamic Plot of measurement",fontsize=25)
		plt.xlabel("Time",fontsize=18)
		plt.ylabel("Distance (cm)",fontsize=18)
		plt.grid(True)

	def start_plot(self):
		self.event_plot.clear()
		t = threading.Thread(target=self.plot_distance_thread)
		t.start()

	def stop_plot(self):
		self.event_plot.set()
		print('Measurement is stopped')

	def plot_distance_thread(self):
		while not self.event_plot.is_set():
			self.line1.set_xdata(self.dlist)
			self.line1.set_ydata(self.ylist)
			self.ax.set_ylim(min(self.ylist)*0.99, max(self.ylist)*1.01) # +1 to avoid singular transformation warning
			self.ax.set_xlim(min(self.dlist), max(self.dlist))
			self.figure.canvas.draw()
			self.figure.canvas.flush_events()
			plt.gcf().autofmt_xdate()
			time.sleep(2)


# Chapter 7 - Sound functions
import pyaudio
import struct
import wave

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


def voice2signal(voice, window=500, normalize=2**15, limit=0.1):
    filtered = np.convolve(np.abs(voice), np.ones(window), 'same')
    filtered = filtered/(normalize*window)
    filtered[filtered<limit] = 0
    filtered[filtered>0] = 1
    return filtered
