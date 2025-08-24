from abc import ABC, abstractmethod

import pygame.image

from code.Constante import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple): # Define os atributos das entidades NOME, IMAGEM, VELOCIDADE, VIDA
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() # Convert Alpha trata a imagem PNG de uma maneira mais otimizada
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod # decorator
    def move(self, ):
        pass