import pygame

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1440, 900
padding_x, padding_y = 10, 0

pygame.init()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), \
	pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
#sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

clock = pygame.time.Clock()


money_rubins = 0

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Рубины:', 1, (255, 255, 255))

f2 = pygame.font.Font(None, 36)
text2 = f2.render(str(money_rubins), 1, (255, 255, 255))

f3 = pygame.font.Font(None, 36)
text3 = f3.render('300  | Воронка', 1, (0, 0, 0))

f4 = pygame.font.Font(None, 36)
text4 = f4.render('1000 | Деревянный каркас', 1, (0, 0, 0))

f5 = pygame.font.Font(None, 36)
text5 = f4.render('2500 | Бур 1', 1, (0, 0, 0))


voronka = pygame.image.load('textures/voronka.bmp')
voronka.set_colorkey((255, 255, 255))
voronka_rect = voronka.get_rect(bottomright=(512+padding_x, 512+30+padding_y))

rubin = pygame.image.load('textures/rubin.bmp')
rubin.set_colorkey((255, 255, 255))
rubin_rect = rubin.get_rect(bottomright=(512/2+30+padding_x, 512/2+30+30+padding_y))

wood = pygame.image.load('textures/wood.bmp')
wood.set_colorkey((255, 255, 255))
wood_rect = wood.get_rect(bottomright=(512+padding_x, 512+30+padding_y))

drill_1 = pygame.image.load('textures/drill_1.bmp')
drill_1.set_colorkey((255, 255, 255))
drill_1_rect = drill_1.get_rect(bottomright=(296+padding_x, 232+30+padding_y))

drill_2 = pygame.image.load('textures/drill_2.bmp')
drill_2.set_colorkey((255, 255, 255))
drill_2_rect = drill_2.get_rect(bottomright=(232+padding_x, 303+30+padding_y))
#232 303
textures = [
	['rubin', rubin, rubin_rect],
	['wood', wood, wood_rect],
	['voronka', voronka, voronka_rect],
	['money_rubins_1', text1, (5, 0)],
	['money_rubins_2', text2, (130, 0)],
	['drill_1', drill_1, drill_1_rect],
	['drill_2', drill_2, drill_2_rect],
]
textures_on = []

textures_on.append(textures[3])
textures_on.append(textures[4])
#textures_on.append(textures[1])
#textures_on.append(textures[2])

voronka_status = True
wood_status = True
drill_1_status = True
drill_2_status = True

click = 500
autoclick = 1
print(type(autoclick))

while 1:
	money_rubins += autoclick

	clock.tick(FPS)
		
	textures_on[1][1] = f2.render(str(money_rubins), 1, (255, 255, 255))
	sc.fill((50, 50, 50))
	for texture in textures_on:
		sc.blit(texture[1], texture[2])
	sc.blit(textures[0][1], textures[0][2])
	if voronka_status == True:
		button1 = pygame.draw.rect(sc, (255, 255, 255), (512+20, 30, 512, 60))
		sc.blit(text3, (550, 50))
	if wood_status == True:
		button2 = pygame.draw.rect(sc, (255, 255, 255), (512+20, 100, 512, 60))
		sc.blit(text4, (550, 120))
	if drill_1_status == True:
		button3 = pygame.draw.rect(sc, (255, 255, 255), (512+20, 170, 512, 60))
		sc.blit(text5, (550, 190))
	if drill_2_status == True:
		button4 = pygame.draw.rect(sc, (255, 255, 255), (512+20, 240, 512, 60))
		#sc.blit(text5, (550, 190))

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
	
	if pygame.mouse.get_focused():
		x, y = pygame.mouse.get_pos()
		if rubin_rect.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (1, 0, 0):
			money_rubins += click
		elif rubin_rect.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (0, 0, 1):
			money_rubins -= click
			print(money_rubins)
		elif button1.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (1, 0, 0) and \
		money_rubins > 299:
			money_rubins -= 300
			voronka_status = False
			click += 1
			textures_on.append(textures[2])
		elif button2.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (1, 0, 0) and \
		money_rubins > 999:
			money_rubins -= 1000
			wood_status = False
			click += 1
			textures_on.append(textures[1])
		elif button3.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (1, 0, 0) and \
		wood_status == False and \
		money_rubins > 2499:
			money_rubins -= 2500
			drill_1_status = False
			autoclick += 1
			textures_on.append(textures[5])
		elif button4.collidepoint(x, y) and \
		pygame.mouse.get_pressed() == (1, 0, 0) and \
		wood_status == False and \
		money_rubins > 4999:
			money_rubins -= 5000
			drill_2_status = False
			autoclick += 1
			textures_on.append(textures[6])

	pygame.display.update()