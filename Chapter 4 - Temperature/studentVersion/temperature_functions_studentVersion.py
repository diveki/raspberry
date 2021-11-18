

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
    '''
    dev: DHT11 eszkozt szimbolizalo objektum
    '''
	try:
		t = # olvassuk ki a dht11 objektumbol a homersekletet a temperature attributumot meghivva (nem metodus es nem fuggveny)
	except:
		t = 0
	return t

def get_hum(dev):
    '''
    dev: DHT11 eszkozt szimbolizalo objektum
    '''
	try:
		hum = # olvassuk ki a dht11 objektumbol a paratartalmat a humidity attributumot meghivva (nem metodus es nem fuggveny)
	except:
		hum = 0
	return hum

def ventillation(m, temp, hum):
	if temp and hum:
		if .......:  # ha homerseklet > 30 celsius fok vagy paratartalom > 50 % 
			# forgassuk a motort elore
		else:
			# forgassuk a motort hatra
	