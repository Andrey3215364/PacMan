
import pygame

PLATFORM_WIDTH = 20
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = (123,55,100)

class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("platform.png").convert()
        self.rect = pygame.Rect(x, y, 19, 19)
