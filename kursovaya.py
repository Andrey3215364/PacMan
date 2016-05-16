import pygame
import time
import random
import pyganim
from blocs import  *
from  PacMan import *
from Ghosts import *
from Coins import *
def main(self):
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    yellow = (255,255,0)
    BLUE = (0,0,255)
    size = (600,630)

    #-------------------

    WALL_WIDTH = 20
    WALL_HEIGHT = 20
    WALL_COLOR = (123,55,100)

    f = open("result.txt","r")
    print(f.read())
    x = 0
    y = 0

    pygame.font.init()



    pygame.init()

    #pygame.font.init()
    info_str = pygame.font.Font(None, 32)
    Is = pygame.Surface((600,30))
    #----------------------------------------

    coin_sprites_list = pygame.sprite.Group()
    monster_sprites_list = pygame.sprite.Group()
    wals_sprites_list = pygame.sprite.Group()
    obj_list = pygame.sprite.Group()
    hero_sprite = pygame.sprite.Group()
    #----------------------------------------
    left = False
    right = False
    up = False
    down = False

    g1left = False
    g1right = True
    g1up = False
    g1down = False


    score = 0

    Level = ['------------------------------',
            '-............................-',
            '-   -          -----     --  -',
            '- ---   -          -      -  -',
            '-   -   -    ----- -    ---  -',
            '-   -   -    .   -        -  -',
            '-   -              -   -     -',
            '-   --             -   -     -',
            '-...............--------     -',
            '-........-......-......---...-',
            '-........-----...............-',
            '-....-...-..-...........-....-',
            '-....-----..............-....-',
            '-........-..-.........-----..-',
            '-........------.........-....-',
            '-.....-..-....-.........-....-',
            '-....-----..............-....-',
            '-...............-....----....-',
            '-...............-            -',
            '- ............. -        --- -',
            '-         ---------        - -',
            '-           -              - -',
            '-     -         -          - -',
            '-     -         -   -        -',
            '-  -------      -----   -    -',
            '-     -         -       -    -',
            '-     -         -   -   -    -',
            '-     ---   -   -   -   ---  -',
            '-                            -',
            '------------------------------']

    #----------------------------------------

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PacMan")
    clock = pygame.time.Clock()
    pygame.init()
    done = True

    #-----------------------------------------

    hero = PacMan (400,500)
    hero_sprite.add(hero)
    obj_list.add(hero)

    monster1 = Ghost (200,350,"blue_ghost.gif")
    monster_sprites_list.add(monster1)
    obj_list.add(monster1)

    monster2 = Ghost (300,280,"red_ghost.gif")
    monster_sprites_list.add(monster2)
    obj_list.add(monster2)

    #------------------------------------------

    #-----------------------------------------------------
    x = 0
    y = 0
    for row in Level:
        for col in row:
            if col == "-":
                pf = Blocks(x,y)
                wals_sprites_list.add(pf)
                obj_list.add(pf)
            x += 20
        y += 20
        x = 0

    x1 = 0
    y1 = 5
    for row in Level:
        for col in row:
            if col == ".":
                coin = Coin (x1,y1)
                coin_sprites_list.add(coin)
                obj_list.add(coin)

            x1 += 20
        y1 = y1 + 20
        x1 = 7
    #---------------------------------------------------


    while  done:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    left = True

                if e.key == pygame.K_RIGHT:
                    right = True

                if e.key == pygame.K_UP:
                    up = True

                if e.key == pygame.K_DOWN:
                    down = True


            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    left = False

                if e.key == pygame.K_RIGHT:
                    right = False

                if e.key == pygame.K_UP:
                    up = False

                if e.key == pygame.K_DOWN:
                    down = False


        bonus_list = pygame.sprite.spritecollide(hero, coin_sprites_list, True)
        if len(bonus_list)>0 :
            score += 100




        screen.fill((10,48,66))
        screen.blit(Is,(0,600))
        Is.fill((23,95,120))
        Is.blit(info_str.render( 'SCORE:'+ str(score), 1 ,(0,0,200)), (0,0))

        #---------------------------------------------------





        #-----------------------------------------------------



        obj_list.draw(screen)
        hero.update(left,right,up,down, wals_sprites_list,coin_sprites_list)
        monster1.update(g1left,g1right,g1up,g1down,wals_sprites_list)
        pygame.display.flip()
        clock.tick(40)

    pygame.quit()

if __name__ == '__main__':
        main()