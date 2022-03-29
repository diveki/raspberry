# importald be a threading csomagot
# importald be a time csomagot
# importald be a  read_2column_files es interpolate1d fuggvenyeket a raspberry_functions_studentVersion modulbol
# from gpiozero import LED, MCP3008


class ActiveSensor:
	def __init__(self, led, mcp, calibname):
		self.led = # rendeld hozza a led bemeno parametert
		self.mcp = # rendeld hozza az mcp bemeno parametert
		self.calibfile = # rendeld hozza a fajl nevet
		# hivd meg a self.initialize_calibration metodust a self.calibfile bemeno ertekkel
		self.event = # hozz letre egy esemenyt
		
	def start(self):
		# allitsd vissza a self.event esemenyt alapallapotba a clear metodussal
		# kapcsold be a ledet
		t = threading.Thread(# inicializald a threadet a self.start_measurement vegrehajtando fuggvennyel)
		# inditsd el a threadet

	def start_measurement(self):
		print('Measurement started')
		while not self.event.is_set():
			current_voltage = # olvasd le a jelenlegi feszultseget
			current_distance = # hasznald az interpolate1d fuggvenyt, hogy megbecsuld a tavolsagot a kalibracios feszultseg, tavolsag es a jelenlegi feszultseg alapjan
			print(f'Current distance from object is: {current_distance:.2} cm')
			# varj egy masodpercet
		
	def stop(self):
        # a self.event-et allitsd aktiv allapotba
		# kapcsold ki a ledet
		print('Measurement is stopped')

	def initialize_calibration(self, filename):
		self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)
	

if __name__ == '__main__':
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	a = ActiveSensor(ir, mcp, calib_file)


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.