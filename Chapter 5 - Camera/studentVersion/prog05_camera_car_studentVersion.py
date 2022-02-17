# importald a Motor es Button objektumokat a gpiozerobol
# importald a numpy-t es nevezd el np-nek
import sys, pygame, pygame.freetype
# importald a time es a cv2 csomagokatimport time


motor_left = # inicializald a bal oldali motort, elore 23as pin, hatra 24es pin, enable 25os pin
motor_right = # inicializald a bal oldali motort, elore 27as pin, hatra 22es pin, enable 17es pin 
cap = # inicializald a kamerat, bemeno parameternek a '/dev/video0' parametert add meg

pygame.init( )


#Set canvas parameters
size = 500, 500

#Display size
screen = pygame.display.set_mode(size)

def move_forward(m1, m2, speed=0.8):
    # mozgasd az m1 motort elore a speed sebesseggel
    # mozgasd az m2 motort elore a speed sebesseggel

def move_backward(m1, m2, speed=0.8):
    # mozgasd az m1 motort hatra a speed sebesseggel
    # mozgasd az m2 motort hatra a speed sebesseggel

def move_left(mleft, mright, speed=0.8):
    # mozgasd az mleft motort hatra a speed sebesseggel

def move_right(mleft, mright, speed=0.8):
    # mozgasd az mright motort hatra a speed sebesseggel

def stop_motors(m1, m2):
    # megallitod mindket motort egyenkent


while 1:
    ret, frame = # keszits egy kepet
    frame = # forgasd el a kepet 90 fokkal az np.rot90 fuggvennyel
    frame = # alakitsd at a kep szinskalajat a cv2.cvtColor fuggvennyel a cv2.COLOR_BGR2RGB szinskalaba
    frame=pygame.surfarray.make_surface(frame)
    screen.blit(frame,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # zarjuk le a python programot a sys csomag exit fuggvenyevel
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('Move right...')
                # mozgasd az autot jobbra a move_right fuggvennyel es a megfelelo bemeno parameterekkel
            if event.key == pygame.K_LEFT:
                print('Move left...')
                # mozgasd az autot balra a move_left fuggvennyel es a megfelelo bemeno parameterekkel
            if event.key == pygame.K_DOWN:
                print('Move backward...')
                # mozgasd az autot jobbra a move_backward fuggvennyel es a megfelelo bemeno parameterekkel 
            if event.key == pygame.K_UP:
                print('Move forward...')
                # mozgasd az autot jobbra a move_forward fuggvennyel es a megfelelo bemeno parameterekkel 

        if event.type == pygame.KEYUP:
            print('Stop motors...')
            # allitsd meg az autot a stop_motors fuggvennyel es a megfelelo bemeno parameterekkel

    time.sleep(0.1)#Wait for 100ms before next button press
