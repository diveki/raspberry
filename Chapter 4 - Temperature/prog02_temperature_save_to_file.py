
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
duration = 30  # given in seconds
 
def read_temp_raw(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(file_name):
    lines = read_temp_raw(file_name)
    now = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(file_name)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f, now

def write2file(txt,filename='temperature.csv'):
	f = open(filename, 'a')
	f.write(txt)
	f.close()
	
def prepare2save(tc,tf,ts):
	txt = ts + ',' + str(round(tc,2)) + ',' + str(round(tf,2)) + '\n'
	return txt
	
t0 = time.time()
t1 = time.time()

while t1 - t0 < duration:
	tc, tf, ts = read_temp(device_file)
	t1 = time.time()
	print(t1-t0)
	text = prepare2save(tc, tf, ts)
	write2file(text, filename=filename)
	time.sleep(1)
	
