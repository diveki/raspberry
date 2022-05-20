# importald a threading csomagot
# importald a time csomagot
# importald be a  read_2column_files es interpolate1d fuggvenyeket a raspberry_functions_studentVersion modulbol
# from gpiozero import LED, MCP3008
# importald a datetime csomagot mint dt
# importald a matplotlib.pyplot csomagot mint plt

class RGBActiveSensor(ActiveSensor):
	def __init__(self, rgb, led, mcp, calibname):
		super().__init__(led, mcp, calibname)
		self.rgb = rgb

	def start(self):
		# allitsd vissza alap allapotba a self.event esemenyt a clear metodussal
		# kapcsold be a self.led-et
		t = threading.Thread(target=self.start_measurement)
		trgb = threading.# inicializalj egy Thread-et ami a self.start_rgb fuggvenyt inditja el
		t. # inditsd el a threadet
		trgb. # inditsd el a threadet

	def start_rgb(self):
		print('Rgb started')
		while not ........:  # vizsgald meg a self.event allapotat
			if len(self.ylist) > 0:
				# hivd meg a self.set_color fuggvenyt. Bemeno parameter a self.ylist utolso eleme (-1-ik elemkent is lehet hivatkozni ra)
			time.sleep(1)

	def stop(self):
		# aktivald a self.event esemenyt
        # kapcsold ki a self.led-et
		# kapcsold ki a self.rgb-et
		print('Measurement is stopped')

	def set_color(self, value):
		if value < 10:
			self.rgb.color = (1,0,0) # green
		elif 10 <= value < 17:
			# az rgb szine legyen sarga (nezz utana az sargahoz tartozo rgb kodnak) # yellow
		elif value >= 17:
			# az rgb szine legyen piros # red



if __name__ == '__main__':
	rgb = RGBLED(16,20,21)
	ir = LED(2)
	mcp = MCP3008(channel=7)
	calib_file = 'ir_calibration.csv'
	a = RGBActiveSensor(rgb, ir, mcp, calib_file)


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.
