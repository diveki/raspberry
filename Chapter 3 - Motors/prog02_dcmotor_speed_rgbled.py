from gpiozero import Motor, Button, RGBLED

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
led = RGBLED(red=9, green=10, blue=11, active_high = True)
button_start_stop = Button(17)
button_faster = Button(27)
button_slower = Button(22)

on_off = False   # keeps note about the rotation of the motor True-rotates, False-stopped


def start_stop(button, m):
    global on_off, led
    if on_off:
        on_off = False
        m.stop()
        led.off()
        print('Motor off...')
    else:
        on_off = True
        m.forward()
        color = value2rgb(0, 1, m.value)
        led.color = color
        print('Motor on...')

def speed(button, increment = 0.1):
    global led, motor
    new_speed = motor.value + increment
    if new_speed > 0 and new_speed < 1.01:
        print(f'New speed: {new_speed}')
        motor.value = new_speed
        color = value2rgb(0, 1, new_speed)
        led.color = color
    else:
        print('Motor speed is out of range of 0 and 1.')
        print(f'Current speed is: {motor.value}')

def value2rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))/255
    r = int(max(0, 255*(ratio - 1)))/255
    g = (255 - b - r)/255
    return r, g, b


button_start_stop.when_pressed = lambda : start_stop(button_start_stop, motor)
button_faster.when_pressed = lambda : speed(button_faster, increment=0.1)
button_slower.when_pressed = lambda : speed(button_slower, increment=-0.1)

while True:
    pass
