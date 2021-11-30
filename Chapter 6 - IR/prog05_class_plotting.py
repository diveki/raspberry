import threading
import time
from raspberry_functions import read_2column_files, interpolate1d
from gpiozero import LED, MCP3008
import datetime as dt
import matplotlib.pyplot as plt
import random


class ActiveSensor:
	def __init__(self, led, mcp, calibname):
		self.led = led
		self.mcp = mcp
		self.calibfile = calibname
		self.initialize_calibration(self.calibfile)
		self.event = threading.Event()
		self.event_plot = threading.Event()
		self.dlist = []
		self.ylist = []
		
	def start(self):
		self.event.clear()
		self.led.on()
		t = threading.Thread(target=self.start_measurement)
		t.start()

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			dd = dt.datetime.now()
			current_voltage = self.mcp.voltage
			current_distance = interpolate1d(self.calib_volt, self.calib_distance, current_voltage)
			print(f'Current distance from object is: {current_distance:.2} cm')
			self.prepare_data(dd, current_distance)
			time.sleep(1)
		
	def stop(self):
		self.event.set()
		self.led.off()
		print('Measurement is stopped')

	def initialize_calibration(self, filename):
		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)

	def prepare_data(self, dd, yy, maxlen=20):
		self.dlist.append(dd)
		self.ylist.append(yy)
		if len(self.dlist) > maxlen:
			self.dlist.pop(0)
			self.ylist.pop(0)

	def plot_initialize(self):
		plt.ion()
		self.figure, self.ax = plt.subplots(figsize=(8,6))
		self.line1, = self.ax.plot(self.dlist, self.ylist, 'o-')
		plt.title("Dynamic Plot of measurement",fontsize=25)
		plt.xlabel("Time",fontsize=18)
		plt.ylabel("Distance (cm)",fontsize=18)
		plt.grid(True)

	def start_plot(self):
		self.event_plot.clear()
		t = threading.Thread(target=self.start_measurement)
		t.start()

	def stop_plot(self):
		self.event_plot.set()
		print('Measurement is stopped')

	def plot_distance_thread(self):
		while not self.event_plot.is_set():
			self.line1.set_xdata(self.dlist)
			self.line1.set_ydata(self.ylist)
			self.ax.set_ylim(min(self.ylist)*0.99, max(self.ylist)*1.01) # +1 to avoid singular transformation warning
			self.ax.set_xlim(min(self.dlist), max(self.dlist))
			self.figure.canvas.draw()
			self.figure.canvas.flush_events()
			plt.gcf().autofmt_xdate()
			time.sleep(2)


# class ActiveSensorTest:
# 	def __init__(self):
# 		self.event = threading.Event()
# 		self.event_plot = threading.Event()
# 		self.dlist = []
# 		self.ylist = []
		
# 	def start(self):
# 		self.event.clear()
# 		t = threading.Thread(target=self.start_measurement)
# 		t.start()

# 	def start_measurement(self):
# 		print('Measurement started')
# 		while not self.event.is_set():
# 			dd = dt.datetime.now()
# 			current_voltage = random.uniform(0,10)
# 			print(f'Current distance from object is: {current_voltage:.2} cm')
# 			self.prepare_data(dd, current_voltage)
# 			time.sleep(1)
		
# 	def stop(self):
# 		self.event.set()
# 		print('Measurement is stopped')

# 	def initialize_calibration(self, filename):
# 		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)

# 	def prepare_data(self, dd, yy, maxlen=20):
# 		self.dlist.append(dd)
# 		self.ylist.append(yy)
# 		if len(self.dlist) > maxlen:
# 			self.dlist.pop(0)
# 			self.ylist.pop(0)

# 	def plot_initialize(self):
# 		plt.ion()
# 		self.figure, self.ax = plt.subplots(figsize=(8,6))
# 		self.line1, = self.ax.plot(self.dlist, self.ylist, 'o-')
# 		plt.title("Dynamic Plot of temperature",fontsize=25)
# 		plt.xlabel("Time",fontsize=18)
# 		plt.ylabel("Temperature (C)",fontsize=18)
# 		plt.grid(True)

# 	def start_plot(self):
# 		self.event_plot.clear()
# 		t = threading.Thread(target=self.plot_distance_thread)
# 		t.start()


# 	def plot_distance_thread(self):
# 		while not self.event_plot.is_set():
# 			self.line1.set_xdata(self.dlist)
# 			self.line1.set_ydata(self.ylist)
# 			self.ax.set_ylim(min(self.ylist)*0.99, max(self.ylist)*1.01) # +1 to avoid singular transformation warning
# 			self.ax.set_xlim(min(self.dlist), max(self.dlist))
# 			self.figure.canvas.draw()
# 			self.figure.canvas.flush_events()
# 			plt.gcf().autofmt_xdate()
# 			time.sleep(2)

if __name__ == '__main__':
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	a = ActiveSensor(ir, mcp, calib_file)
	# a = ActiveSensorTest()


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.