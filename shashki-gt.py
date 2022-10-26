import os
import random
import time

import pygame

from objects import Player, Road, Obstacle, Obstacle1, Button

pygame.init()
screen = WIDTH, HEIGHT = 720, 700
win = pygame.display.set_mode(screen, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("ШАШКИ DRIVE")

BLUE = (30, 144, 255)
WHITE = (255, 255, 155)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

home_img = pygame.image.load("i.png")
home_img = pygame.transform.scale(home_img, (WIDTH, HEIGHT))
bg = pygame.image.load("img/bg.jpg")

cars = []
def center(image):
	return (WIDTH // 2) - image.get_width() // 2
play_img = pygame.image.load('play.png')
play_btn = Button(play_img, (100, 34), center(play_img)+10, HEIGHT-80)

gas_fx = pygame.mixer.Sound('sound/prodoljitelnyiy-zvonkiy-zvuk-raotayuschego-motorchika.wav')
break_fx = pygame.mixer.Sound('sound/audio-material-ekstrennogo-tormojeniya-42011.wav')
dtp_fx = pygame.mixer.Sound('sound/zvuk-iz-mema-smert-v-gta-5-gta-v---wasted-3380.wav')
pygame.mixer.music.load('sound/OFFL1NX_-_UPGRADE_74387561.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(1)

road = Road()
p = Player(270, HEIGHT-185, 0)

obstacle_group = pygame.sprite.Group()

home_page = True
game_page = False

move_left = False
move_right = False
move_up = False
move_down = False

counter = 0
speed = 15


run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_left = True

			if event.key == pygame.K_RIGHT:
				move_right = True

			if event.key == pygame.K_ESCAPE:
				run = False
			if event.key == pygame.K_UP:
				gas_fx.play()
				move_up = True
			if event.key == pygame.K_DOWN:
				break_fx.play()
				move_down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_left = False
			if event.key == pygame.K_RIGHT:
				move_right = False
			if event.key == pygame.K_UP:
				gas_fx.stop()
				move_up = False
			if event.key == pygame.K_DOWN:
				break_fx.stop()
				move_down = False



		if (event.type == pygame.MOUSEBUTTONDOWN):
			x, y = event.pos
			if x <= WIDTH//2:
				move_left = True
			else:
				move_right = True

		if event.type == pygame.MOUSEBUTTONUP:
			move_left = False
			move_right = False


	if home_page:
		win.blit(home_img, (0, 0))
		if play_btn.draw(win):
			p = Player(270, HEIGHT - 185, 0)
			home_page = False
			game_page = True

	if game_page:
		speed = 14
		win.blit(bg, (0, 0))
		road.update(speed)
		road.draw(win)

		counter += 1
		if counter % 50 == 0:
			obs = random.choices([1, 2, 3], weights=[6, 2, 2], k=1)[0]
			obstacle = Obstacle(obs)
			obstacle1 = Obstacle1(obs)
			obstacle_group.add(obstacle, obstacle1)

		obstacle_group.update(speed)
		obstacle_group.draw(win)

		p.update(move_left, move_right, move_up, move_down)
		p.draw(win)

		for obstacle in obstacle_group:
			if obstacle.rect.y >= HEIGHT:
				obstacle.kill()

			if pygame.sprite.collide_mask(p, obstacle):
				pygame.draw.rect(win, RED, p.rect, 1)
				speed = 0
				dtp_fx.play()
				time.sleep(2)
				home_page = True
				game_page = False
				obstacle_group.empty()



	pygame.display.update()

run()