import pygame

from code.Constante import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION  # Importa as duas constantes do arquivo contante.py
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init() # Inicializa o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Cia uma variavel para inicializar a janela, define o tamanho da janela em tupla(entre parenteses)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in  [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: # seleciona a opção NEW GAME 1P ou NEW GAME 2P
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if menu_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]: # seleiona a opção exit
                pygame.quit()
                quit() # fecha o game
            else:
                pass





