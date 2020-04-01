# 94<> 58||
class Screen:
	WIN_WIDTH, WIN_HEIGHT = 1440, 900
	FPS = 2
	padding_main = 15
	workspace_start_x = padding_main
	workspace_start_y = padding_main
	workspace_finish_x = WIN_WIDTH - (padding_main*2)
	workspace_finish_y = WIN_HEIGHT - (padding_main*2)

class Colors:
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	DARKGREEN = (0, 200, 0)
	BLUE = (0, 0, 255)
	GRAY = (100, 100, 100)