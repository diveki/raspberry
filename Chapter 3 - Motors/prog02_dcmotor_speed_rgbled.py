from gpiozero import Motor, Button, RGBLED

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
led = RGBLED(red=9, green=10, blue=11, active_high = True)
button_start_stop = Button(17)
button_faster = Button(27)
button_slower = Button(22)

on_off = False   # keeps note about the rotation of the motor True-rotates, False-stopped


def start_stop(button, m):
    global on_off
    if on_off:
        on_off = False
        return m.stop
    else:
        on_off = True
        return m.forward

def speed(increment = 0.1):
    global led, motor
    new_speed = motor.value + increment
    if new_speed > 0 and new_speed < 1.01:
        motor.value = new_speed
    else:
        print('Motor speed is out of range of 0 and 1.')
        print(f'Current speed is: {motor.value}')


button_start_stop.when_pressed = start_stop(button_start_stop, motor)
button_faster.when_pressed = speed(increment=0.1)
button_slower.when_pressed = speed(increment=-0.1)

while True:
    pass
