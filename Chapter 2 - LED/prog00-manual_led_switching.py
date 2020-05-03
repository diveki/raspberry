#### manually switching a led on and off
## steps to do:

# 1) install gpiozero
# 2) from gpiozero import LED
# 3) initialize a LED object with its corresponding gpio pin number: led = LED(25)
# 4) switch it on: led.on()
# 5) switch it off: led.off()

# import gpio control module
from gpiozero import LED

# initialize LED
led = LED(25)

# Switch on the LED
led.on()

# Switch off the LED
led.off()
