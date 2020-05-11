from gpiozero import Button
import os
import time
import random

button = Button(2)

N = 5    # number of trials
waiting_times = list(range(1,11))
delays = []

sounds = os.listdir('./sounds')

for n in range(N):
	print(f'Game {n+1} started')
	time.sleep(1)
	print('Press the button when signal heard')
	ran = random.choice(waiting_times)
	time.sleep(ran)
	os.system('aplay sounds/{0}'.format(sounds[ran-1]))
	print('press now')

	start = time.time()
	button.wait_for_press()
	end = time.time()
	delay = end - start
	delays.append(delay)

print(f'The game is over')
reaction = sum(delays) / N
print(f'Your average reaction took {reaction:.2f} seconds')
