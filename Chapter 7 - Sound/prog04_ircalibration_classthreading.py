import threading
import time
from raspberry_functions import read_2column_files, interpolate1d
from gpiozero import LED, MCP3008


class ActiveSensor:
	def __init__(self, led, mcp, calibname):
		self.led = led
		self.mcp = mcp
		self.calibfile = calibname
		self.initialize_calibration(self.calibfile)
		self.event = threading.Event()
		
	def start(self):
		self.event.clear()
		self.led.on()
		t = threading.Thread(target=self.start_measurement)
		t.start()

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			current_voltage = self.mcp.voltage
			current_distance = interpolate1d(self.calib_volt, self.calib_distance, current_voltage)
			print(f'Current distance from object is: {current_distance:.2} cm')
			time.sleep(1)
		
	def stop(self):
		self.event.set()
		self.led.off()
		print('Measurement is stopped')

	def initialize_calibration(self, filename):
		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)
	

if __name__ == '__main__':
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	as = ActiveSensor(ir, mcp, calib_file)


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.