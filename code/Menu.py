from pygame.font import Font
import pygame.image
from pygame import Surface, Rect

from code.Constante import WIN_WIDTH, C_YELLOW, C_RED, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/fundo.png').convert_alpha()  # Carrega a imagem e Defini a imagem de fundo
        self.rect = self.surf.get_rect(left=0, top=0)  # Cria o retangulo iniciando no cando superior esquerdo

    def run(self, ):
        menu_option = 0 # Inicia o menu na primeira opção
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenha as imagens
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem
            self.menu_text(80, 'BURNING', C_RED, ((WIN_WIDTH / 2), 70), border_size=4)  # Escreve o texto
            self.menu_text(80, 'DRAGON', C_YELLOW, ((WIN_WIDTH / 2), 150), border_size=4)  # Escreve o texto
            self.menu_text(15, 'PRESS ENTER TO CONFIRM', C_YELLOW, ((WIN_WIDTH / 2), 650), border_size=2)  # Escreve o texto

            # Controle de piscar (blink) a cada 500ms
            time_now = pygame.time.get_ticks()
            blink = (time_now // 400) % 2 == 0  # alterna entre True/False a cada 0,5s

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    if blink:
                        self.menu_text(30, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 400 + 45 * i))  # Escreve o texto # Quando o cursos estiver sobre uma opção ficar de cor diferente
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 400 + 45 * i))  # Escreve o texto do menu
            pygame.display.flip()

            # Evento de fechar a janela
            for event in pygame.event.get():  # Pega os eventos e checa os eventos com a variavel event
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # Encerra o pygame

                    # EVENTOS PARA NAVEGAR PELO MENU
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Se a tecla direcinal for precionada para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # Se a tecla direcinal for precionada  para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # Ao apertar enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple,
                  border_color: object = (0, 0, 0),
                  border_size: object = 3) -> None:
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size,
                                              bold=True)  # Diz qual fonte vou usar
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()  # Renderiza e cria uma imagem a partir do texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Renderiza a borda (texto preto deslocado em várias direções)
        border_color = (0, 0, 0)
        offsets = [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]

        # Renderiza a borda (texto deslocado em várias direções)
        for ox in range(-border_size, border_size + 1):
            for oy in range(-border_size, border_size + 1):
                if ox == 0 and oy == 0:  # evita desenhar no meio
                    continue
                border_surf = text_font.render(text, True, border_color).convert_alpha()
                border_rect = border_surf.get_rect(center=(text_center_pos[0] + ox, text_center_pos[1] + oy))
                self.window.blit(border_surf, border_rect)
        self.window.blit(source=text_surf, dest=text_rect)
