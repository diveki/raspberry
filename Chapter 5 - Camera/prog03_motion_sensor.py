import cv2, time
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from gpiozero import LED
from raspberry_functions import prepare_data, frame2grayscale

cap = cv2.VideoCapture(0)
led = LED(2)


def motion_sensor(frame, calibration, limit=2):
    ret, frame = cv2.threshold(frame, limit, 255, cv2.THRESH_BINARY)
    return np.sum(frame) / calibration

def led_control(led, value, threshold = 0.8):
    if value > threshold:
        led.on()
    else:
        led.off()


height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
calibration = height * width * 256

ret, frame = cap.read()
frame = frame2grayscale(frame)
frame = cv2.equalizeHist(frame)

max_count = 20
dplot = [dt.datetime.now()]
tplot = [motion_sensor(frame, calibration)]		
	
plt.ion()

figure, ax = plt.subplots(1,1, figsize=(8,6))
line1, = ax.plot(dplot, tplot, 'o-')


while True:
    ret, frame1 = cap.read()
    frame1 = frame2grayscale(frame1)
    frame1 = cv2.equalizeHist(frame1)

    delta_frame = frame1-frame    
    frame_mean = motion_sensor(delta_frame, calibration)

    dplot, tplot = prepare_data(dt.datetime.now(), frame_mean, dplot, tplot)

#    led_control(led, frame_mean, threshold=0.8)
    frame = frame1

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

