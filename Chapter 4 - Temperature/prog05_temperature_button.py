from gpiozero import MCP3008, Button
import numpy as np
from scipy.interpolate import interp1d
import sys,time


mcp = MCP3008(channel=7)
button = Button(2)


def read_mapping(name):
	f = open(name, 'r')
	data = f.readlines()
	f.close()
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

def compare(tc, eps=0.01):
	if abs(tc[0]-tc[1]) < eps and abs(tc[0]-tc[2]) < eps and abs(tc[2]-tc[1]) < eps:
		t_mean = sum(tc)/len(tc)
		print(f'Your body temperature is: {t_mean:.2f} Celsius degree')
		sys.exit(0)

tc, resistance = read_mapping('ntcc.csv')		
t_body = []

print('Place your hand on the thermistor')
button.wait_for_press()


while True:
	time.sleep(0.8)
	rt = voltage2resistance(mcp.voltage, v_in=3.3, r=9.82e3)
	t_therm = interpolate_temperature(rt, tc, resistance)
	t_body.append(t_therm)
	#print(t_body)
	
	if len(t_body) < 3:
		continue
	else:
		compare(t_body, eps=0.01)
		t_body.pop(0)
		
# homework: add a criteria that stops the while cycle after 15 s, so that you do not wait forever for the result
		
	
