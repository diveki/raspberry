# importald a threading csomagot
# import a time csomagot
# importald a LED es MCP3008 objektumokat a gpiozero csomagbol
# importald a import read_2column_files es interpolate1d fuggvenyeket a raspberry_functions_studentVersion modulbol

ir = # inicializald a ledet a 2es gpiora
mcp = # inicializald az MCP3008at a 7es csatornara

calib_file = # add meg a kalibracios fajlod nevet sztring formaban
volt, distance = # olvasd be a kalibracios fajlbol a feszultseget es tavolsagokat

def start(event):
	print('Measurement started')
	while not event.is_set():
		current_voltage = # merd meg az mcp-n a feszultseget
		current_distance = # az interpolate1d fuggvenyt felhasznalva es a kalibracios fajlbol kinyert adatokbol, allapitsd meg, milyen tavolsag tartozik a mert feszultseghez
		# nyomtasd ki az aktualis tavolsagot 
		# varakozz 1 masodpercet
		
def stop(event):
	# aktivizald az esemenyt (event) a set metodussal
	print('Measurement is stopped')
	

kill = # definialj egy esemnyt a threading csomagbol
t = threading.Thread(target=start, args=(kill,))
t. # inditsd el a threadet
# varj 6 masodpercet 
# allitsd le a threadet a fent definialt stop fuggvennyel
t.join()
