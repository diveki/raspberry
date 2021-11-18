
# importalni az adafruit_dht csomagot
# importalni a time csomagot
# a gpiozero csomagbol a Motor klasszt importalni
# a temperature_functions_studentVersion fajlbol a get_hum, get_temp, ventillation fuggvenyeket importalni

dev = # inicializalni a DHT11 eszkozt
motor = # inicializalni a motort. 3 bemeno parameter: elore forgato pin, hatra forgato pin es az enable pin szama 

while True:
	t = # olvasd ki a homersekletet a get_temp fuggvennyel
	h = # olvasd ki a homersekletet a get_hum fuggvennyel
	# nyomtasd ki a kepernyore a homersekletet es a paratartalmat: pl. megjeleno szoveg legyen: Temp: 23 Celsius degree , Hum: 50 %
	# hivd meg a ventillation fuggvenyt ami iranyitja a motor bekapcsolasat
	time.sleep(0.5)
	

