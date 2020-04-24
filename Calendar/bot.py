from time import sleep
import pyautogui

sleep(3)
for _ in range(100):
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')

#🎲