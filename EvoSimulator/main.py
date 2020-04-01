import random
import os
import pygame
import cells
from settings import *

cords = cells.getCords(Screen.workspace_finish_x,
					Screen.workspace_finish_y,
					Screen.padding_main)
table = []
for cord in cords:
	k = cells.EmpyCell(cord)
	table.append(k)

pygame.init()
screen = pygame.display.set_mode((Screen.WIN_WIDTH, Screen.WIN_HEIGHT))
#screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), \
#	pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
clock = pygame.time.Clock()

food = []
first = True
while 1:
	clock.tick(Screen.FPS)
	os.system('cls')
	pygame.draw.rect(screen, Colors.WHITE, (Screen.workspace_start_x,
									Screen.workspace_start_y,
									Screen.workspace_finish_x,
									Screen.workspace_finish_y))
	#==========================================
	food = cells.printFood(table, food, 1000)
	if first == True:
		alive = cells.printAlive(table, 10)	
		first = False
	alive = cells.moveAlive(table, alive)
	for i in table:
		if type(i) == cells.Food:
			if i.todead > 0:
				pygame.draw.rect(screen, i.color, i.cord)
				i.todead -= 1
			elif i.todead == 0:
				pygame.draw.rect(screen, i.deadcolor, i.cord)
				i.todead -= 1
			else:
				table[table.index(i)] = cells.EmpyCell(i.cord)
				food.remove(i)
		elif type(i) == cells.EmpyCell:
			pygame.draw.rect(screen, i.color, i.cord)
		elif type(i) == cells.Alive:
			pygame.draw.rect(screen, i.color, i.cord)

	print('Еда:   \t', len(food))
	print('Живые: \t', len(alive))
	#==========================================
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
	pygame.display.update()