
import subprocess
import time
from stepper_motor import StepperMotor

m = # inicializalni stepper motort

data = [{'name':'Phone1', 'mac':"4a-c0-56-a9-1a-46", 'ip':'192.168.0.166'},
        {'name':'', 'mac':"", 'ip':''}     # toltsd ki az eszkoz nevet, mac cimet, ip cimet string formatumban
]


while True:
    people_at_home = 0
    print("starting loop")
    output = subprocess.check_output(......., shell=True)   # a pontok helyere ird be az arp paranccsal valo vegrehajtast
    print ("starting scan")
    for item in data:
        outp = subprocess.check_output(f'ping -W 2 -c 3 {......}', shell=True)   # a pontok helyere ird hivd meg az item valtozo ip cimet
        if item['mac'] in output.decode() or item['mac'].replace('-',':') in output.decode():  # 
            people_at_home = people_at_home + 1
    
    if people_at_home == 0:
        if .....:    # ellenorizd le, hogy a motor szoge 180 foknal van-e
            pass     # ha igen, forgasd a motort hatrafele 180 fokkal es a sebessege legyen 1
    else:
        if .......  :  # ellenorizd le, hogy a motor szoge 0 fok e
            pass     # ha igen, forgasd a motort elore 180 fokkal es a sebessege legyen 1
            time.sleep(2)
    
    time.sleep(5)
