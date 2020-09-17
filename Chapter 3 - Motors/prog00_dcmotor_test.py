from gpiozero import Motor, OutputDevice

# switching on motor with manually activating the Enable pin
motor = Motor(forward=23, backward = 24)  # Motor(23,24)
motor_enable = OutputDevice(25)

## Measure the voltage between the ground and IN1, IN2, EN1
## since we have not switched them on they should show 0 V

motor_enable.on()  # activate EN1
## measure the voltage between GND and EN1
## now it should be 3.3 V, roughly

motor.forward(speed=0.8) # makes the motor spin with a certain speed, that can vary between 0 and 1
## measure the voltage between GND and IN1; plus measure the voltage on the pins of the motor
## or the GND and OUT1 (the last two should be the same)
## if this value does not reach 3V, the motor will not spin

motor.is_active  # prints out True, showing the motor is active
motor.value      # prints the value corresponding to the speed
motor.stop()   # stops the motor

motor_enable.off()   # switch off the enable, that prevents the motor of rotating
motor.backward(speed=0.9)  # does not work

motor_enable.on()
motor.backward(speed=0.9)  # the motor rotates the other direction

motor.reverse()     # reverses the direction of rotation with the speed it had
motor.stop()

#########################################
# controlling the motor without manually enabling the EN1

motor = Motor(forward=23, backward = 24, enable=25)  # Motor(23,24,25)
# the enable argument takes care of enabling the driver right after the initialization of the object
motor.forward()  # should rotate without any problem
motor.stop()
