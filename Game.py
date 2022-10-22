from webbrowser import BackgroundBrowser
import pygame
import random
import math

pygame.init()

# game consts
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
WIDTH = 450
HEIGHT = 300


# game variables
score = 0
high_score = 0
player_x = 50
player_y = 200
rock_x = 0
rock_y = -10
y_change = 0
x_change = 0
gravity = 1
obstacles = [300, 450, 600]
obstacle_speed = 0
active = True
player_center_x = player_x + 5
player_center_y = player_y + 5
radius = 40
angle = -2
angle_change = 0
intro = True
running = False
rock_active = False

# game setup
screen = pygame.display.set_mode([WIDTH, HEIGHT])
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Infinite Runner")
background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game logic

while intro:
    welcome_text = font.render('Welcome To Game', True, black, white)
    instructions_text = font.render('Press Space to Start', True, black, white)
    screen.blit(welcome_text, (152, 100))
    screen.blit(instructions_text, (145, 150))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame. K_SPACE:
                intro = False
                running = True

while running:

    if rock_active and angle < 2:
        angle_change = 0.3
        angle += angle_change
        rock_x = player_center_x + math.cos(angle)*radius
        rock_y = (player_y + 5) + math.sin(angle)*radius
    if rock_active and angle >= 2:
        angle = -2
        angle_change = 0
        rock_x = -10
        rock_active = False

    timer.tick(fps)
    screen.fill(background)
    score_text = font.render(f'Score: {score}', True, white, black)
    high_score_text = font.render(
        f'High Score: {high_score}', True, white, black)
    screen.blit(score_text, (100, 250))
    screen.blit(high_score_text, (240, 250))
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])
    rock = pygame.draw.rect(screen, purple, [rock_x, rock_y, 5, 5])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                active = True
                obstacles = [300, 450, 600]
                score = 0

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_UP and y_change == 0:
                y_change = 18
            if event.key == pygame. K_SPACE and rock_active == False:
                rock_active = True

    for i in range(len(obstacles)):
        if active:
            if score < 20:
                obstacle_speed = 2
            if score > 20 and score < 40:
                obstacle_speed = 3
            if score > 40 and score < 60:
                obstacle_speed = 4

            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
            if rock.colliderect(obstacle0):
                obstacles[0] = random.randint(470, 570)
                score += 1
            if rock.colliderect(obstacle1):
                obstacles[1] = random.randint(470, 570)
                score += 1
            if rock.colliderect(obstacle2):
                obstacles[2] = random.randint(470, 570)
                score += 1

            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False
                if high_score < score:
                    high_score = score
        if not active:
            instructions_text = font.render('You Lose', True, black, white)
            instructions2_text = font.render(
                'Press Space To Retry', True, black, white)
            screen.blit(instructions_text, (120, 55))
            screen.blit(instructions2_text, (150, 75))

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()
