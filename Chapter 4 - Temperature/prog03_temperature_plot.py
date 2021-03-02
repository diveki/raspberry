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
		dd = dt.datetime.strptime(a[0], '%Y-%m-%d %H:%M:%S')
		date.append(dd)
		tc.append(float(a[1]))
	return date, tc

lines = read_temp_raw(filename)
d,t = read_data(lines, delimiter=',')

plt.plot(d,t, 'o-')
plt.gcf().autofmt_xdate()
plt.show()
