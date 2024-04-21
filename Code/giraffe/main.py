#!/usr/bin/env python3

from random import choice
from time import sleep
import pygame
import sys

# Initialization and game constants
height = 400
width = 600
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Giraffe")

background1 = pygame.image.load("Sprites/background.png")
background2 = pygame.image.load("Sprites/background_2.png")
background1_x = 0
background2_x = 600

score = 0
text = f"{score}"
font = pygame.font.Font('Fonts/SF-Pro-Rounded-Regular.ttf', 36)
text_surface = font.render(text, True, (0, 0, 0))
text_rect = text_surface.get_rect(center=(width // 2, height // 2))

clock = pygame.time.Clock()
running = True

# Game variables
player_img = pygame.image.load("Sprites/giraffe_1.png")
player_x = width // 6.75
player_y = height - player_img.get_height()
player = 1
player_increment = 1

coin_img = pygame.image.load("Sprites/coin.png")
coin_increment = 5
coin_x = [400, 800, 1200, 1600]
coin_y = [choice([260, 215, 175]), choice([260, 215, 175]), choice([260, 215, 175]), choice([260, 215, 175])]

# Functions
def check_hit(x_1, x_2, y_1, y_2, w_1, w_2, h_1, h_2):
    if (
        x_1 < x_2 + w_2 and
        x_1 + w_1 > x_2 and
        y_1 < y_2 + h_2 and
        y_1 + h_2 > y_2
    ):
        return True

def check_point(x, y):
	global score
	global coin_x
	global coin_y
	if x == True:
		score += 1
		pygame.mixer.music.load("SFX/giraffe_coin.wav")
		pygame.mixer.music.play(1)
		coin_x[y] = coin_x[3] + 400
		coin_y[y] = choice([260, 215, 175])
		element = coin_x.pop(y)
		coin_x.append(element)

def game_over():
	global coin_increment
	global player_increment
	global running
	coin_increment = 0
	player_increment = 0
	pygame.mixer.music.load("SFX/game_over.wav")
	pygame.mixer.music.play(1)
	sleep(1.5)
	running = False

def check_game_end():
	global coin_x
	if (coin_x[0] < 0 or
		coin_x[1] < 0 or
		coin_x[2] < 0 or
		coin_x[3] < 0
	):
		return True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_UP:
        		if player < 3:
        			player += player_increment
        			pygame.mixer.music.load("SFX/giraffe_powerup_1.wav")
        			pygame.mixer.music.play(1)
        		else:
        			pygame.mixer.music.load("SFX/giraffe_blocked.wav")
        			pygame.mixer.music.play(1)
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_DOWN:
        		if player > 1:
        			player -= player_increment
        			pygame.mixer.music.load("SFX/giraffe_powerup_2.wav")
        			pygame.mixer.music.play(1)
        		else:
        			pygame.mixer.music.load("SFX/giraffe_blocked.wav")
        			pygame.mixer.music.play(1)

    background1_x -= 1
    background2_x -= 1
    if background1_x == -600:
        background1_x = 600
    if background2_x == -600:
        background2_x = 600

    screen.fill((0, 0, 0))
    screen.blit(background1, (background1_x, 0))
    screen.blit(background2, (background2_x, 0))

    coin_x[0] -= coin_increment
    coin_x[1] -= coin_increment
    coin_x[2] -= coin_increment
    coin_x[3] -= coin_increment

    coin_1 = screen.blit(coin_img, (coin_x[0], coin_y[0]))
    coin_2 = screen.blit(coin_img, (coin_x[1], coin_y[1]))
    coin_3 = screen.blit(coin_img, (coin_x[2], coin_y[2]))
    coin_4 = screen.blit(coin_img, (coin_x[3], coin_y[3]))

    player_img = pygame.image.load(f"Sprites/giraffe_{player}.png")
    player_y = height - player_img.get_height()
    screen.blit(player_img, (player_x, player_y))

    check_1 = check_hit(player_x, coin_x[0], player_y, coin_y[0], player_img.get_width(), coin_img.get_width(), player_img.get_width(), coin_img.get_width())
    check_2 = check_hit(player_x, coin_x[1], player_y, coin_y[1], player_img.get_width(), coin_img.get_width(), player_img.get_width(), coin_img.get_width())
    check_3 = check_hit(player_x, coin_x[2], player_y, coin_y[2], player_img.get_width(), coin_img.get_width(), player_img.get_width(), coin_img.get_width())
    check_4 = check_hit(player_x, coin_x[3], player_y, coin_y[3], player_img.get_width(), coin_img.get_width(), player_img.get_width(), coin_img.get_width())

    check_point(check_1, 0)
    check_point(check_2, 1)
    check_point(check_3, 2)
    check_point(check_4, 3)

    text = f"{score}"
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, text_rect)

    coin_increment += 0.01

    # Game ends
    check_5 = check_game_end()
    if check_5:
    	game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
