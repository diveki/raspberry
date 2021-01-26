# pip install adafruit-blinka
# pip install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2
# you need buster os system for this


import adafruit_dht
import time
from gpiozero import Motor

dev = adafruit_dht.DHT11(3)
motor = Motor(23,24,25)


def read_temp_hum(dev):
	try:
		t = dev.temperature
		hum = dev.humidity
	except:
		t = None
		hum = None
	return t, hum

def ventillation(m, temp, hum):
	if temp and hum:
		if temp > 30 or hum > 50:
			m.forward()
		else:
			m.stop()


while True:
	t, h = read_temp_hum(dev)
	print(f'Temp: {t} Celsius degree , Hum: {h} %')
	ventillation(motor, t,h)
	time.sleep(0.5)
	
