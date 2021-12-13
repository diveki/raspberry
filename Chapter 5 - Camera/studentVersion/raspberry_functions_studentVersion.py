#### Chapter 4 - Temperature functions
from time import sleep 
import numpy as np

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
    # zold kikapcs
    # sarga bekapcs
    sleep(1)
    # sarga kikapcs
    # piros bekapcs
    sleep(dt)
    # sarga bekapcs
    sleep(1)
    #zold bekapcs
    #sarga kikapcs 
    # piros kikapcs	

def prepare_data(date, value, dplot, tplot, maxlen=20):
	# add a date elemet a dplot listahoz
	# add a value elemet a tplot listahoz
	if ........:  # nezd meg, hogy a dplot lista hossza nagyobb-e a maxlen valtozo ertekenel, ha igen
		# torold ki a dplot elso (0ik) elemet
		# torold ki a tplot elso (0ik) elemet
	return dplot, tplot

def frame2grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


