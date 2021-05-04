from gpiozero import LED
import cv2, time
import numpy as np
from raspberry_functions import traffic_light_sequence

red    = LED(17)
yellow = LED(27)
green  = LED(22)
cap    = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    light = np.mean(frame) / 256
    print(light)
    if light < 0.3:
        red.off()
        green.off()
        yellow.on()
        time.sleep(0.5)
        yellow.off()
    else:
        traffic_light_sequence(red, yellow, green)
    time.sleep(0.2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()
