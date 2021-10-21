import matplotlib.pyplot as plt
import os, glob, time
import datetime as dt
 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

 
def read_temp_raw(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(file_name):
    lines = read_temp_raw(file_name)
    now = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(file_name)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f, now

def prepare_data(date, tc, dplot, tplot, maxlen=20):
	dd = # alakitsd at az 'a' lista elso elemet (ido) datetime formatumba a strptime metodussal felhasznalva a string alakot '%Y-%m-%d %H:%M:%S'
	# add a dplot listahoz a dd erteket az append metodussal
	# add a tplot listahoz a tc erteket az append metodussal
	if len(dplot) > maxlen:
		dplot.pop(0)
		tplot.pop(0)
	return dplot, tplot
	

max_count = 20
dplot = [dt.datetime.now()]
tplot = [23.6]		
	
plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = # plottold a tplotot a dplot fuggvenyeben  'o-' markert hasznalva. Itt az ax.plot fuggvenyt kell majd hasznalni

plt.title(..........,fontsize=25)  # adj cimet a plotnak string formaban a ..... helyen

plt.xlabel("Time",fontsize=18)
plt.ylabel("Temperature (C)",fontsize=18)
plt.grid(True)


while True:
	tc, tf, ts = # olvasd ki a homersekletet a device_file fajlbol a read_temp fuggveny segitsegevel
	print(ts)
	dplot, tplot = # keszitsd elo a plottolni kivant listakat (dplot, tplot) a prepare_data fugvennyel. A maxlen erteke legyen max_count
	
	line1.set_xdata(dplot)
	line1.set_ydata(tplot)
	ax.set_ylim(min(tplot)*0.99,max(tplot)*1.01) # +1 to avoid singular transformation warning
	ax.set_xlim(min(dplot),max(dplot))
	figure.canvas.draw()
	figure.canvas.flush_events()
	plt.gcf().autofmt_xdate()
	
	time.sleep(1)
