# pip install pygame==1.9.4
from gpiozero import Button
import numpy as np
import time, threading
from raspberry_functions import read_2column_files, interpolate1d, ActiveSensor
from gpiozero import LED, MCP3008

# motor_left = Motor(forward=23, backward = 24, enable=25)  #
# motor_right = Motor(forward=27, backward = 22, enable=17)  #

ir = LED(2)
button = Button(3)
mcp = MCP3008(channel=7)
calib_file = 'ir_calibration.csv'
sensor = ActiveSensor(ir, mcp, calib_file)
sampling_rate = 1/5


class HeartBeatSensor(ActiveSensor):
    def __init__(self, ir=ir, mcp=mcp, button=button, calib_file=calib_file, sampling_rate=1):
        super.__init__(ir, mcp, calib_file, sampling_rate=sampling_rate)
        self.button = button
        self.is_measuring = False
        self.button.when_pressed = self.measurement

    def measurement(self):
        if self.is_measuring:
            self.stop()   # inherited function
            self.stop_plot()
            self.is_measuring = False
        else:
            self.start()  # inherited function
            time.sleep(0.1)
            self.plot_initialize()
            self.start_plot()
            self.is_measuring = True


hb = HeartBeatSensor(ir, mcp, button, calib_file, sampling_rate)
hb.plot_length = 100
