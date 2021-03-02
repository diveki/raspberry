from gpiozero import MCP3008, LED
import numpy as np
from scipy.interpolate import interp1d
from temperature_functions import read_temp_raw


mcp = MCP3008(channel=7)
red = LED(21)
yellow = LED(20)
green = LED(16)


def read_mapping(name):
	data = read_temp_raw(name)
	data.pop(0)
	tc = []
	r = []
	for line in data:
		clean_data = line.strip().split(',')
		tc.append(float(clean_data[0]))
		r.append(float(clean_data[1])*1000)
	return np.array(tc), np.array(r)
	
def voltage2resistance(v_out, v_in=3.3, r=9.82e3):
	return r * v_out / (v_in - v_out)

def interpolate_temperature(resistance, tc, r):
	f = interp1d(r,tc)
	return f(resistance)
	
def lightning(temp, leds=[green, yellow, red]):
	if temp < 23:
		for led in leds:
			led.off()
	elif temp < 28 and temp >= 23:
		leds[0].on()
		leds[1].off()
		leds[2].off()
	elif temp < 32 and temp >= 28:
		leds[0].on()
		leds[1].on()
		leds[2].off()
	elif temp >= 32:
		leds[0].on()
		leds[1].on()
		leds[2].on()


tc, resistance = read_mapping('ntcc.csv')

while True:
	rt = voltage2resistance(mcp.voltage, v_in=3.3, r=9.82e3)
	t_therm = interpolate_temperature(rt, tc, resistance)
	lightning(t_therm, leds=[green, yellow, red])
	print(t_therm)

