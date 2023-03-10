import pygame
import os
import sys
import random


pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 600
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
lvl = 'menu'
timer=0
from load import *



def startMenu():
    global lvl
    sc.blit(menu_image, (0, 0))
    sc.blit(start_image, (100, 200))

    sc.blit(exit_image, (100, 400))
    pos_mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if 100 < pos_mouse[0] < 400:
            if 200 < pos_mouse[1] < 275:
                print('кнопка старта игры')
                lvl = 'game'
            elif 300 < pos_mouse[1] < 375:
                print('кнопка меню рекордов')
            elif 400 < pos_mouse[1] < 475:
                print('кнопка выхода из игры')
                pygame.quit()
                sys.exit()
    pygame.display.update()
class FOТ():
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = fon_image

    def update(self):
        self.timer += 2
        sc.blit(self.image[self.frame], (0, 0))
        if self.timer / FPS > 0.1:
            if self.frame == len(self.image) - 1:
                self.frame = 0
            else:
                self.frame += 1
            self.timer = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, controls, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.gigapower = False
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.flag_damage2 = False
        self.frame = 0
        self.timer_anime = 0
        self.image_lists = image_lists
        self.image = self.image_lists[0][0]
        self.current_list_image = self.image_lists[0]
        self.rect = self.image.get_rect()

        self.dir = "right"
        self.hp = 100

        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []

        if controls == 1:
            self.controls = [
                pygame.K_d,
                pygame.K_a,
                pygame.K_e,
                pygame.K_SPACE,
                pygame.K_q,]
            self.rect.center = (200, 380)
            self.hp_bar = 'blue'

        else:
            self.controls = [
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RETURN,
                pygame.K_KP0,
                pygame.K_LCTRL
            ]
            self.rect.center = (800, 380)
            self.hp_bar = "red"

    def update(self, enemy):
        global lvl
        if self.rect.center[0] - enemy.rect.center[0] < 0:
            self.dir = "right"
        else:
            self.dir = "left"
        key = pygame.key.get_pressed()

        if key[self.controls[0]]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        elif key[self.controls[1]]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        else:
            if not self.anime_atk and not self.gigapower:
                self.anime_idle = True
            self.anime_run = False

        if key[self.controls[3]]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

        if key[self.controls[2]] and not self.anime_atk:
            self.frame = 0
            self.anime_atk = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True
        self.timer_anime += 2

        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.gigapower:
                    self.current_list_image = player1_idle
                    self.gigapower = False
                    self.anime_idle = True
                if self.anime_atk:
                    self.current_list_image = player1_idle
                    self.anime_atk = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0

        print(self.anime_atk,self.anime_idle,self.anime_run,self.gigapower)
        if key[self.controls[4]] and not self.gigapower:
            self.frame = 0
            self.anime_atk = False
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = False
            self.flag_damage2 =True
            self.gigapower = True
        self.timer_anime += 2


        if self.anime_idle:
            self.current_list_image = self.image_lists[0]
        elif self.anime_run:
            self.current_list_image = self.image_lists[1]
        elif self.anime_atk:
            self.current_list_image = self.image_lists[2]
        elif self.gigapower:
            self.current_list_image = self.image_lists[3]
        try:
            if self.dir == "right":
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(
                    self.current_list_image[self.frame], True, False
                )
        except:
            self.frame = 0

        if self.hp_bar == "red":
            pygame.draw.rect(sc, self.hp_bar, (600 + (600 - self.hp * 6), 0, 600, 50))
        else:
            pygame.draw.rect(sc, self.hp_bar, (0, 0, 600 * self.hp / 100, 50))

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []

        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        if len(set(self.mask_list) & set(enemy.mask_list)) > 0:
            if self.gigapower == True and self.flag_damage2 == True:
                enemy.hp -= 50

                self.flag_damage = False
            if self.anime_atk and self.flag_damage:
                enemy.hp -= 10
                self.flag_damage = False
        if self.hp <= 0:
            lvl = 'win'



def restart():
    global player_1, player_1_group, player_2, player_2_group, fon
    player_1_group = pygame.sprite.Group()
    player_1 = Player(1, (player1_idle, player1_run, player1_attack,player1_attack2))
    player_1_group.add(player_1)
    player_2_group = pygame.sprite.Group()
    player_2 = Player(2, (player2_idle, player2_run, player2_attack,player2_attack))
    player_2_group.add(player_2)
    fon = FOТ()


def game():
    fon.update()
    player_1_group.update(player_2)
    player_1_group.draw(sc)
    player_2_group.update(player_1)
    player_2_group.draw(sc)

    pygame.display.update()


restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl == 'game':
        game()
    elif lvl == "menu":
        startMenu()
    elif lvl == 'win':
        timer += 1
        if timer / FPS >5 and lvl != "menu":
            lvl = "menu"
            restart()
            timer = 0
        if player_1.hp <= 0:
            sc.blit(win2_image , (0,0))
        else:
            sc.fill("black")
            sc.blit(win1_image , (350,200))
        pygame.display.update()

    clock.tick(FPS)