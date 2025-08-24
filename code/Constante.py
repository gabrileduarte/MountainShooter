import pygame

# C
COLOR_YELLOW = 255, 215, 0
COLOR_RED = 255, 0, 0
COLOR_WHITE = 255, 255, 255

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 3,
    'Level1Bg2': 5,
    'Level1Bg3': 9,
    'Level1Bg4': 11,
    'Level1Bg5': 13,
    'Level1Bg6': 15,
    'Level1Bg7': 17,
    'Player1':6,
    'Player1Shot': 10,
    'Player2':6,
    'Player2Shot': 10,
    'Enemy1':5,
    'Enemy1Shot': 10,
    'Enemy2':3,
    'Enemy2Shot': 6,
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}
ENTITY_SHOT_DELAY = {
    'Player1': 15,
    'Player2': 15,
    'Enemy1': 35,
    'Enemy2': 45,

}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                    'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                    'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_SPACE}

# S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 1280 # De acordo com a pep usa-se letras maiusculas
WIN_HEIGHT = 720
