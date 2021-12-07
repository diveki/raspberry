# importald az MCP3008 es LED klasszokat a gpiozero csomagbol
import numpy as np
from scipy.interpolate import interp1d
# importald a read_temp_raw fuggvenyt a temperature_functions fajlbol


mcp = # inicializald az ADC konvertert a megfelelo csatornaval
red = # inicializald a piros ledet
yellow = # inicializald a sarga ledet
green = # inicializald a zold ledet


def read_mapping(name):
	data = # olvasd be a name fajl tartalmat a read_temp_raw
	# a data listanak az elso eleme a fejlecet tartalmazza, igy ki kell venni a listabol a pop metodussal
	tc = # inicializalj egy ures listat a homersekleti ertekek reszere
	r = # inicializalj egy ures listat az ellenallasi ertekek reszere
	for line in data:
		clean_data = # minden sor ket szamot tartalmaz ami vesszovel van elvalasztva. hasznald a strip metodust az ujsorok es az ures helyek eltuntetesere, majd a split metodust, hogy a stringet szetvagd a vesszok menten
		# EZT A SORT NE SZERKESZD: a clean_data ket elemet fog tartalmazni, az elso a homerseklet, a masodik az ellenallas kOhmban kifejezve, string formatumban mind a ketto
		# bovitsd a tc listat a clean_data elso elemevel (homerseklet), de vigyazz, hogy a float paranccsal at kell alakitani a stringet szamma
		# bovitsd az r listat a clean_data masodik elemevel (ellenallas), de vigyazz, hogy a float paranccsal at kell alakitani a stringet szamma, valamint 1000el szorozni kell, hogy Ohmba kapjuk meg az erteket
	return np.array(tc), np.array(r)
	
def voltage2resistance(v_out, v_in=3.3, r=9.82e3):
	return r * v_out / (v_in - v_out)

def interpolate_temperature(resistance, tc, r): 
	f = interp1d(r,tc)
	return f(resistance)
	
def lightning(temp, leds=[green, yellow, red]):
	if ......:  # ha homerseklet (temp) kisebb mint 23 fok:
		# az osszes led kikapcsolt allapotban marad
	elif ....... : # ha temp < 28 es temp >= 23, akkor a zold led vilagit, a tobbi nem
		# 
		#
		#
	elif ...... : # ha temp < 32 es temp >= 28 akkor csak a piros nem vilagit
		#
		#
		#
	elif ........ : # ha a homerseklet nagyobb vagy egyenlo mint 32 fok akkor mindegyik vilagit
		# mindegyik led vilagit


tc, resistance = # a read_mapping fuggvennyel olvasd be az ntcc.csv nevu fajl tartalmat

while True:
	rt = # a voltage2resistance fuggvennyel alakitsd at a mert feszultseget (mcp.voltage) ellenallasa. A v_in erteke legyen 3.3 V, az r erteke pedig 9820 Ohm)
	t_therm = # becsuld meg az aktualis ellenellasertekhez tartozo homersekletet az interpolate_temperature fuggvennyel
	# inditsd el a lightning fuggvenyt a kiszamolt homerseklettel, figyelj, a ledek sorrendjere a listaban, zold az elso, aztan sarga es vegul piros
	print(t_therm)

