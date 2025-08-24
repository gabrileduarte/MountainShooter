import pygame

from code.Constante import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.Playershot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] # Adiciona um delay  ao manter pressionado a tecla de tiro

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: # SOBE o player enquanto estiver pressionando UP e para ao chegar no topo
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # DESCE o player enquanto estiver pressionando DOWN e para ao chegar no FIM da tela
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Move para tras
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Move para frente
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
           self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Adiciona um delay ao manter pressionado a tecla de tiro
           pressed_key = pygame.key.get_pressed()
           if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
