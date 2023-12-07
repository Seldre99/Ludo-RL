import pygame
import sys
from pedina import Token
from environment import disegna_tabella

# Inizializza Pygame
pygame.init()

# Definisci le dimensioni della finestra e altri parametri
larghezza_finestra = 600
altezza_finestra = 600
colore_sfondo = (255, 255, 255)
dimensione_cella = larghezza_finestra // 15  # 15 caselle in una riga
spessore_bordo = 1

####### TOKENS ########
# Create four tokens
tokens = [Token((139,0,0), (2, 2), 1, dimensione_cella),
          Token((139,0,0), (2, 3), 2, dimensione_cella),
          Token((139,0,0), (3, 2), 3, dimensione_cella),
          Token((139,0,0), (3, 3), 4, dimensione_cella),
          Token((173, 216, 230), (11, 2), 1, dimensione_cella),
          Token((173, 216, 230), (11, 3), 2, dimensione_cella),
          Token((173, 216, 230), (12, 2), 3, dimensione_cella),
          Token((173, 216, 230), (12, 3), 4, dimensione_cella),
          Token((0, 100, 0), (2, 11), 1, dimensione_cella),
          Token((0, 100, 0), (2, 12), 2, dimensione_cella),
          Token((0, 100, 0), (3, 11), 3, dimensione_cella),
          Token((0, 100, 0), (3, 12), 4, dimensione_cella),
          Token((184, 134, 11), (11, 11), 1, dimensione_cella),
          Token((184, 134, 11), (11, 12), 2, dimensione_cella),
          Token((184, 134, 11), (12, 11), 3, dimensione_cella),
          Token((184, 134, 11), (12, 12), 4, dimensione_cella),]

# Inizializza la finestra
finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Tabella Ludo")

# Ciclo principale
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            # Check arrow keys for movement
            if evento.key == pygame.K_UP:
                current_pos, previous_pos = tokens[0].move('UP')
                print(f'Moved UP. Current Position: {current_pos}, Previous Position: {previous_pos}')
            elif evento.key == pygame.K_DOWN:
                current_pos, previous_pos = tokens[0].move('DOWN')
                print(f'Moved DOWN. Current Position: {current_pos}, Previous Position: {previous_pos}')
            elif evento.key == pygame.K_LEFT:
                current_pos, previous_pos = tokens[0].move('LEFT')
                print(f'Moved LEFT. Current Position: {current_pos}, Previous Position: {previous_pos}')
            elif evento.key == pygame.K_RIGHT:
                current_pos, previous_pos = tokens[0].move('RIGHT')
                print(f'Moved RIGHT. Current Position: {current_pos}, Previous Position: {previous_pos}')


    # Pulisci la finestra
    finestra.fill(colore_sfondo)

    # Disegna la tabella
    disegna_tabella(finestra, dimensione_cella, spessore_bordo)

    # Disegna i tokens
    for token in tokens:
        x, y = token.position
        center_x = y * dimensione_cella + dimensione_cella // 2
        center_y = x * dimensione_cella + dimensione_cella // 2
        pygame.draw.circle(finestra, token.color, (center_x, center_y), token.size)
        number = pygame.font.SysFont(None, 30).render(str(token.number), True, (0,0,0))
        number_rect = number.get_rect(center=(center_x, center_y))
        finestra.blit(number, number_rect)

    # Aggiorna la finestra
    pygame.display.flip()
