from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

led = LED(4)
right_button = Button(15)
left_button = Button(14)

answer = True
turn_off = False

left_name = input('left player name is ')
right_name = input('right player name is ')


def pressed(button):
	global turn_off
	if led.is_lit:
		if button.pin.number == 14:
			print(left_name + ' won the game')
		else:
			print(right_name + ' won the game')
	else:	
		if button.pin.number == 14:
			print(left_name + ' lost the game')
		else:
			print(right_name + ' lost the game')	
	turn_off = True
	
	
right_button.when_pressed = pressed
left_button.when_pressed = pressed

led.off()

while answer:
	if not led.is_lit:
		print('Game has started!')
		sleep(uniform(2, 10))
		led.on()
	if turn_off:
		led.off()
		turn_off = False
		txt = input('Do you want to play again? (y/n) ')
		if txt == 'y':
			answer = True
		else:
			answer = False


#Can you put the game into a loop (you’ll need to remove the exit()), so that the LED comes on again?
#Can you add scores for both players that accumulate over a number of rounds, and displays the players’ total scores?
#How about adding in a timer, to work out how long it took the players to press the button after the LED turned off?