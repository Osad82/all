# by de_jure 23.03.2020
# -*- coding: utf-8 -*-
from time import sleep
from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import pyautogui
from selenium import webdriver

sleep(10)
while True:
	sleep(2)
	pyautogui.moveTo((1380, 330))
	sleep(.1)
	pyautogui.leftClick()
	sleep(15)
	ImageGrab.grab().save('111.jpg')
	img_rgb = cv2.imread('111.jpg')
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread('222.jpg', 0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		x = int((pt[0]*2 + w)/2)
		y = int((pt[1]*2 + w)/2)
		if x > 900 and y > 500:
			cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			print(x, y)
			pyautogui.moveTo((x, y))
			sleep(1)
			pyautogui.leftClick()
			break
	pyautogui.moveTo((1440, 180))
	sleep(1)
	pyautogui.leftClick()
	pyautogui.moveTo((1300, 50))
	sleep(1)
	pyautogui.leftClick()
	pyautogui.keyDown('F5')
	sleep(.1)
	pyautogui.keyUp('F5')
	cv2.imwrite('screen.jpg', img_rgb)

