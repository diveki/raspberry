from gpiozero import LED
from time import sleep

red = LED(2)
amber = LED(3)
green = LED(4)

green.on()
amber.off()
red.off()

while True:
    sleep(10)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(10)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()


# from gpiozero import TrafficLights
# from time import sleep

# lights = TrafficLights(2, 3, 4)

# lights.green.on()

# while True:
#     sleep(10)
#     lights.green.off()
#     lights.amber.on()
#     sleep(1)
#     lights.amber.off()
#     lights.red.on()
#     sleep(10)
#     lights.amber.on()
#     sleep(1)
#     lights.green.on()
#     lights.amber.off()
#     lights.red.off()


# from gpiozero import TrafficLights
# from time import sleep
# from signal import pause

# lights = TrafficLights(2, 3, 4)

# def traffic_light_sequence():
#     while True:
#         yield (0, 0, 1) # green
#         sleep(10)
#         yield (0, 1, 0) # amber
#         sleep(1)
#         yield (1, 0, 0) # red
#         sleep(10)
#         yield (1, 1, 0) # red+amber
#         sleep(1)

# lights.source = traffic_light_sequence()

# pause()