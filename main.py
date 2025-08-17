import pygame

print('Setup Start')
pygame.init() # Inicializa o pygame
window = pygame.display.set_mode(size=(1280, 720))  # Cia uma variavel para inicializar a janela, define o tamanho da janela em tupla(entre parenteses)
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():  # Pega os eventos e checa os eventos com a variavel event
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # Encerra o pygame
