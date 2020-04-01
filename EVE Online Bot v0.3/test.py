#набросок для кнопки выключения
#АНО РАБОТАЕТ!!!!!!

import threading
from time import sleep

def clock(interval):
	while True:
		sleep(interval)
		print('Hello world')

t = threading.Thread(target = clock, args = (10, ))
t.daemon = True
t.start()

while True:
	x = input()
	if x == 'q':
		exit()
	sleep(0.1)

