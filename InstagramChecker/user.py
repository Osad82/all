class User:
	login = None
	posts = None
	subscribers = None
	subscribe = None
	level_vtope = None
	
	def __init__(self, login, posts, subscribers, subscribe):
		self.login = login
		self.posts = posts
		self.subscribers = subscribers
		self.subscribe = subscribe

	def print(self):
		print(self.login + ':')
		print('Посты: {0} Подписчики: {1} Подписки: {2}'.format(self.posts, \
			self.subscribers, self.subscribe))