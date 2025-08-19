import pygame

from code.Constante import WIN_WIDTH, WIN_HEIGHT # Importa as duas constantes do arquivo contante.py
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init() # Inicializa o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Cia uma variavel para inicializar a janela, define o tamanho da janela em tupla(entre parenteses)

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass



