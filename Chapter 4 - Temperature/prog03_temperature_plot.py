import matplotlib.pyplot as plt
import datetime as dt

filename = 'test.csv'

def read_data(fn, delimiter=','):
	f = open(fn, 'r')
	lines = f.readlines()
	f.close()
	date = []
	tc = []
	for line in lines[1:]:
		a = line.strip().split(',')
		dd = dt.datetime.strptime(a[0], '%Y-%m-%d %H:%M:%S')
		date.append(dd)
		tc.append(a[1])
	return date, tc

d,t = read_data(filename)

plt.plot(d,t, 'o-')
plt.gcf().autofmt_xdate()
plt.show()
