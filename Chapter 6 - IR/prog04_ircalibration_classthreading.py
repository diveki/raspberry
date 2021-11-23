import threading
import random
import time


class ActiveSensor:
	def __init__(self, led, mcp, calibname):
		self.led = led
		self.mcp = mcp
		self.calibfile = calibname
		self.event = threading.Event()
		
	def start(self):
		self.event.clear()
		t = threading.Thread(target=self.start_measurement)
		t.start()

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			print(f'Measured value is: {random.randint(0, 10)} ')
			time.sleep(1)
		
	def stop(self):
		self.event.set()
		print('Measurement is stopped')
	

