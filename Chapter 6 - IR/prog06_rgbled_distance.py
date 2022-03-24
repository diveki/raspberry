import threading
import time
from raspberry_functions import read_2column_files, interpolate1d, ActiveSensor
from gpiozero import LED, MCP3008, RGBLED
import datetime as dt
import matplotlib.pyplot as plt


class RGBActiveSensor(ActiveSensor):
	def __init__(self, rgb, led, mcp, calibname):
		super().__init__(led, mcp, calibname)
		self.rgb = rgb

	def start(self):
		self.event.clear()
		self.led.on()
		t = threading.Thread(target=self.start_measurement)
		trgb = threading.Thread(target=self.start_rgb)
		t.start()
		trgb.start()

	def start_rgb(self):
		print('Rgb started')
		while not self.event.is_set():
			if len(self.ylist) > 0:
				self.set_color(self.ylist[-1])
			time.sleep(1)

	def stop(self):
		self.event.set()
		self.led.off()
		self.rgb.off()
		print('Measurement is stopped')

	def set_color(self, value):
		if value < 10:
			self.rgb.color = (1,0,0) # green
		elif 10 <= value < 17:
			self.rgb.color = (1,1,0) # yellow
		elif value >= 17:
			self.rgb.color = (0,1,0) # red



if __name__ == '__main__':
	rgb = RGBLED(16,20,21)
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	a = RGBActiveSensor(rgb, ir, mcp, calib_file)


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.
