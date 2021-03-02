from gpiozero import MCP3008, LED

mcp = MCP3008(channel=7)
red = LED(21)
yellow = LED(20)
green = LED(16)

def lightning(volt, leds=[green, yellow, red]):
	if volt > 1.8:
		for led in leds:
			led.off()
	elif volt <= 1.8 and volt > 1.5:
		leds[0].on()
		leds[1].off()
		leds[2].off()
	elif volt <= 1.5 and volt > 1.3:
		leds[0].on()
		leds[1].on()
		leds[2].off()
	elif volt <= 1.3:
		leds[0].on()
		leds[1].on()
		leds[2].on()

while True:
	lightning(mcp.voltage, leds=[green, yellow, red])

