from gpiozero import Motor, Button

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
button_forward = Button(17)
button_backward = Button(27)

button_forward.hold_time = 0.2
button_forward.hold_repeat = True

button_backward.hold_time = 0.2
button_backward.hold_repeat = True


def rotate(button, m, direction='forward'):
    if button.is_pressed:
        if direction == 'forward':
            print('Moving forward')
            return m.forward()
        if direction == 'backward':
            print('Moving backward')
            return m.backward()
        
def motor_stop(button, m):
    m.stop()


button_forward.when_held = lambda : rotate(button_forward, motor, direction='forward')
button_forward.when_released = lambda : motor_stop(button_forward, motor)

button_backward.when_held = lambda : rotate(button_backward, motor, direction='backward')
button_backward.when_released = lambda : motor_stop(button_backward, motor)


while True:
    pass
