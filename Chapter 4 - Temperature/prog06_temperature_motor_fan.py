# pip install adafruit-blinka
# pip install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2
# you need buster os system for this


import adafruit_dht
import time
from gpiozero import Motor
from temperature_functions import get_hum, get_temp, ventillation

dev = adafruit_dht.DHT11(3)
motor = Motor(23,24,25)

while True:
	t = get_temp(dev)
	h = get_hum(dev)
	print(f'Temp: {t} Celsius degree , Hum: {h} %')
	ventillation(motor, t,h)
	time.sleep(0.5)
	

