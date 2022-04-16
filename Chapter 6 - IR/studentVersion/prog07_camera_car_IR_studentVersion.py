# importald be a Motor, LED, MCP3008 klasszokat a gpiozerobol
# importald be a numpy csomagot np neven
# importald be a sys, pygame, time, threading es cv2 csomagokat
# a raspberry_functions_studentVersion modulbol importald be a read_2column_files, interpolate1d fuggvenyeket es ActiveSensor klasszt 

motor_left = # inicializald a Motor objektumot elore forgatas 24es gpio, hatra forgatas 23as gpio, enable 25os gpio  
motor_right = # inicializald a Motor objektumot elore forgatas 22es gpio, hatra forgatas 27es gpio, enable 17es gpio  

ir = # inicializald az IR LEDet a 2es gpiora
mcp = # inicializald az ADC konvertert a 7es csatornara
calib_file = # add meg a kalibracios fajl nevet
sensor = # inicializald az ActiveSensor objektumot. A kotelezo parameterek mellett allitsd a print_distance parametert False ertekre
cap = # inicializald a kamerat bemeno parameter a '/dev/video0'

pygame.init( )


#Set canvas parameters
size = # ez egy tuple ket elemmel, javasolt ertekek 500 es 500

#Display size
screen = pygame.display.set_mode(size)

class Car:
    def __init__(self, m1, m2, sensor, camera):
        self.cap = camera
        self.motor1 = m1
        self.motor2 = m2
        self.ir_sensor = sensor
        self.stop_event = # hozz letre egy esemenyt
        self.move_thread = # hozz letre egy Threadet ami a self.start_movement metodust inditja majd el
        self.camera_thread = # hozz letre egy Threadet ami a self.start_camera metodust inditja majd el
        self.check_thread = # hozz letre egy Threadet ami a self.distance_check metodust inditja majd el
        # inditsd el a self.ir_sensor mereset
        # inditsd el a self.camera_thread-et
        # inditsd el a self.move_thread-et
        self.current_key = 'up'
        self.map_direction = {
            'right': 'left',
            'left': 'right',
            'up': 'down',
            'down': 'up',
        }
        self.allowed_direction = ''
        # inditsd el a self.check_thread-et

    def start_camera(self):
        while ........:  # a pontok helyen megvizsgaljuk, hogy az esemeny aktivalodott-e. Ha igen, ki kell lepnie a while ciklusbol. Alapertelmezetten az esemeny erteke False
            ret, frame = # keszits egy kepet a kamera read() metodusaval
            frame = np.rot90(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame,(0,0))
            pygame.display.flip()

    def start_movement(self):
        while ........:  # a pontok helyen megvizsgaljuk, hogy az esemeny aktivalodott-e. Ha igen, ki kell lepnie a while ciklusbol. Alapertelmezetten az esemeny erteke False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # allitsd meg a self.ir_sensor mereset
                    # a self.stop_event esemenyt allitsd at aktiv allapotba
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.current_key = 'right'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move right...')
                            # hivd meg a jobbra mozgato fuggvenyt (ne feledd, a self objektum tartalmazza)
                    if event.key == pygame.K_LEFT:
                        self.current_key = 'left'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move left...')
                            # hivd meg a balra mozgato fuggvenyt (ne feledd, a self objektum tartalmazza)
                    if event.key == pygame.K_DOWN:
                        self.current_key = 'down'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move backward...')
                            # hivd meg a hatra fele mozgato fuggvenyt (ne feledd, a self objektum tartalmazza)
                    if event.key == pygame.K_UP:
                        self.current_key = 'up'
                        if self.current_key == self.allowed_direction or self.allowed_direction == '':
                            print('Move forward...')
                            # hivd meg az elore fele mozgato fuggvenyt (ne feledd, a self objektum tartalmazza)

                if event.type == pygame.KEYUP:
                    print('Stop motors...')
                    # allitsd le a motorokat (ne feledd, a self objektum tartalmazza)

            time.sleep(0.1)#Wait for 100ms before next button press

    def distance_check(self):
        while ........:  # a pontok helyen megvizsgaljuk, hogy az esemeny aktivalodott-e. Ha igen, ki kell lepnie a while ciklusbol. Alapertelmezetten az esemeny erteke False
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
        # inditsd el mindket motort elore a speed parameterrel (emlekezz, a self objektum tarolja a motorokat)

    def move_backward(self, speed=0.8):
        # inditsd el mindket motort hatra a speed parameterrel (emlekezz, a self objektum tarolja a motorokat)

    def move_left(self, speed=0.8):
        # inditsd el csak az 1es motort a speed parameterrel

    def move_right(self, speed=0.8):
        # inditsd el csak az 2es motort a speed parameterrel

    def stop_motors(self):
        # allitsd le mind a ket motort


a = Car(motor_left, motor_right, sensor, cap)
