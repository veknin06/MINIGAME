# pygame template

import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font("Fixedsys.ttf", 100)

# Colours---------------------------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (150, 75, 0)
GRASS = (126, 200, 80)
SKY = (155, 206, 255)

#Variables--------------------------
apple_x = random.randrange(0, 640)
apple_y = 100
apple_radius = 8
apple_speed = 11
basket_height = 15
basket_width = 150
basket_x = WIDTH / 2 - basket_width / 2
basket_y = 440
basket_speed = 29
score = 0
end_score = 250

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True


    
# Basket - Left and Right--------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed
          
# Apples - Down--------------------------


    apple_y += apple_speed
    if apple_y > HEIGHT:
      apple_x = random.randint(0, WIDTH - apple_radius)
      apple_y = 0
      score -= 5

# Apples - Caught--------------------------
    if apple_y + apple_radius > basket_y and apple_x > basket_x and apple_x + apple_radius < basket_x + basket_width:
      apple_x = random.randint(0, WIDTH - apple_radius)
      apple_y = 0
      score += 10 

# Score Reset + End Score--------------------------
    if score < 0:
      score = 0

    if score >= end_score:
      main_menu()

  
# GAME STATE UPDATES
# All game math and comparisons happen here

# DRAWING--------------------------
    screen.fill((BLACK))
    
    pygame.draw.circle(screen, WHITE, (320, 280), 180)
    pygame.draw.circle(screen, BLACK, (320, 280), 145)

    pygame.draw.circle(screen, RED, (apple_x, apple_y), apple_radius)
  
    pygame.draw.rect(screen, BROWN, (basket_x, basket_y, basket_width, basket_height))
    
# Score - Tect--------------------------
    score_text = font.render("Score: " + str(score), True, SKY)
    screen.blit(score_text, (10, 10))

  
# Must be the last two lines
# of the game loop
    pygame.display.flip()
    clock.tick(30)
#---------------------------

pygame.quit()
