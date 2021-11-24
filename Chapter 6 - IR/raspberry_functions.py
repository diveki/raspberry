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
