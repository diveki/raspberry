
import subprocess
import time
from stepper_motor import StepperMotor

m = StepperMotor(1,2,3,4)

data = [{'name':'Phone1', 'mac':"4a-c0-56-a9-1a-46", 'ip':'192.168.0.166'},
        {'name':'Phone2', 'mac':"4a-c0-56-a9-1a-44", 'ip':'192.168.0.132'}
]
alone = True

def test(ip):
    p=subprocess.Popen(f'ping {ip}', shell=True, stdout=subprocess.PIPE)
    p.wait()
    output=p.stdout.read()
    return output

while True:
    print("starting loop")
    output = subprocess.check_output("arp -a", shell=True)
    print ("starting scan")
    for item in data:
        if item['mac'] in output.decode():
            test(item['ip'])
            print(f'{item['name']} is at home')
            if alone:
                m.forward(speed=1, angle=180)
                alone = False
                time.sleep(2)
        else:
            alone = True
    time.sleep(5)