from environment import *
from costanti import *
import sys
import pygame
import numpy as np
import random
import ludo_env
import costanti
import matplotlib.pyplot as plt
import pickle


def table(finestra):
    # Clean window
    finestra.fill(colore_sfondo)
    # Draw the table
    disegna_tabella(finestra, dimensione_cella, spessore_bordo)


def draw_dice(dado, finestra, turno_player_red):
    # Draw the dice
    pygame.draw.rect(finestra, dado.color, (
        dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella),
                     0)
    pygame.draw.rect(finestra, (0, 0, 0), (
        dado.position[1] * dimensione_cella, dado.position[0] * dimensione_cella, dimensione_cella, dimensione_cella),
                     spessore_bordo)

    # Draw the number of the dice
    number_color = (255, 0, 0) if turno_player_red else (0, 255, 0)
    number = pygame.font.SysFont(None, 30).render(str(dado.value), True, number_color)
    number_rect = number.get_rect(center=(dado.position[1] * dimensione_cella + dimensione_cella // 2,
                                          dado.position[0] * dimensione_cella + dimensione_cella // 2))
    finestra.blit(number, number_rect)


def draw_tokens(finestra, framerate):
    # Draw tokens
    for token in tokens:
        x, y = token.position
        center_x = y * dimensione_cella + dimensione_cella // 2
        center_y = x * dimensione_cella + dimensione_cella // 2
        pygame.draw.circle(finestra, token.color, (center_x, center_y), token.size)
        number = pygame.font.SysFont(None, 30).render(str(token.number), True, (0, 0, 0))
        number_rect = number.get_rect(center=(center_x, center_y))
        finestra.blit(number, number_rect)

    # Update window
    pygame.display.flip()
    framerate.tick(120)


def choose_action(state):
    if np.random.rand() < exploration_prob:
        return np.random.randint(0, 1)  # Random exploration
    else:
        return np.argmax(Q[state, :])  # Knowledge exploitation


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
    # Initialize window
    finestra = pygame.display.set_mode((larghezza_finestra, altezza_finestra))
    pygame.display.set_caption("Tabella Ludo")

    total_reward = 0

    agent_wins = []
    cpu_wins = []
    total_rewards = []

    plt.ion()
    fig, ax = plt.subplots()

    for episode in range(num):
        end = False
        current_state = 30
        dado.roll

        while not end:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            table(finestra)
            turno_player_red = True
            draw_dice(dado, finestra, turno_player_red)
            # Agent's turn
            if current_state in range(1, 4) or current_state in range(8, 11) or current_state in range(19, 22):
                # Management for states where one token is in the GOAL and consequently the only action available
                # is the movement of only the other one
                if tokens[0].position == (7, 6):
                    action = 1
                else:
                    action = 0
            else:
                action = choose_action(current_state)
            dado, observ, consecutive_sixes, end = env.step(action, dado, 0, 'red')
            reward = rewards[current_state, action]
            total_reward += reward
            draw_tokens(finestra, framerate)

            # New agent's turn if 6 comes out
            if consecutive_sixes > 0 and end is False:
                for consecutive_sixes in range(4):
                    new_state = update_observation(observ)
                    new_action = choose_action(new_state)

                    updateQ(current_state, action, reward, new_state, new_action)

                    table(finestra)
                    draw_dice(dado, finestra, turno_player_red)

                    if new_state in range(1, 4) or new_state in range(8, 11) or new_state in range(19, 22):
                        if tokens[0].position == (7, 6):
                            action = 1
                        else:
                            action = 0
                    else:
                        action = new_action

                    dado, observ, consecutive_sixes, end = env.step(action, dado, consecutive_sixes, 'red')
                    reward = rewards[new_state, action]
                    total_reward += reward

                    new_state_2 = update_observation(observ)
                    draw_tokens(finestra, framerate)

                    updateQ(new_state, action, reward, new_state_2, new_action)
                    current_state = new_state_2
                    if consecutive_sixes == 0 or end is True:
                        break

            if not end:
                # Random cpu turn
                turno_player_red = False
                draw_dice(dado, finestra, turno_player_red)
                dado, observ_cpu, consecutive_sixes, end = env.step(random.randint(0, 1), dado, 0, 'green')
                draw_tokens(finestra, framerate)

                # New cpu turn if 6 comes out
                if consecutive_sixes > 0 and end is False:
                    for consecutive_sixes in range(3):
                        new_state = update_observation(observ)
                        table(finestra)
                        draw_dice(dado, finestra, turno_player_red)
                        dado, observ_cpu, consecutive_sixes, end = env.step(random.randint(0, 1), dado,
                                                                            consecutive_sixes, 'green')
                        new_state = update_observation(observ)
                        draw_tokens(finestra, framerate)
                        if consecutive_sixes == 0 or end is True:
                            break
                else:
                    new_state = update_observation(observ)

            updateQ(current_state, action, reward, new_state, choose_action(new_state))
            current_state = new_state

        print(f"episodio {episode}: {total_reward}")
        print(f"Vittorie agente: {costanti.red_wins} - Vittorie cpu: {costanti.green_wins}")
        agent_wins.append(costanti.red_wins)
        cpu_wins.append(costanti.green_wins)
        total_rewards.append(total_reward)

        # Update the plots
        ax.clear()
        ax.plot(agent_wins, label='Agent Wins', color='red')
        ax.plot(cpu_wins, label='CPU Wins', color='green')
        ax.set_title('Wins Over Episodes')
        ax.set_xlabel('Episode')
        ax.set_ylabel('Total Wins')
        ax.legend()

        # Pause to allow the plot to update
        plt.pause(0.1)
        env.reset()
    plt.savefig('wins_plot_test4_sarsa.png')
    plt.ioff()
    plt.show()


def updateQ(current_state, action, reward, new_state, new_action):
    # Q-matrix update with the Sarsa algorithm
    Q[current_state, action] = Q[current_state, action] + learning_rate * (
            reward + discount_factor * Q[new_state, new_action] - Q[current_state, action])


rewards = np.array([
                     [5, 5],
                     [0.2, 0.2], [0, 0.3], [0.3, 0],
                     [0.2, 0.2], [-0.9, 0.5], [0.5, -0.9], [0.2, 0.2],
                     [0, 0], [0.2, 0], [0, 0.2],
                     [0.2, 0.2], [-0.9, 0.5], [0.5, -0.5], [0.2, 0.2],
                     [0.3, 0.3], [0.5, -0.9], [-0.9, 0.5], [0.2, 0.2],
                     [0, 0], [-0.9, 0.5], [0.5, -0.9],
                     [0, 0], [-0.9, 0.5], [0.5, -0.9], [0.2, 0.2],
                     [0.2, 0.2], [-0.7, 0.4], [0.4, -0.7], [0.2, 0.2],
                     [0.3, 0.3], [-0.5, 0.6], [0.6, -0.5], [0.3, 0.3]
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

# Parameters of Sarsa algorithm
learning_rate = 0.3
discount_factor = 0.95
exploration_prob = 0.1
num_episodes = 5000

# Initialization of Q-matrix with random values
Q = np.random.rand(34, 2)



if __name__ == '__main__':
    episode_train(num_episodes)
    with open('models/modello_sarsa.pkl', 'wb') as file:
        pickle.dump(Q, file)

    print("Modello Q salvato con successo.")
