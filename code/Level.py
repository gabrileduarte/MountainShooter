import random
import sys
from random import choice

import pygame.display
import pygame

from pygame.font import Font
from pygame import Surface, Rect

from code.Constante import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_ORANGE, C_BLACK
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000 # Tempo informado sempre em milisegundos
        self.window = window
        self.name = name
        self.game_mode  = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # Inicializa o background
        self.entity_list.append(EntityFactory.get_entity('Player1')) # Inicializa o player1
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # Inicializa o player1
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # Define o tempo de surgimento dos inimigos

    def run(self, ):
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1) # Faz a música tocar enquanto estiver jogando
        clock = pygame.time.Clock() # Utilizado para definir a taxa de quandros FPS
        while True:
            clock.tick(60) # Definir a taxa de quadros
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent,(Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:{ent.health} | Score: {ent.score}', C_ORANGE, (10,25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health:{ent.health} | Score: {ent.score}', C_BLACK, (10,45))
            for event in pygame.event.get():  # Pega os eventos e checa os eventos com a variavel event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - TIMEOUT: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5)) # MOstra o tempo de duração do level
            self.level_text(14, f'FPS:{clock.get_fps() : .0f}', C_WHITE, (10, WIN_HEIGHT - 35)) # Mostra o FPS na tela
            self.level_text(14, f'ENTIDADES: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20)) # Mostra o numero de entidades na tela
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
