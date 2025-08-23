import sys
import pygame.display
import pygame

from xml.dom.minidom import Entity
from pygame.font import Font
from pygame import Surface, Rect

from code.Constante import COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactore


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode  = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactore.get_entity('Level1Bg'))

    def run(self, ):
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1) # Faz a música tocar enquanto estiver jogando
        clock = pygame.time.Clock() # Utilizado para definir a taxa de quandros FPS
        while True:
            clock.tick(60) # Definir a taxa de quadros
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():  # Pega os eventos e checa os eventos com a variavel event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #

            self.level_text(14, f'{self.name} - TIMEOUT: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5)) # MOstra o tempo de duração do level
            self.level_text(14, f'FPS:{clock.get_fps() : .0f}', COLOR_WHITE, (10,WIN_HEIGHT - 35)) # Mostra o FPS na tela
            self.level_text(14, f'ENTIDADES: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20)) # Mostra o numero de entidades na tela
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
