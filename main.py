import pygame
import sys
from pedina import Token
from environment import disegna_tabella, Dice
import time

# Inizializza Pygame
pygame.init()

# Definisci le dimensioni della finestra e altri parametri
larghezza_finestra = 600
altezza_finestra = 600
colore_sfondo = (255, 255, 255)
dimensione_cella = larghezza_finestra // 15  # 15 caselle in una riga
spessore_bordo = 1
phase = "red"
turno_player_red = True
tempo_limite = 30
tempo_iniziale = time.time()
green_safe_zone = [(6,7), (5,7), (4,7), (3,7), (2,7), (1,7)]
red_safe_zone = [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1)]

####### TOKENS ########
# Create four tokens
tokens = [Token((139,0,0), (2, 2), 1, dimensione_cella),
          Token((139,0,0), (2, 3), 2, dimensione_cella),
          Token((0, 100, 0), (2, 11), 1, dimensione_cella),
          Token((0, 100, 0), (2, 12), 2, dimensione_cella)]

dado = Dice((0, 0, 0), (7, 7), 30)
# Inizializza la finestra
finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
pygame.display.set_caption("Tabella Ludo")


# Scelta del token da spostare
def turn(phase, tok):
    if phase == "red" and tok == 1:
        if tokens[0].position == (2, 2) and dado.value == 6:
            tokens[0].position = (6, 2)
        elif tokens[0].position != (2, 2):
            new_position = tokens[0].move(dado.value)
            # Verifica se la nuova posizione è nella zona avversaria e se ci sono pedine avversarie nella stessa posizione
            if new_position != (2, 2) and new_position == tokens[2].position:
                # Ritorna alla posizione iniziale
                print('tokens[2] è stato preso')
                tokens[2].position = (2, 11)
            elif new_position != (2, 2) and new_position == tokens[3].position:
                print('tokens[3] è stato preso')
                tokens[3].position = (2, 12)
    elif phase == "red" and tok == 2:
        if tokens[1].position == (2, 3) and dado.value == 6:
            tokens[1].position = (6, 2)
        elif tokens[1].position != (2, 3):
            new_position = tokens[1].move(dado.value)
            if new_position != (2, 3) and new_position == tokens[2].position:
                # Ritorna alla posizione iniziale
                print('tokens[2] è stato preso')
                tokens[2].position = (2, 11)
            elif new_position != (2, 3) and new_position == tokens[3].position:
                print( 'tokens[3] è stato preso')
                tokens[3].position = (2, 12)

    elif phase == "green" and tok == 1:
        if tokens[2].position == (2, 11) and dado.value == 6:
            tokens[2].position = (2, 8)
        elif tokens[2].position != (2, 11):
            new_position = tokens[2].move(dado.value)
            if new_position != (2, 11) and new_position == tokens[0].position:
                # Ritorna alla posizione iniziale
                print('tokens[0] è stato preso')
                tokens[0].position = (2, 2)
            elif new_position != (2, 11) and new_position == tokens[1].position:
                print('tokens[1] è stato preso')
                tokens[1].position = (2, 3)

    elif phase == "green" and tok == 2:
        if tokens[3].position == (2, 12) and dado.value == 6:
            tokens[3].position = (2, 8)
        elif tokens[3].position != (2, 12):
            new_position = tokens[3].move(dado.value)
            if new_position != (2, 12) and new_position == tokens[0].position:
                # Ritorna alla posizione iniziale
                print('tokens[0] è stato preso')
                tokens[0].position = (2, 2)
            elif new_position != (2, 12) and new_position == tokens[1].position:
                print('tokens[1] è stato preso')
                tokens[1].position = (2, 3)

    return dado

# Ciclo principale
while True:

    tempo_trascorso = time.time() - tempo_iniziale
    if tempo_trascorso > tempo_limite:
        print("Tempo scaduto! Riprova.")
        dado.roll()
        tempo_iniziale = time.time()

    # Pulisci la finestra
    finestra.fill(colore_sfondo)

    # Disegna la tabella
    disegna_tabella(finestra, dimensione_cella, spessore_bordo)

    # Draw the dice
    pygame.draw.rect(finestra, dado.color, (
    dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella), 0)
    pygame.draw.rect(finestra, (0, 0, 0), (
    dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella),
                     spessore_bordo)
    if phase == "green":
        number = pygame.font.SysFont(None, 30).render(str(dado.value), True, (255, 0, 0))
    else:
        number = pygame.font.SysFont(None, 30).render(str(dado.value), True, (0, 255, 0))
    number_rect = number.get_rect(center=(dado.position[1] * dimensione_cella + dimensione_cella // 2,
                                          dado.position[0] * dimensione_cella + dimensione_cella // 2))
    finestra.blit(number, number_rect)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w or evento.key == pygame.K_e:
                tok = 1 if evento.key == pygame.K_w else 2
                phase = "red" if turno_player_red else "green"
                dado = turn(phase, tok)
                turno_player_red = not turno_player_red
                dado.roll()
                tempo_iniziale = time.time()
            '''
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
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    dado.roll()
                    print(f'Dice Rolled. Value: {dado.value}')
            '''

    # Disegna i tokens
    for token in tokens:
        x, y = token.position
        center_x = y * dimensione_cella + dimensione_cella // 2
        center_y = x * dimensione_cella + dimensione_cella // 2
        pygame.draw.circle(finestra, token.color, (center_x, center_y), token.size)
        number = pygame.font.SysFont(None, 30).render(str(token.number), True, (0, 0, 0))
        number_rect = number.get_rect(center=(center_x, center_y))
        finestra.blit(number, number_rect)

    # Aggiorna la finestra
    pygame.display.flip()
