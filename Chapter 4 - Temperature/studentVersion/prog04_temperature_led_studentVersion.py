# importald a gpiozero csomagbol az MCP3008, LED objektumokat

mcp = # inicializald az MCP3008 objektumot a 7es csatornaval
red = # inicializald a piros LEDet
yellow = # inicializald a sarga LEDet
green = # inicializald a zold LEDet

def lightning(volt, leds=[green, yellow, red]):
	if .........:   # ha a volt erteke nagyobb mint 1.8
		for led in leds:
			# kapcsold ki a LEDeket
	elif volt <= 1.8 and volt > 1.5:
		leds[0].on()  # zold LED bekapcsolava EZT A SORT NEM KELL EDITALNI
		# sarga LED kikapcsol
		# piros led kikapcsol
	elif ...........:   # ha a volt <= 1.5 es volt > 1.3
		# zold LED bekapcsolva
		# sarga LED bekapcsol
		# piros led kikapcsol
	elif ...........:  # ha volt <= 1.3
		# minden LED bekapcsol

while True:
	lightning(mcp.voltage, leds=[green, yellow, red])

