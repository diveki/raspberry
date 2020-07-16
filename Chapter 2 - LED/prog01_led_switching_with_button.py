from gpiozero import LED, Button

led = LED(17, initial_value = False)
button = Button(14)


while True:
    button.wait_for_press()
    if led.is_lit:
        led.off()
    else:
        led.on()


# while True:
#     button.wait_for_press()
#     led.toggle()
