import matplotlib
matplotlib.use('Qt5Agg')
from gpiozero import Button
import numpy as np
import time, threading
from raspberry_functions import read_2column_files, interpolate1d, ActiveSensor
from gpiozero import LED, MCP3008


ir = LED(2)
button = Button(3)
mcp = MCP3008(channel=7)
calib_file = 'heart_rate_calibration.csv'
sampling_rate = 5
sensor = ActiveSensor(ir, mcp, calib_file, calibrate=False, print_distance=False, sampling_rate=sampling_rate)
sensor.plot_length = sampling_rate * 60
