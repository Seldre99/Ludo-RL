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
tokens = [Token((139,0,0), (2, 2), dimensione_cella),
          Token((0, 100, 0), (12, 2), dimensione_cella),
          Token((173, 216, 230), (2, 12), dimensione_cella),
          Token((184, 134, 11), (12, 12), dimensione_cella)]

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
        center_x = x * dimensione_cella + dimensione_cella // 2
        center_y = y * dimensione_cella + dimensione_cella // 2
        pygame.draw.circle(finestra, token.color, (center_x, center_y), token.size)

    # Aggiorna la finestra
    pygame.display.flip()
