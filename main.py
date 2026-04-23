"""
Digital Self-Expression: Art in Programming
Year of Aesthetics Workshop — Spring 2026
"""

import pygame
import random
from world import make_stars, cycle_sky, draw_stars, draw_sun, draw_ground, draw_trail, draw_player

pygame.init()

WIDTH, HEIGHT = 600, 600
GROUND_LEVEL = HEIGHT - 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# ======= STUDENT CUSTOMIZATION ============== #

### Name your animation! This will appear in the title bar
WINDOW_TITLE = "My World"   # change My World in the quotes to whatever you want
pygame.display.set_caption(WINDOW_TITLE)

###  colors
GROUND_COLOR = (50, 200, 100)
PLAYER_COLOR = (255, 100, 200) # only used for shapes, not emoji

###  movement & physics
SPEED = 5
JUMP_STRENGTH = -15
GRAVITY = 1
TRAIL_SIZE = 6

### change this to make the player bigger or smaller
PLAYER_SIZE = 20

### larger = longer trail
TRAIL_LENGTH = 100

# ============================================ #


# ======= SKY ================================ #
# The sky slowly cycles between two colors
# Each pair is (minimum, maximum) for Red, Green, Blue (RGB value)

# Default - Daylight
SKY_RED_RANGE = (150, 200)
SKY_GREEN_RANGE = (210, 240)
SKY_BLUE_RANGE = (240, 255)

# Deep night:
#SKY_RED_RANGE = (10, 40)
#SKY_GREEN_RANGE = (0, 20)
#SKY_BLUE_RANGE = (40, 100)

# Sunset:
#SKY_RED_RANGE = (180, 255)
#SKY_GREEN_RANGE = (60, 120)
#SKY_BLUE_RANGE = (20, 80)

# Ocean:
#SKY_RED_RANGE = (0, 30)
#SKY_GREEN_RANGE = (80, 160)
#SKY_BLUE_RANGE = (120, 220)

# Smaller = slower cycle, larger = faster
SKY_SPEED = 0.3

# ============================================ #


# ======= SUN / MOON ========================= #

SUN_X = 480 # 0 = far left, 600 = far right
SUN_Y = 100 # 0 = top, 600 = bottom
SUN_SIZE = 40
SUN_COLOR = (255, 220, 80) # try (200, 200, 255) for a moon
SHOW_SUN = True # set to False to hide

# ============================================ #


# ======= STARS ============================== #

STAR_COUNT = 80
STAR_COLOR = (255, 255, 255) # try (200, 220, 255) for icy blue

# ============================================ #


# ======= PLAYER ============================= #

### emoji player
# set USE_EMOJI = True and change the emoji to use it as your character!
PLAYER_EMOJI = "👾"
USE_EMOJI = False

### shape player (used when USE_EMOJI = False)
# default is circle
# to change shape, go to the DRAW PLAYER section below.

# ============================================ #


# ======= SPARKLE TRAIL ====================== #
# Each dot in the trail gets its own random color from the ranges below
# This gives a sparkle effect

# Each pair is (minimum, maximum) for Red, Green, Blue (RGB value)

# Default - random rainbow:
SPARKLE_COLOR = ((100, 255), (100, 255), (100, 255))

# Purple/Lavender (remove # to use):
#SPARKLE_COLOR = ((150, 255), (0, 150), (255, 255))

# Red/Fire:
#SPARKLE_COLOR = ((255, 255), (80, 180), (0, 40))

# Golden:
#SPARKLE_COLOR = ((255, 255), (200, 230), (120, 170))

# Slime:
#SPARKLE_COLOR = ((120, 240), (255, 255), (100, 120))

# One solid color (one single RGB value):
#SPARKLE_COLOR = (238, 196, 255)

# ============================================ #


### setup (ignore this section!) 
stars = make_stars(STAR_COUNT, WIDTH, GROUND_LEVEL)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", PLAYER_SIZE * 2)
x = WIDTH // 2
y = HEIGHT - 100
velocity_y = 0
on_ground = True
trail = []
sky_tick = 0


### game loop
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += SPEED

    # jump
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = JUMP_STRENGTH
        on_ground = False

    # gravity
    velocity_y += GRAVITY
    y += velocity_y

    # ground collision
    if y >= GROUND_LEVEL:
        y = GROUND_LEVEL
        velocity_y = 0
        on_ground = True

    # screen wrap
    if x > WIDTH:
        x = 0
    if x < 0:
        x = WIDTH

    # update trail
    trail.append((x + 10, y + 10))
    if len(trail) > TRAIL_LENGTH:
        trail.pop(0)

    ### draw
    sky_tick = cycle_sky(screen, sky_tick, SKY_RED_RANGE, SKY_GREEN_RANGE, SKY_BLUE_RANGE, SKY_SPEED)
    draw_stars(screen, stars, STAR_COLOR)
    draw_sun(screen, SHOW_SUN, SUN_X, SUN_Y, SUN_SIZE, SUN_COLOR)
    draw_trail(screen, trail, SPARKLE_COLOR, TRAIL_SIZE)
    draw_ground(screen, GROUND_COLOR, GROUND_LEVEL, WIDTH)


# ======= DRAW PLAYER ======================== #

    draw_player(screen, x, y, USE_EMOJI, emoji_font, PLAYER_EMOJI, PLAYER_COLOR, PLAYER_SIZE)

# ============================================ #

    pygame.display.flip()

pygame.quit()