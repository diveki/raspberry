# importald a matploltib csomagot
matplotlib.use('Qt5Agg')
# importald a threading csomagot
# importald a time csomagot
# importald be a  read_2column_files es interpolate1d fuggvenyeket a raspberry_functions_studentVersion modulbol
# from gpiozero import LED, MCP3008
# importald a datetime csomagot mint dt
# importald a matplotlib.pyplot csomagot mint plt

class ActiveSensor:
	# definiald az __init__ metodust, 3 bemeno parameterrel (a self-rol se feledkezz meg). A parameterek: led, mcp, calibname
		self.led = # a led valtozo erteket veszi fel a bejovo parameterek kozul
		self.mcp = # az mcp valtozo erteket veszi fel a bejovo parameterek kozul
		self.calibfile = # a calibname valtozo erteket veszi fel a bejovo parameterek kozul
		# hivd meg az initialize_calibration fuggvenyt (figyelj oda, hogy hasznalod a self objektumot). Bemeno parameterkent a self.calibfile valtozot add meg
		self.event = # hozz letre egy esemenyt
		self.event_plot = # hozz letre meg egy esemenyt
		self.dlist = # hozz letre egy ures listat
		self.ylist = # hozz letre egy ures listat
		
	def start(self):
		# allitsuk a self.event esemenyt alapallapotba a .clear() metodussal
		# kapcsoljuk be a self.led- et
		t = threading.# indits el egy Thread-et a threding csomagbol. A target argumentum erteke legyen a self.start_measurement fuggveny
		t. # indits el a t threadet

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			dd = # a dt csomagnak a datetime moduljabol allapitsd meg a jelenlegi idopillanatot a now fuggveny segitsegevel
			current_voltage = # olvasd le a jelenlegi feszultseget
			current_distance = # hasznald az interpolate1d fuggvenyt, hogy megbecsuld a tavolsagot a kalibracios feszultseg, tavolsag es a jelenlegi feszultseg alapjan
			print(f'Current distance from object is: {current_distance:.2} cm')
			self.prepare_data(dd, current_distance)
			# varj egy masodpercet
		
	def stop(self):
		# a self.event-et allitsd aktiv allapotba
		# kapcsold ki a ledet
		print('Measurement is stopped')

	def initialize_calibration(self, filename):
		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)

	def prepare_data(self, dd, yy, maxlen=20):
		# add hozza a self.dlist listahoz a dd parameter erteket
		# add hozza a self.ylist listahoz az yy parameter erteket
		if ...........: # ha a self.dlist lista hossza (elemeinek szama) > mint a maxlen erteke
			# tavoltsd el a self.dlist lista 0ik elemet
			# tavoltsd el a self.ylist lista 0ik elemet

	def plot_initialize(self):
		plt.ion()
		self.figure, self.ax = plt.subplots(figsize=(8,6))
		self.line1, = self.ax.plot(......)  # abrazold a self.dlist (x tengely) fuggvenyeben a self.ylist (y tengely),  vonnallal osszekottot korocske szimbolumokkal: 'o-'
		plt.title(.................,fontsize=25) # string formajaban adj cimet a plotnak a ................. helyen
		plt.xlabel("Time",fontsize=18)
		plt.ylabel("Distance (cm)",fontsize=18)
		plt.grid(True)

	def start_plot(self):
		# allitsuk a self.event_plot esemenyt alapallapotba a .clear() metodussal
		t = threading.# indits el egy Thread-et a threding csomagbol. A target argumentum erteke legyen a self.plot_distance_thread fuggveny
		t. # indits el a t threadet

	def stop_plot(self):
		# a self.event_plot-ot allitsd aktiv allapotba
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



if __name__ == '__main__':
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	a = ActiveSensor(ir, mcp, calib_file)


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.