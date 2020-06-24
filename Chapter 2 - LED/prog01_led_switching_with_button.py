from gpiozero import LED, Button

led = LED(14, initial_value = False)
button = Button(2)


while True:
    button.wait_for_press()
    if led.is_lit:
        led.off()
    else:
        led.on()


# while True:
#     button.wait_for_press()
#     led.toggle()
