import threading, signal
import time, subprocess
from raspberry_functions import read_2column_files, interpolate1d, ActiveSensor
from gpiozero import LED, MCP3008, RGBLED
import datetime as dt
import matplotlib.pyplot as plt

rgb = RGBLED(red=21, green=20, blue=16)
key_mapping = {
    'KEY_1': (1,0,0),
    'KEY_2': (0,1,0),
    'KEY_3': (0,0,1),
    'KEY_4': (1,1,0),
    'KEY_5': 'off'
}

class IR_Controlled_RGB:
    def __init__(self, rgb, key_mapping, conf_file=None):
        # self.rgb = rgb
        self.key_mapping = key_mapping
        self.stop_event = threading.Event()
        self.start()
        self.decoding = threading.Thread(target=self.action)
        self.decoding.start()

    def start(self):
        self.stop_event.clear()
        self.process = subprocess.Popen(['irw'], stdout=subprocess.PIPE, universal_newlines=True)
        # self.process = subprocess.Popen(['ping', '-n 1000', 'google.com'], stdout=subprocess.PIPE, universal_newlines=True)

    def stop(self):
        self.stop_event.set()
        self.process.send_signal(signal.CTRL_C_EVENT)  

    def action(self):
        while not self.stop_event.set():
            if len(self.process.stdout) > 0:
                self.get_key_from_signal(self.process.stdout)      
        
    def get_key_from_signal(self, value):
        pass

    def set_color(self, value):
        pass
		# if value < 10:
		# 	self.rgb.color = (1,0,0) # green
		# elif 10 <= value < 17:
		# 	self.rgb.color = (1,1,0) # yellow
		# elif value >= 17:
		# 	self.rgb.color = (0,1,0) # red


# For development:
# 1) Ird at a klasszt ugy, hogy ha nincs inicializalaskor megadva kalibracios fajl, akkor ne interpolaljon, hanem csak a mert feszultseget irja ki.
# 2) Modositsd a while ciklust ugy, hogy ha eler a feszultseg pl. 2 V-ot, akkor ne tortenjen tobb meres.
