# importaljuk a LED klasszt a gpiozero csomagbol
# importaljuk a cv2 es time csomagokat
import numpy as np
from raspberry_functions import traffic_light_sequence

red    = # inicializalj egy LED objektumot a 17es pinnel
yellow = # inicializalj egy LED objektumot a 27es pinnel
green  = # inicializalj egy LED objektumot a 22es pinnel
cap    = # inicializalj egy video objektumot a cv2 csomag VideoCapture fuggvenyevel a '\dev\video0' argumentummal


while True:
    ret, frame = # keszits egy kepet a cap-nek a read metodusaval
    frame = # hasznald a cv2 csomag cvtColor fuggvenyet a frame valtozon, ahol cv2.COLOR_BGR2GRAY argumentummal szurkeve alakitod a kepet
    light = # szamold ki a teljes kep pixeleinek atlagerteket. Hasznald az np.mean fuggvenyt es oszd le 256-tal, hogy 0 es 1 kozotti szamot kapj
    print(light)
    if .......:  # ha light erteke kisebb mint 0.3 azaz kezd sotetedni
        # piros kikapcs
        # zold kikapcs
        # sarga bekapcs
        time.sleep(0.5)
        # sarga kikapcs
    else:
        # hivd meg a traffic_light_sequence fuggvenyt a red, yellow, green bemeno parameterekkel
    time.sleep(0.2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()
