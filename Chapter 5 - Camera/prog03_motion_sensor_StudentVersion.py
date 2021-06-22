import cv2, time
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from gpiozero import LED
from raspberry_functions import prepare_data, frame2grayscale

# inicializald a kamerat
cap = 
# inicializald a ledet
led = 


def motion_sensor(frame, calibration, limit=2):
    pass

def led_control(led, value, threshold = 0.8):
    pass


height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
calibration = height * width * 256

ret, frame = 
# alakitsd szurke szinskalara
frame = 
# javitsd fel a kontrasztot
frame = 

max_count = 20
dplot = [dt.datetime.now()]
# ird be az indikator erteket a tplot listaba
tplot = []		
	
plt.ion()

figure, ax = plt.subplots(1,1, figsize=(8,6))
line1, = ax.plot(dplot, tplot, 'o-')


while True:
    # olvasd ki az uj kepet
    ret, frame1 = 
    # alakitsd at szurke szinskalara
    frame1 = 
    # javitsd fel a kontrasztot
    frame1 = 

    # szamold ki a hatter levont kepet
    delta_frame = 
    # hatarozd meg a mozgas indikator erteket a delta_frame-bol
    motion = 

    dplot, tplot = prepare_data(dt.datetime.now(), motion, dplot, tplot)

    # vezereld a led mukodeset
    ........
    # frissitsd a hatterkepet
    frame = 

    line1.set_xdata(dplot)
    line1.set_ydata(tplot)
    ax.set_ylim(min(tplot)*0.99,max(tplot)*1.01) # +1 to avoid singular transformation warning
    ax.set_xlim(min(dplot),max(dplot))
    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.gcf().autofmt_xdate()

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

