import cv2, time, subprocess
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from gpiozero import LED

cap = cv2.VideoCapture(0)
led = LED(2)


def motion_sensor(frame, calibration):
    return np.sum(frame) / calibration

def prepare_data(date, value, dplot, tplot, maxlen=20):
	dplot.append(date)
	tplot.append(value)
	if len(dplot) > maxlen:
		dplot.pop(0)
		tplot.pop(0)
	return dplot, tplot

def frame2grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def hist_equalizer(img):
    return cv2.equalizeHist(img)

def led_control(led, value, threshold = 0.8):
    if value > 0.8:
        led.on()
    else:
        led.off()


ret, frame = cap.read()
frame = frame2grayscale(frame)
frame = hist_equalizer(frame)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
calibration = np.product((height, width)) * 255

max_count = 20
dplot = [dt.datetime.now()]
tplot = [np.sum(frame)/calibration]		
	
plt.ion()

figure, ax = plt.subplots(2,1, figsize=(8,6))
ax[0].imshow(frame)
line1, = ax[1].plot(dplot, tplot, 'o-')

plt.title("Dynamic Plot of temperature",fontsize=25)



while True:
    # button.wait_for_press()
    ret, frame1 = cap.read()
    frame1 = frame2grayscale(frame1)
    frame1 = hist_equalizer(frame1)

    delta_frame = frame1-frame
    ret, delta_frame = cv2.threshold(delta_frame,2,255,cv2.THRESH_BINARY)
    ax[0].imshow(delta_frame)
    
    frame_mean = motion_sensor(delta_frame, calibration)
    dplot, tplot = prepare_data(dt.datetime.now(), frame_mean, dplot, tplot)

    led_control(led, frame_mean, threshold=0.8)
    frame = frame1

    line1.set_xdata(dplot)
    line1.set_ydata(tplot)
    ax[1].set_ylim(min(tplot)*0.99,max(tplot)*1.01) # +1 to avoid singular transformation warning
    ax[1].set_xlim(min(dplot),max(dplot))
    figure.canvas.draw()
    figure.canvas.flush_events()
    plt.gcf().autofmt_xdate()

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

