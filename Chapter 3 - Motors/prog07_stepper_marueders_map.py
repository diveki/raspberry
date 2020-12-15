
import subprocess
import time
from stepper_motor import StepperMotor

m = StepperMotor(12,16,20,21)

data = [{'name':'Phone1', 'mac':"4a-c0-56-a9-1a-46", 'ip':'192.168.0.166'},
        {'name':'Phone2', 'mac':"4a-c0-56-a9-1a-44", 'ip':'192.168.0.132'}
]

# def test(ip):
#     p=subprocess.Popen(f'ping -W 2 -c 3 {ip}', shell=True, stdout=subprocess.PIPE)
#     p.wait()
#     output=p.stdout.read()
#     return output

while True:
    people_at_home = 0
    print("starting loop")
    output = subprocess.check_output("arp -a", shell=True)
    print ("starting scan")
    for item in data:
        # test(item['ip'])
        outp = subprocess.check_output(f'ping -W 2 -c 3 {item['ip']}', shell=True)
        if item['mac'] in output.decode() or item['mac'].replace('-',':') in output.decode():
            people_at_home = people_at_home + 1
    
    if people_at_home == 0:
        if m.angle == 180:
            m.backward(speed=1, angle=180)
    else:
        if m.angle == 0:  # 0 degree is alone position
            m.forward(speed=1, angle=180)
            time.sleep(2)
    
    time.sleep(5)
