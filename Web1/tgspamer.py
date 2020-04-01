import pyautogui
from time import sleep
from tqdm import tqdm

x = int(input())
sleep(5)
for i in tqdm(range(0, x)):
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	sleep(.1)
	pyautogui.keyUp('ctrl')
	pyautogui.keyUp('v')
	pyautogui.keyDown('enter')
	pyautogui.keyUp('enter')
while 1:
	pass