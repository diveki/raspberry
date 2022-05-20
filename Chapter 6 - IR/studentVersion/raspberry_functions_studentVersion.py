#### Chapter 4 - Temperature functions
from time import sleep 

def read_temp_raw(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(file_name):
    lines = read_temp_raw(file_name)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(file_name)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def get_temp(dev):
    try:
        t = dev.temperature
    except:
        t = 0
    return t

def get_hum(dev):
    try:
        hum = dev.humidity
    except:
        hum = 0
    return hum

def ventillation(m, temp, hum):
    if temp and hum:
        if temp > 30 or hum > 50:
            m.forward()
        else:
            m.stop()


# Chapter 5 - Camera functions
import cv2

def traffic_light_sequence(red, amber, green, dt = 3):
    sleep(dt)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(dt)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()	

def prepare_data(date, value, dplot, tplot, maxlen=20):
    dplot.append(date)
    tplot.append(value)
    if len(dplot) > maxlen:
        dplot.pop(0)
        tplot.pop(0)
    return dplot, tplot

def frame2grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# Chapter 6 - IR functions
from scipy.interpolate import interp1d
import numpy as np
import threading
import time
import datetime as dt
import matplotlib.pyplot as plt


def read_2column_files(name, sep=',', header=True):
    lines = read_temp_raw(name)
    # ha a header erteke igaz:
        # a lines listanak dobd ki az elso elemet (azaz azt a sort ami a fejlecet tartalmazza)
    distance = # inicializalj egy ures listat
    voltage = # inicializalj egy ures listat
    for line in lines:
        if line.strip() != '':
            data = # line valtozora alkalmazd a strip metodust, hogy eltunjenek az ures helyek a sztring elejerol es vegerol
            # majd alkalmazd ra a split metodust a sep parameterrel, ami megadja, milyen karakter menten vagjuk kette a sztringet 
            # hogy listat kapjunk
            # a data lista elso elemet (ami sztring) alakitsd at float tipussa, es add hozza a voltage listahoz
            # a data lista masodik elemet (ami sztring) alakitsd at float tipussa, es add hozza a distance listahoz
    return np.array(voltage), np.array(distance)

def interpolate1d(x, y, target):
    f = interp1d(x,y)
    return # hivd meg az f fuggvenyt a target valtozoval, hogy kapj egy tavolsag becslest


class ActiveSensor:
    def __init__(self, led, mcp, calibname, sampling_rate=1, print_distance=True, calibrate=True):
        self.led = led
        self.mcp = mcp
        self.calibfile = calibname
        self.sampling_rate = sampling_rate
        self.plot_length = 20
        self.initialize_calibration(self.calibfile)
        self.event = # hozz letre egy esemenyt a threading csomagbol
        self.event_plot = # hozz letre egy esemenyt a threading csomagbol
        self.dlist = # hozz letre egy ures listat
        self.ylist = # hozz letre egy ures listat
        self.print_distance = print_distance
        self.calibrate = calibrate
        
    def start(self):
        # allitsd vissza alap allapotba a self.event esemenyt a clear metodussal
        # kapcsold be a self.led-et
        t = threading.Thread(target=self.start_measurement)
        # inditsd el a t threadet

    def start_measurement(self):
        print('Measurement started')
        while not self.event.is_set():
            dd = # merd meg a jelenlegi idot a dt.datetime csomag now fuggvenyevel
            self.current_voltage = # merd meg a jelenlegi feszultseget a self.mcp-n
            if self.calibrate:
                self.current_distance = interpolate1d(self.calib_volt, self.calib_distance, self.current_voltage)
            else:
                self.current_distance = self.current_voltage
            if self.print_distance:
                print(f'Current distance from object is: {self.current_distance:.3} cm')
            self.prepare_data(dd, self.current_distance)
            time.sleep(1/self.sampling_rate)
        
    def stop(self):
        # aktivald a self.event esemenyt
        # kapcsold ki a self.led-et
        print('Measurement is stopped')

    def initialize_calibration(self, filename):
        self.calib_volt, self.calib_distance = read_2column_files(filename, header=True)

    def prepare_data(self, dd, yy):
        self.dlist, self.ylist = prepare_data(dd, yy, self.dlist, self.ylist, maxlen=self.plot_length)

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
        t = threading.Thread(target=self.plot_distance_thread)
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


