import pygame
import random

screen = WIDTH, HEIGHT = 720, 700
lane_pos = [40, 85, 180, 220]
lane_pos1 = [360, 400, 550, 590]
class Road():
	def __init__(self):
		self.image = pygame.image.load("img/road.jpg")
		self.image = pygame.transform.scale(self.image, (WIDTH - 60, HEIGHT))

		self.reset()
		self.move=True

	def update(self, speed):

		if self.move:
			self.y1 += speed
			self.y2 += speed
			if self.y1 >= HEIGHT:
				self.y1 =- HEIGHT
			if self.y2 >= HEIGHT:
				self.y2 =- HEIGHT
	def draw(self, win):
		win.blit(self.image, (self.x, self.y1))
		win.blit(self.image, (self.x, self.y2))
	def reset(self):
		self.x = 30
		self.y = 0
		self.y1 = 0
		self.y2 = -HEIGHT

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, type):
		super(Obstacle, self).__init__()
		dx = 0
		ctype = random.randint(1, 6)

		self.image = pygame.image.load(f'car/{ctype}.png')
		self.image = pygame.transform.flip(self.image, False, True)
		if ctype == 1:
			self.image = pygame.transform.scale(self.image, (110, 200))
		elif ctype == 2:
			self.image = pygame.transform.scale(self.image, (100, 180))
		elif ctype == 3:
			self.image = pygame.transform.scale(self.image, (150, 200))
		elif ctype == 4:
			self.image = pygame.transform.scale(self.image, (100, 190))
		elif ctype == 5:
			self.image = pygame.transform.scale(self.image, (90, 180))
		elif ctype == 6:
			self.image = pygame.transform.scale(self.image, (100, 210))


		self.rect = self.image.get_rect()
		self.rect.x = random.choice(lane_pos) + dx
		self.rect.y = -200

	def update(self, speed):
		self.rect.y += 10
		if self.rect.y >= HEIGHT:
			self.kill()
		self.mask = pygame.mask.from_surface(self.image)

	def draw(self, win):
		win.blit(self.image, self.rect)

class Obstacle1(pygame.sprite.Sprite):
	def __init__(self, type):
		super(Obstacle1, self).__init__()
		dx = 0
		ctype = random.randint(1, 6)

		self.image = pygame.image.load(f'car/{ctype}.png')
		if ctype == 1:
			self.image = pygame.transform.scale(self.image, (110, 200))
		elif ctype == 2:
			self.image = pygame.transform.scale(self.image, (100, 180))
		elif ctype == 3:
			self.image = pygame.transform.scale(self.image, (150, 200))
		elif ctype == 4:
			self.image = pygame.transform.scale(self.image, (100, 190))
		elif ctype == 5:
			self.image = pygame.transform.scale(self.image, (90, 180))
		elif ctype == 6:
			self.image = pygame.transform.scale(self.image, (100, 210))


		self.rect = self.image.get_rect()
		self.rect.x = random.choice(lane_pos1) + dx
		self.rect.y = -200

	def update(self, speed):
		self.rect.y += 7
		if self.rect.y >= HEIGHT:
			self.kill()
		self.mask = pygame.mask.from_surface(self.image)

	def draw(self, win):
		win.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, type):
		self.image = pygame.image.load("car/red_car.png")
		self.image = pygame.transform.scale(self.image, (200, 185))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, left, right, top, bottom):
		if left:
			self.rect.x -= 3
			if self.rect.x <= -60:
				self.rect.x = -60
		if right:
			self.rect.x += 3
			if self.rect.right >= 770:
				self.rect.right = 770
		if top:
			self.rect.y -= 4
			if self.rect.y <= 0:
				self.rect.y = 0
		if bottom:
			self.rect.y += 4
			if self.rect.y >= HEIGHT-185:
				self.rect.y = HEIGHT-185
	def draw(self, win):
		win.blit(self.image, self.rect)


class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()

		self.scale = scale
		self.image = pygame.transform.scale(img, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action