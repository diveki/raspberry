#https://thepihut.com/blogs/raspberry-pi-tutorials/18095732-sensors-temperature-with-the-1-wire-interface-and-the-ds18b20
#http://docs.37sensors.com/#
#https://sensorkit.en.joy-it.net/index.php?title=KY-028_Temperature_Sensor_module_(Thermistor)
#https://www.malnasuli.hu/leckek/homerseklet-merese-1-wire-szenzorral/
#https://www.electronicshub.org/raspberry-pi-ds18b20-tutorial/

import os
import glob
import time
 
os.system('.....')    # modprobe w1-gpio
#  futtasd le a modprobe w1-therm parancsot is
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(......)[0]    # keresd meg van e '28'-al kezdodo fajl a base_dir mappaban
device_file = device_folder + '/w1_slave'
 
def read_temp_raw(file_name):
    f = open      # nyisd meg a file_name nevu fajlt olvasasra
    lines = f.   # olvasd ki a fajlbol az ossz sort egy listaba
    f.           # zard be a megnyitott kommunikaciot
    return lines
 
def read_temp(file_name):
    lines = # olvasd be a file_name tartalmat a read_temp_raw fuggvennyel
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(file_name)
    equals_pos = lines[1].    # talald meg a lines lista masodik elemeben melyik karakter pozicional van a t= string
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = #  alakitsd at a megtalalt homersekletet float tipusba es oszd le ezerrel, hogy celsius fokban legyen a homerseklet
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while True:
	print(read_temp(device_file))	
	time.sleep(1)
