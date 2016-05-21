import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.rect = pygame.Rect(x,y,0.000000001,0.000000001)
