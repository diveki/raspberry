from gpiozero import Motor, LED, MCP3008
import numpy as np
import sys, pygame, pygame.freetype
import time, threading
import cv2
from raspberry_functions import read_2column_files, interpolate1d, ActiveSensor

motor_left = Motor(forward=24, backward = 23, enable=25)  #
motor_right = Motor(forward=22, backward = 27, enable=17)  #

ir = LED(2)
mcp = MCP3008(channel=7)
calib_file = 'ir_calibration.csv'
sensor = ActiveSensor(ir, mcp, calib_file, print_distance=False)
cap = cv2.VideoCapture('/dev/video0')

pygame.init( )


#Set canvas parameters
size = 500, 500

#Display size
screen = pygame.display.set_mode(size)

class Car:
    def __init__(self, m1, m2, sensor, camera):
        self.cap = camera
        self.motor1 = m1
        self.motor2 = m2
        self.ir_sensor = sensor
        self.stop_event = threading.Event()
        self.move_thread = threading.Thread(target=self.start_movement)
        self.camera_thread = threading.Thread(target=self.start_camera)
        self.check_thread = threading.Thread(target=self.distance_check)
        self.ir_sensor.start()
        self.camera_thread.start()
        self.move_thread.start()
        self.current_key = 'up'
        self.map_direction = {
            'right': 'left',
            'left': 'right',
            'up': 'down',
            'down': 'up',
        }
        self.allowed_direction = ''
        self.check_thread.start()

    def start_camera(self):
        while not self.stop_event.is_set():
            ret, frame = self.cap.read()
            frame = np.rot90(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame,(0,0))
            pygame.display.flip()

    def start_movement(self):
        while not self.stop_event.is_set():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ir_sensor.stop()
                    self.stop_event.set()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.current_key = 'right'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move right...')
                            self.move_right(speed=1)
                    if event.key == pygame.K_LEFT:
                        self.current_key = 'left'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move left...')
                            self.move_left(speed=1)
                    if event.key == pygame.K_DOWN:
                        self.current_key = 'down'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            
                            print('Move backward...')
                            self.move_backward(speed=1)
                    if event.key == pygame.K_UP:
                        self.current_key = 'up'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            
                            print('Move forward...')
                            self.move_forward(speed=1)

                if event.type == pygame.KEYUP:
                    print('Stop motors...')
                    self.stop_motors()

            time.sleep(0.1)#Wait for 100ms before next button press

    def distance_check(self):
        while not self.stop_event.is_set():
            print(self.ir_sensor.current_voltage)
            if self.ir_sensor.current_voltage > 1.3:
                self.allowed_direction = self.map_direction.get(self.last_key, '')
                if self.current_key != self.last_key:
                    print('Stop motors...')
                    self.stop_motors()
            else:
                self.allowed_direction = ''
                self.last_key = self.current_key
            time.sleep(0.5)

    def move_forward(self, speed=0.8):
        self.motor1.forward(speed=speed)
        self.motor2.forward(speed=speed)

    def move_backward(self, speed=0.8):
        self.motor1.backward(speed=speed)
        self.motor2.backward(speed=speed)

    def move_left(self, speed=0.8):
        self.motor1.backward(speed=speed)
        #mright.forward(speed=speed)

    def move_right(self, speed=0.8):
        #mleft.forward(speed=speed)
        self.motor2.backward(speed=speed)

    def stop_motors(self):
        self.motor1.stop()
        self.motor2.stop()


a = Car(motor_left, motor_right, sensor, cap)
