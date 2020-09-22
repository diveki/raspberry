from gpiozero import Motor, Button

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
button_forward = Button(17)
button_backward = Button(27)


def rotate(button, m, direction='forward'):
    if button.is_pressed:
        if direction == 'forward':
            return m.forward
        if direction == 'backward':
            return m.backward
    else:
        return m.stop


button_forward.when_held = rotate(button_forward, motor, direction='forward')
button_backward.when_held = rotate(button_backward, motor, direction='backward')


while True:
    pass
