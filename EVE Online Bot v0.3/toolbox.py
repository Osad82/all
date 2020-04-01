from PIL import ImageGrab
from PIL import ImageOps
from time import sleep
from lib_cord import *
from numpy import *
import pyautogui
import threading
import os
'''



Управление мышью и клавишами
'''
def lmc(x):
	pyautogui.moveTo(x)
	pyautogui.click()
	sleep(.1)
#ЛКМ
def rmc(x):
	pyautogui.moveTo(x)
	pyautogui.rightClick()
	sleep(.1)
#ПКМ
def lmc_long(x1, x2):
	pyautogui.moveTo(x1)
	pyautogui.mouseDown(button = 'left')
	pyautogui.moveTo(x2, duration = 1)
	pyautogui.mouseUp(button = 'left')
	sleep(.1)
#Выделение
def key_down(key):
	pyautogui.keyDown(key)
	sleep(.1)
#зажимает клавишу
def key_up(key):
	pyautogui.keyUp(key)
	sleep(.1)
#отпускает клавишу
'''




Управление зрением
'''
def screenGrab():
	im = ImageGrab.grab()
	return im
#Делает скрин и передает его дальше
def trunk_switch(x):
	im = screenGrab()
	rgb = im.getpixel(x)
	if rgb[0] < 10 and rgb[1] > 70 and rgb[2] > 90:
		return False
	else:
		return True
#Датчик заполнения отсека руды
def drill_switch(x):
	im = screenGrab()
	rgb = im.getpixel(x)
	if rgb[0] < 200 and rgb[1] < 200 and rgb[2] < 200:
		return False
	else:
		return True
#Датчик работы буров
'''




Передвижение в космосе
'''
def exit_port():
	lmc(Cord.exit_p)
	sleep(.1)
#Выйти из порта
def enter_port(x):
	key_down('d')
	lmc(x)
	key_up('d')
	sleep(.1)
#Вернуться в порт
def menu_psa():
	lmc(Cord.psa)
	sleep(.1)
#Вкладка "Пояса"
def menu_ast():
	lmc(Cord.ast)
	sleep(.1)
#Вкладка "Астероиды"
def menu_stns():
	lmc(Cord.stns)
	sleep(.1)
#Вкладка "Станции"
def warp(x):
	key_down('s')
	lmc(x)
	key_up('s')
	sleep(10)
#Варп джамп
def miniwarp(x):
	key_down('w')
	lmc(x)
	key_up('w')
	sleep(60)
	lmc(Cord.stop)
	sleep(.1)
#Подлёт к цели (60 сек) и остановка
def get_target(x):
	key_down('ctrl')
	lmc(x)
	key_up('ctrl')
	sleep(5)
#Захват цели
def unload():
	lmc(Cord.trunk_open)
	lmc(Cord.trunk_ore_open)
	lmc_long(Cord.trunk_ore_cor1, Cord.trunk_ore_cor2)
	lmc_long(Cord.unload1, Cord.unload2)
	lmc(Cord.tr_close)
	lmc(Cord.tr_close)
	sleep(.1)
#Разгрузка трюма на склад
'''



Управление добычей
'''
def start_mining():
	lmc(Cord.trg)
	lmc(Cord.drill_1)
	lmc(Cord.drill_2)
	sleep(.1)
#Включение буров
def mining_logic():
	while True:
		if trunk_switch(Cord.trunk_ore_see) != True:
			break
		if drill_switch(Cord.drill_see_1) == True:
			ink = True
		elif drill_switch(Cord.drill_see_2) == True:
			ink = True
		else: 
			ink = False
		if ink == False:
			lmc(Cord.drill_1)
			lmc(Cord.drill_2)
			sleep(1)
			rmc(Cord.empy_point)
			sleep(.1)
			get_target(Cord.fst_pos)
			start_mining()
		sleep(15)
#Добывает пока не заполнится отсек (я сам не понимаю что тут происходит)
