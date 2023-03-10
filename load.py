import pygame.image

start_image = pygame.image.load('image/fon/start (1).png').convert_alpha()
exit_image = pygame.image.load('image/fon/exit (1).png').convert_alpha()
menu_image = pygame.image.load('image/fon/fon.png').convert_alpha()
win1_image = pygame.image.load('image/fon/win1.png').convert_alpha()
win2_image = pygame.image.load('image/fon/win2.png').convert_alpha()

player1_idle = [
           pygame.image.load('image/player 1/idle/1.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/2.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/3.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/4.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/5.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/6.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/7.png').convert_alpha(),
           pygame.image.load('image/player 1/idle/8.png').convert_alpha()
]
player1_run = [
           pygame.image.load('image/player 1/run/1.png').convert_alpha(),
           pygame.image.load('image/player 1/run/2.png').convert_alpha(),
           pygame.image.load('image/player 1/run/3.png').convert_alpha(),
           pygame.image.load('image/player 1/run/4.png').convert_alpha(),
           pygame.image.load('image/player 1/run/5.png').convert_alpha(),
           pygame.image.load('image/player 1/run/6.png').convert_alpha(),
           pygame.image.load('image/player 1/run/7.png').convert_alpha(),
           pygame.image.load('image/player 1/run/8.png').convert_alpha()
]
player1_attack = [
           pygame.image.load('image/player 1/attack/1.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/2.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/3.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/4.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/5.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/6.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/7.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/8.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/9.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/10.png').convert_alpha(),
           pygame.image.load('image/player 1/attack/11.png').convert_alpha(),
]
player1_attack2 = [
           pygame.image.load('image/player 1/attack 2/1.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/2.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/3.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/4.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/5.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/6.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/7.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/8.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/9.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/10.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/11.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/12.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/13.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/14.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/15.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/16.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/17.png').convert_alpha(),
           pygame.image.load('image/player 1/attack 2/18.png').convert_alpha(),
]
player2_idle = [
           pygame.image.load('image/player 2/idle/1.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/2.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/3.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/4.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/5.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/6.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/7.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/8.png').convert_alpha(),
           pygame.image.load('image/player 2/idle/9.png').convert_alpha()
]
player2_run = [
           pygame.image.load('image/player 2/run/1.png').convert_alpha(),
           pygame.image.load('image/player 2/run/2.png').convert_alpha(),
           pygame.image.load('image/player 2/run/3.png').convert_alpha(),
           pygame.image.load('image/player 2/run/4.png').convert_alpha(),
           pygame.image.load('image/player 2/run/5.png').convert_alpha(),
           pygame.image.load('image/player 2/run/6.png').convert_alpha(),

]
player2_attack = [
           pygame.image.load('image/player 2/attack/1.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/2.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/3.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/4.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/5.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/6.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/7.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/8.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/9.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/10.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/11.png').convert_alpha(),
           pygame.image.load('image/player 2/attack/12.png').convert_alpha()
]

fon_image = [pygame.image.load('image/fon/1.jpg').convert_alpha(),
             pygame.image.load('image/fon/2.jpg').convert_alpha(),
             pygame.image.load('image/fon/3.jpg').convert_alpha(),
             pygame.image.load('image/fon/4.jpg').convert_alpha(),
             pygame.image.load('image/fon/5.jpg').convert_alpha(),
             pygame.image.load('image/fon/6.jpg').convert_alpha(),
             pygame.image.load('image/fon/7.jpg').convert_alpha(),
             pygame.image.load('image/fon/8.jpg').convert_alpha(),
             ]

player3_idle = [pygame.image.load('image/player 3/01_idle/idle_1.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_2.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_3.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_4.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_5.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_6.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_7.png').convert_alpha(),
                pygame.image.load('image/player 3/01_idle/idle_8.png').convert_alpha(),
                ]

player3_attack=[pygame.image.load('image/player 3/07_1_atk/1_atk_1.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_2.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_3.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_4.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_5.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_6.png').convert_alpha(),
                pygame.image.load('image/player 3/07_1_atk/1_atk_7.png').convert_alpha(),
                ]

player3_run  = [pygame.image.load('image/player 3/02_walk/walk_1.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_2.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_3.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_4.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_5.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_6.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_7.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_8.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_9.png').convert_alpha(),
                pygame.image.load('image/player 3/02_walk/walk_10.png').convert_alpha(),
                ]