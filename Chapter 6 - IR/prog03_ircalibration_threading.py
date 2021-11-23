import threading
import random
import time

def start(event):
	print('Measurement started')
	while not event.is_set():
		print(f'Measured value is: {random.randint(0, 10)} ')
		time.sleep(1)
		
def stop(event):
	event.set()
	print('Measurement is stopped')
	

kill = threading.Event()
t = threading.Thread(target=start, args=(kill,))
t.start()
time.sleep(6)
stop(kill)
t.join()
