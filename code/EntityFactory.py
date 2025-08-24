import random

from code.Background import Background
from code.Constante import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Faz o fundo passar eternamente
                for i in range(8):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2.5 - 70)) # Define a posição que o player1 vai iniciar na tela (no meio da tela)
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2.5 + 70)) # Define a posição que o player1 vai iniciar na tela (no meio da tela)
            case 'Enemy1':
                enemy = Enemy('Enemy1', (0, 0))
                x = WIN_WIDTH + 10
                y = random.randint(0, WIN_HEIGHT - enemy.rect.height)
                enemy.rect.topleft = (x, y)
                return enemy
            case 'Enemy2':
                enemy = Enemy('Enemy2', (0, 0))
                x = WIN_WIDTH + 10
                y = random.randint(0, WIN_HEIGHT - enemy.rect.height)
                enemy.rect.topleft = (x, y)
                return enemy


