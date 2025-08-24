from code.Constante import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.EmenyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] # Adiciona um delay  ao manter pressionado a tecla de tiro

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
           self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Adiciona um delay ao manter pressionado a tecla de tiro
           return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

