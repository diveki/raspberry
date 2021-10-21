import matplotlib.pyplot as plt
import datetime as dt

filename = 'test.csv'

def read_temp_raw(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_data(lines, delimiter=','):
	date = []
	tc = []
	for line in lines[1:]:
		a = line.strip().split(',')
		dd = # alakitsd at az 'a' lista elso elemet (ido) datetime formatumba a strptime metodussal felhasznalva a string alakot '%Y-%m-%d %H:%M:%S'
		# add a 'date' listahoz a dd erteket az append metodussal
		# add az 'a' masodik elemet (celsius fok) a tc listahoz az append metodussal. Hasznald a float parancsot, hogy a stringet szamma alakitsd
	return date, tc

lines = # olvasd ki a filename nevu fajl tartalmat a read_temp_raw fuggvennyel
d,t = # valaszd szet a datumot es a homersekletet a read_data fuggvennyel

# plottold a t valozot a d fuggvenyeben, a marker tipusa legyen korocske vonallal: 'o-'
plt.gcf().autofmt_xdate()
plt.show()
