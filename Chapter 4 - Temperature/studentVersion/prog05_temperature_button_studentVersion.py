# importald az MCP3008 es Button csomagokat a gpiozerobol
import numpy as np
# importald a sys es time csomagokat
from scipy.interpolate import interp1d
# a temperature_functions modulbol importald a read_temp_raw fuggvenyt


mcp = # inicializald az ADC konvertert a megfelelo csatornaval
button = # inicializald a gombot


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
	# a fuggveny adja vissza az adott ellenallast az alabbi keplet alapjan:
    # ellenallas * mert feszultseg / (tapfeszultseg - mert feszultseg)

def interpolate_temperature(resistance, tc, r):
	f = interp1d(r,tc)
	return f(resistance)

def compare(tc, eps=0.01):
    # NE SZERKESZD: tc egy lista ami 3 egymas utan mert homersekletet tartalmaz
	if ........: # ha a mert homersekletek paronkenti kulonbsegenek abszolut erteke kisebb mint eps, pl. abs(tc[0]-tc[1]) < eps
		t_mean = # szamold ki a 3 homerseklet atlagat, hasznald a sum fuggvenyt, a lista elemeinek osszeadasara es a len fuggvenyt, hogy megkapd hany szamot atlagolsz
		# nyomtasd ki, hogy: A testhomersekleted t_mean Celsius fok; t_mean-t ket tizedes pontossaggal add meg
		sys.exit(0)

tc, resistance = # olvasd be a homerseklet ellenallas lekepzest a read_mapping fuggvennyel. A fajl neve ntcc.csv		
t_body = []

print('Place your hand on the thermistor')
# varj a gomb lenyomasara. Ez az esemeny inditja a merest


while True:
	time.sleep(0.8)
	rt = voltage2resistance(......., v_in=3.3, r=9.82e3)  # add meg a mert feszultseget bemeno parameternek
	t_therm = # becsuld meg az aktualis ellenellasertekhez tartozo homersekletet az interpolate_temperature fuggvennyel
	# bovitsd a t_body listat a t_therm homerseklettel
	
	if len(t_body) < 3:
		continue
	else:
		# hivf meg compare fuggvenyt a mert homersekletekkel es homerseklet kulonbseg toleranciaval (eps)
		# vedd ki a t_body listabol a legregebbi mert homersekletet
		
		
	
