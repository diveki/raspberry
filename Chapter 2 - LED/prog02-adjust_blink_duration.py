from gpiozero import LED
from time import sleep

# initialize variables that can be changed  
max_blinking = 5
duration_on = 3
duration_off = 1

# initialize led object
led = LED(25)

# set a counter
count = 0

# enter a loop that counts up to max_blinking
while count < max_blinking:
    print(count, end=' ')               # visualization: print the counter
    led.on()                            # switch on the led
    sleep(duration_on)                  # wait `duration_on` seconds
    led.off()                           # switch it off
    sleep(duration_off)                 # wait `duration_off` seconds
    count = count + 1                   # increase the counter by 1
