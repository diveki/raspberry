import time 
from gpiozero import OutputDevice as stepper

IN1 = stepper(12)
IN2 = stepper(16)
IN3 = stepper(20)
IN4 = stepper(21)

step_pins = [IN1, IN2, IN3, IN4]

sequence = [[1,0,0,1],
            [1,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1]]

step_count = len(sequence)
step_dir = 1
wait_time = 0.001
step_counter = 0

while True:
    print(step_counter)
    print(sequence[step_counter])

    for pin in range(0,4):
        xpin = step_pins[pin]
        if sequence[step_counter][pin] != 0:
            xpin.on()
        else:
            xpin.off()
    step_counter = step_counter + step_dir

    if step_counter >= step_count:
        step_counter = 0
    if step_counter < 0:
        step_counter = step_count + step_dir
    
    time.sleep(wait_time)
