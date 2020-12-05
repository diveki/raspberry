import time, math
from gpiozero import OutputDevice as stepper


class StepperMotor:
    sequence = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]
    rotation_per_step = 1/(2038*2)
    stride_angle = 410 * rotation_per_step  # degree
    
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = stepper(pin1)
        self.pin2 = stepper(pin2)
        self.pin3 = stepper(pin3)
        self.pin4 = stepper(pin4)
        self.pins = [self.pin1, self.pin2, self.pin3, self.pin4]
        self.step_count = len(self.sequence)
        self.step_direction = 1
        self.wait_time = 0.001
        self.angle = 0

    def _move_continuous(self):
        step_counter = 0
        while True:
            # print(step_counter)
            # print(sequence[step_counter])

            for pin in range(len(self.pins)):
                xpin = self.pins[pin]
                if self.sequence[step_counter][pin] != 0:
                    xpin.on()
                else:
                    xpin.off()
            step_counter = step_counter + self.step_direction

            if step_counter >= self.step_count:
                step_counter = 0
            if step_counter < 0:
                step_counter = self.step_count + self.step_direction
            
            time.sleep(self.wait_time)

    def _move_discrete(self):
        step_counter = 0
        steps = 0
        while self.steps_to_make > steps:
            for pin in range(len(self.pins)):
                xpin = self.pins[pin]
                if self.sequence[step_counter][pin] != 0:
                    xpin.on()
                else:
                    xpin.off()
            step_counter = step_counter + self.step_direction

            if step_counter >= self.step_count:
                step_counter = 0
            if step_counter < 0:
                step_counter = self.step_count + self.step_direction
            steps = steps + 1
            time.sleep(self.wait_time)

    def forward(self, speed=1, angle=None):
        self.set_direction(1)
        self.set_speed(speed)
        if angle:
            if angle < self.stride_angle:
                pass
            else:
                self.set_step_number(angle)
                self.set_angle(angle)
                self._move_discrete()
        else:
            self._move_continuous()

    def backward(self, speed=1, angle=None):
        self.set_direction(-1)
        self.set_speed(speed)
        if angle:
            if angle < self.stride_angle:
                pass
            else:
                self.set_step_number(angle)
                self.set_angle(angle)
                self._move_discrete()
        else:
            self._move_continuous()

    def set_direction(self, direction):
        self.step_direction = direction
    
    def set_speed(self, speed):
        if speed == 0:
            self.wait_time = 1000
        else:
            self.wait_time = -0.01*speed+0.011

    def set_step_number(self, angle):
        self.steps_to_make = round(angle / self.stride_angle)

    def set_angle(self, angle):
        self.angle = self.angle + self.step_direction*angle
		
    def stop(self):
        for pin in self.pins:
            pin.off()
        print('Motor stopped!')

    def close(self):
        for pin in self.pins:
            pin.close()
        print('Connection with motor closed!')
