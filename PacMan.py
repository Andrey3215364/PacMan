import pygame
import  pyganim
move = 3
width = 20
height = 20
yellow = (255,255,0)
color = yellow



ANIM_DELAY = 0.2
ANIM_STAY = [("pacman_right_open.png",ANIM_DELAY)]

PACMAN_ANIM_RIGHT = ["pacman_right_open.png",
                    "pacman_right_close.png"]

PACMAN_ANIM_LEFT = ["pacman_left_open.png",
                    "pacman_left_close.png"]

PACMAN_ANIM_DOWN = ["pacman_down_open.png",
                    "pacman_down_close.png"]

PACMAN_ANIM_UP = ["pacman_up_open.png",
                    "pacman_up_close.png"]

class PacMan(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.xvel = 0
        self.yvel = 0

        #self.image_l = pygame.image.load("pacman_left.png").convert_alpha()
        self.image_r = pygame.image.load("pacman_right_open.png").convert_alpha()
        #self.image_r2 = pygame.image.load("pacman_right_close.png").convert_alpha()
        #self.image_u = pygame.image.load("pacman_up.png").convert_alpha()
        #self.image_d = pygame.image.load("pacman_down.png").convert_alpha()
        self.image = self.image_r
        self.rect = pygame.Rect(x,y,19,19)

        self.boltAnimStay = pyganim.PygAnimation(ANIM_STAY,ANIM_DELAY)
        self.boltAnimStay.play()

        def make_boltAnim(anim_list,delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltANIMRIGHT = make_boltAnim(PACMAN_ANIM_RIGHT,0.1)
        self.boltANIMRIGHT.play()

        self.boltANIMLEFT = make_boltAnim(PACMAN_ANIM_LEFT,0.1)
        self.boltANIMLEFT.play()

        self.boltANIMUP = make_boltAnim(PACMAN_ANIM_UP,0.1)
        self.boltANIMUP.play()

        self.boltANIMDOWN = make_boltAnim(PACMAN_ANIM_DOWN,0.1)
        self.boltANIMDOWN.play()

    def update(self,left,right,up,down, wals,coins):
        self.xvel = 0
        self.yvel = 0
        oldx = self.rect.x
        oldy = self.rect.y
        score = 0
        if left:
            self.xvel = - move
            self.image.fill((10,48,66))
            self.boltANIMLEFT.blit(self.image,(0,0))
        elif right:
            self.xvel = move
            self.image.fill((10,48,66))
            self.boltANIMRIGHT.blit(self.image,(0,0))
        elif up:
            self.yvel = - move
            self.image.fill((10,48,66))
            self.boltANIMUP.blit(self.image,(0,0))
        elif down:
            self.yvel = move
            self.image.fill((10,48,66))
            self.boltANIMDOWN.blit(self.image,(0,0))
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if len(pygame.sprite.spritecollide(self,wals,False))>0 :
            self.rect.x = oldx
            self.rect.y = oldy


