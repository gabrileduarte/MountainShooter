import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init() # Inicializa o pygame
        self.window = pygame.display.set_mode(size=(1280, 720))  # Cia uma variavel para inicializar a janela, define o tamanho da janela em tupla(entre parenteses)

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # # Check for all events
            # for event in pygame.event.get():  # Pega os eventos e checa os eventos com a variavel event
            #     if event.type == pygame.QUIT:
            #         print('Quitting')
            #         pygame.quit()  # Close Window
            #         quit()  # Encerra o pygame


