import pygame
import cv2
import os

pygame.init()

window_width = 1440
window_height = 1024
clock_tick_rate=20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

dead=False


file_path1 = '/home/cmay/Documents/OrganTrail/'

def resize(file_name, xDimension, yDimension):
    global file_path1
    file_path = file_path1 + file_name
    img = cv2.imread(file_path)
    imgResized = cv2.resize(img, (xDimension, yDimension), cv2.INTER_AREA)
    cv2.imwrite(file_path, imgResized)

# resize('Anubis.png', 100, 100)

background_image = pygame.image.load('PyramidBackground.png')

anubis_image = pygame.image.load('Anubis.png')


clock = pygame.time.Clock()

while dead == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        screen.blit(background_image, [0,0])
        screen.blit(anubis_image, [100, 100])
        pygame.display.flip()

        clock.tick(clock_tick_rate)
