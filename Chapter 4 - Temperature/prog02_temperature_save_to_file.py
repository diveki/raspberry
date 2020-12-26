
import os
import glob
import time
import datetime as dt
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

filename = 'test.csv'
duration = 10  # given in seconds
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def write2file(txt,filename='temperature.csv'):
	f = open(filename, 'a')
	f.write(txt)
	f.close()
	
def prepare2save(tc,tf):
	now = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	txt = now + ',' + str(round(tc,2)) + ',' + str(round(tf,2)) + '\n'
	return txt
	
t0 = time.time()
t1 = time.time()

while t1 - t0 < duration:
	tc, tf = read_temp()
	t1 = time.time()
	print(t1-t0)
	text = prepare2save(tc, tf)
	write2file(text, filename=filename)
	time.sleep(1)
	
