import keyboard
import pygame
import random
import ctypes
import os
import sys

# Initialize Pygame
pygame.init()

# Get screen dimensions
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Place window at top-right, leave 10 pixels space
window_pos = (screensize[0] - 110, 10)

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_pos[0]},{window_pos[1]}"

# Initialize screen with NOFRAME to make it headerless
screen = pygame.display.set_mode((100, 100), pygame.NOFRAME)
pygame.display.set_caption('KeyPress Feedback')

# Load the sound file
click_sound = pygame.mixer.Sound("speuzer.mp3")

# Function to change screen color
def change_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill(color)
    pygame.display.update()

# Function to play sound and change color
def play_sound_and_change_color(e):
    click_sound.play()
    change_color()

# Listen to all keys
keyboard.on_press(callback=play_sound_and_change_color)

# Main loop to keep the pygame window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
