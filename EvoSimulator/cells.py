import random
import pygame
from settings import *

# Возвращает координаты отрисовки для всех клеток
def getCords(finish_x, finish_y, padding):
	cords = []
	for x in range(finish_x):
		for y in range(finish_y):
			if x%15 == 0 and y%15 == 0:
				cords.append((x+padding, y+padding, 15, 15))
	return cords

class EmpyCell:
	cord = None
	color = Colors.WHITE
	def __init__(self, _cord):
		self.cord = _cord

class Food:	
	_type = 'Food'
	cord = None
	todead = None
	color = Colors.GREEN
	deadcolor = Colors.DARKGREEN
	def __init__(self, _cord, _todead):
		self.cord = _cord
		self.todead = _todead

class Alive:
	_type = 'Alive'
	cord = None
	color = Colors.BLUE
	deadcolor = Colors.GRAY
	todead = 10
	toborn = 20
	def __init__(self, _cord):
		self.cord = _cord


def printFood(table, how_food, quant):
	if len(how_food) < quant:
		for i in range(0, quant - len(how_food)):
			while 1:
				f = table[random.randint(0, len(table)-1)]
				if type(f) == EmpyCell:
					for k in range(0, len(table)):
						if table[k] == f:
							table[k] = Food(f.cord, random.randint(10, 50))
							how_food.append(table[k])
							break
					break
	return how_food

def printAlive(table, quant):
	alive = []
	for i in range(0, quant):
		rand = random.randint(0, len(table)-1)
		a = table[rand] 
		table[rand] = Alive(a.cord)
		if table[rand] not in alive: 
			alive.append(table[rand])
	return alive

def moveAlive(table, alive):
	for a in alive:
		index = table.index(a)
		rand = random.randint(0, 4)
		while 1:
			if rand == 0:
				break
			elif rand == 1 and index > 0:
				#up
				table[index-1].cord, a.cord = a.cord, table[index-1].cord
				break
			#elif rand == 2 and index < 5290:
				#right
			#	table[index+58].cord, a.cord = a.cord, table[index+58].cord
			#	break
			elif rand == 3 and index < 5450:
				#up
				table[index+1].cord, a.cord = a.cord, table[index+1].cord 
				break
			#elif rand == 4 and index > 57:
				#left
			#	table[index-58].cord, a.cord = a.cord, table[-58].cord
			#	break
			else:
				break
	return alive