from environment import *
from costanti import *
import sys
import pygame
import numpy as np
import random
import ludo_env
import costanti


def table(finestra):
    # Pulisci la finestra
    finestra.fill(colore_sfondo)
    # Disegna la tabella
    disegna_tabella(finestra, dimensione_cella, spessore_bordo)


def draw_dice(dado, finestra, turno_player_red):
    # Draw the dice
    pygame.draw.rect(finestra, dado.color, (
        dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella),
                     0)
    pygame.draw.rect(finestra, (0, 0, 0), (
        dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella),
                     spessore_bordo)

    # Disegna il numero del dado
    number_color = (255, 0, 0) if turno_player_red else (0, 255, 0)
    number = pygame.font.SysFont(None, 30).render(str(dado.value), True, number_color)
    number_rect = number.get_rect(center=(dado.position[1] * dimensione_cella + dimensione_cella // 2,
                                          dado.position[0] * dimensione_cella + dimensione_cella // 2))
    finestra.blit(number, number_rect)


def draw_tokens(finestra, framerate):
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
    framerate.tick(120)



def choose_action(state):
    if np.random.rand() < exploration_prob:
        return np.random.randint(0, 1)  # Esplorazione casuale
    else:
        return np.argmax(Q[state, :])  # Sfruttamento della conoscenza


def update_observation(observ):
    if (tokens[0].count < tokens[2].count) or (tokens[0].count < tokens[3].count):
        observ['passed 1'] = 1
    elif (tokens[1].count < tokens[2].count) or (tokens[1].count < tokens[3].count):
        observ['passed 2'] = 1
    value = tuple(observ.values())
    return lista_stati.index(value)


def episode_train(num):
    global new_state
    pygame.init()
    framerate = pygame.time.Clock()
    env = ludo_env.ludo_env()
    dado = Dice((0, 0, 0), (7, 7), 30)
    # Inizializza la finestra
    finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
    pygame.display.set_caption("Tabella Ludo")

    total_reward = 0

    for episode in range(num):
        end = False
        current_state = 30  #np.random.randint(0, 34)
        dado.roll

        while not end:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            table(finestra)
            turno_player_red = True
            draw_dice(dado, finestra, turno_player_red)
            #Turno agente
            action = choose_action(current_state)
            dado, observ, consecutive_sixes, end = env.step(action, dado, 0, 'red')
            reward = rewards[current_state, action]
            total_reward += reward
            draw_tokens(finestra, framerate)

            #Nuovo turno agente se esce 6
            if consecutive_sixes > 0 and end is False:
                for consecutive_sixes in range(4):
                    new_state = update_observation(observ)
                    updateQ(current_state, action, reward, new_state)

                    table(finestra)
                    draw_dice(dado, finestra, turno_player_red)

                    action = choose_action(new_state)
                    dado, observ, consecutive_sixes, end = env.step(action, dado, consecutive_sixes, 'red')
                    reward = rewards[current_state, action]
                    total_reward += reward

                    new_state = update_observation(observ)
                    draw_tokens(finestra, framerate)

                    updateQ(current_state, action, reward, new_state)
                    if consecutive_sixes == 0 or end is True:
                        break

            if not end:
                #Turno cpu randomica
                turno_player_red = False
                draw_dice(dado, finestra, turno_player_red)
                dado, observ_cpu, consecutive_sixes, end = env.step(random.randint(0, 1), dado, 0, 'green')
                draw_tokens(finestra, framerate)

                # Nuovo turno cpu se esce 6
                if consecutive_sixes > 0 and end is False:
                    for consecutive_sixes in range(3):
                        new_state = update_observation(observ)
                        table(finestra)
                        draw_dice(dado, finestra, turno_player_red)
                        dado, observ_cpu, consecutive_sixes, end = env.step(random.randint(0, 1), dado, consecutive_sixes, 'green')
                        new_state = update_observation(observ)
                        draw_tokens(finestra, framerate)
                        if consecutive_sixes == 0 or end is True:
                            break
                else:
                    new_state = update_observation(observ)

            updateQ(current_state, action, reward, new_state)
            current_state = new_state

        print(f"episodio {episode}: {total_reward}")
        print(f"Vittorie agente: {costanti.red_wins} - Vittorie cpu: {costanti.green_wins}")
        env.reset()



def updateQ(current_state, action, reward, new_state):
    # Aggiornamento della matrice Q con l'algoritmo Q-learning
    Q[current_state, action] = (1 - learning_rate) * Q[current_state, action] + \
                               learning_rate * (reward + discount_factor * np.max(Q[new_state, :]))


rewards = np.array([
    [1, 1],
    [0.5, 0.5],
    [0.6, 0],
    [0, 0.6],
    [0.5, 0.5],
    [0.6, 0.3],
    [0.3, 0.6],
    [0.5, 0.5],
    [0.5, 0.5],
    [0, 0.6],
    [0.6, 0],
    [0.5, 0.5],
    [0.7, 0.3],
    [0.3, 0.7],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.6, 0.2],
    [0.2, 0.6],
    [0.5, 0.5],
    [0.6, 0.6],
    [0, 0.6],
    [0.5, 0.5],
    [0.5, 0.3],
    [0.3, 0.5],
    [0.5, 0.5],
    [0.5, 0.5],
    [0.4, 0.5],
    [0.5, 0.4],
    [0.3, 0.6],
    [0.5, 0.5],
    [0.5, 0.7],
    [0.7, 0.5],
    [0.6, 0.6]
])

lista_stati = [
    (0, 0, 0, 2, 0, 0), (0, 0, 1, 1, 0, 0), (0, 0, 1, 1, 0, 1), (0, 0, 1, 1, 1, 0),
    (0, 0, 2, 0, 0, 0), (0, 0, 2, 0, 0, 1), (0, 0, 2, 0, 1, 0), (0, 0, 2, 0, 1, 1),
    (0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 1, 0), (0, 1, 0, 1, 0, 1), (0, 1, 1, 0, 0, 0),
    (0, 1, 1, 0, 0, 1), (0, 1, 1, 0, 1, 0), (0, 1, 1, 0, 1, 1), (0, 2, 0, 0, 0, 0),
    (0, 2, 0, 0, 1, 0), (0, 2, 0, 0, 0, 1), (0, 2, 0, 0, 1, 1), (1, 0, 0, 1, 0, 0),
    (1, 0, 0, 1, 0, 1), (1, 0, 0, 1, 1, 0), (1, 0, 1, 0, 0, 0), (1, 0, 1, 0, 0, 1),
    (1, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 1), (1, 1, 0, 0, 0, 0), (1, 1, 0, 0, 0, 1),
    (1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 1), (2, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 1),
    (2, 0, 0, 0, 1, 0), (2, 0, 0, 0, 1, 1)
]

# Parametri dell'algoritmo Q-learning
learning_rate = 0.8
discount_factor = 0.95
exploration_prob = 0.2
num_episodes = 1000

# Inizializzazione della matrice Q con valori casuali
Q = np.random.rand(34, 2)



if __name__ == '__main__':
    episode_train(1000)




