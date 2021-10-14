
import os
import glob
import time
import datetime as dt
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

filename =     # add meg a fajl nevet 
duration =     # add meg a mintavetelezes hosszat masodpercben
 
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
        now =   # mentsd el az aktualis idot es alakitsd at string formaba '%Y-%m-%d %H:%M:%S'
        return temp_c, temp_f, now

def write2file(txt,filename='temperature.csv'):
    # nyisd meg a filename nevu fajlt , append formaban 
    # ird bele a txt valtozo tartalmat
    # zard be a fajlt 
	
def prepare2save(tc,tf,ts):
	# a txt valtozohoz add hozza az idopontot, homersekletet celsius, homersekletet fahrenheitban (string formaban) vesszovel elvalasztva
	return txt
	
t0 = # inditsd el az ido szamlalasat (referencia ido)
t1 = # ez a valtozo tarolja majd az aktualis idot, amit minden ciklusban felulirunk

while .......:     # Az aktualisan eltelt idonek kisebbnek kell lenni mint a duration valtozo
	tc, tf, ts = read_temp(device_file)
	t1 = time.time()
	print(t1-t0)
	text = # alakitsd at a mert adatokat stringbe a prepare2save fuggvennyel
	# ird ki fajlba a text valtozo tartalmat a write2file fuggvennyel
	time.sleep(1)
	
