from time import sleep
from toolbox import *
from lib_cord import *


sleep(5)
while True:
	#многопоточный пуск
	exit_port()
	sleep(15)
	menu_psa()
	warp(Cord.fst_pos)
	sleep(50)
	menu_ast()
	miniwarp(Cord.fst_pos)
	mining_logic()
	menu_stns()
	enter_port(Cord.fst_pos)
	sleep(60)
	unload()




