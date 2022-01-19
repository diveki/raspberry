import cv2, time
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from gpiozero import LED
from raspberry_functions_studentVersion import prepare_data, frame2grayscale

# inicializald a kamerat
cap = 
# inicializald a ledet
led = 


def motion_sensor(frame, calibration, limit=2):
    # 1) alkalmazd a cv2.threshold fuggvenyt a frame kepen, aminek min erteke a limit (bemeneti ertekkent megadhato)
    # max erteke legyen 255, es hasznald a cv2.THRESH_BINARY modszert
    # 2) szamitsd ki a thresholdolt matrix osszes elemenek osszeget es oszd el a calibration bemeneti valtozoval
    # az igy kapott ertek lesz a visszaadott erteke a fuggvenynek
    pass

def led_control(led, value, threshold = 0.8):
    # ha a value erteka nagyobb mint threshold erteke
    # akkor bekapcsolni a ledet
    # ha kisebb akkor kikapcsolni a ledet
    pass


height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
calibration = height * width * 256

# olvasd ki a kepet
ret, frame = 
# alakitsd szurke szinskalara a frame2grayscale fuggvenyt hasznalva
frame = 
# javitsd fel a kontrasztot a cv2.equalizeHist fuggveny segitsegevel
frame = 

max_count = 20
dplot = [dt.datetime.now()]
# ird be a mozgas indikator erteket a tplot listaba (a motion_sensor fuggveny altal adott ertek)
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

    # szamold ki a hatter levont kepet (mostani kep - elozo kep)
    delta_frame = 
    # hatarozd meg a mozgas indikator erteket a delta_frame-bol
    motion = 

    dplot, tplot = prepare_data(dt.datetime.now(), motion, dplot, tplot)

    # vezereld a led mukodeset a led_control fuggvennyel
    ........
    # frissitsd a hatterkepet (a jelenlegi uj kep = regi kep)
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

