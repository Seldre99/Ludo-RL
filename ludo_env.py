from pedina import turn, check_end_position
from costanti import *
import gym


def move_token_one(dado):
    observation, end = turn(tokens[0], dado, "red", 1)
    return observation, end

def move_token_two(dado):
    observation, end = turn(tokens[1], dado, "red", 2)
    return observation, end


class ludo_env(gym.Env):
    def __init__(self):
        super(ludo_env, self).__init__()
        self.observations = observations
        self.action_space = gym.spaces.Discrete(2)  # Due azioni possibili
        self.observation_space = gym.spaces.Dict({
            'into the base': gym.spaces.Discrete(3),
            'in the path': gym.spaces.Discrete(3),
            'into the safe zone': gym.spaces.Discrete(3),
            'arrived at destination': gym.spaces.Discrete(3)
        })

    def reset(self):
        tokens = [Token((139, 0, 0), (2, 2), 1, dimensione_cella),
                  Token((139, 0, 0), (2, 3), 2, dimensione_cella),
                  Token((0, 100, 0), (2, 11), 1, dimensione_cella),
                  Token((0, 100, 0), (2, 12), 2, dimensione_cella)]
        return observations, tokens

    def step(self, action, dado, consecutive_sixes):
        max_consecutive_sixes = 3
        reward = 0

        if action not in [0, 1]:
            raise ValueError("Azione non valida")

        if action == 0:
            if check_end_position(action, tokens, phase):
                pass
            observation, end = move_token_one(dado)
            if tokens[0].position == (6, 2):
                reward += 0.5
            elif tokens[0].position in red_safe_zone:
                reward += 0.8
            elif tokens[0].position == (7, 6):
                reward += 0.8

        elif action == 1:
            if check_end_position(action, tokens, phase):
                pass
            observation, end = move_token_two(dado)
            if tokens[1].position == (6, 2):
                reward += 0.5
            elif tokens[1].position in red_safe_zone:
                reward += 0.8
            elif tokens[1].position == (7, 6):
                reward += 0.8

        dice_value = dado.value
        print("turno:", phase, "valore dado:", dice_value)
        # Se il dado ritorna 6, incrementa il conteggio
        if dice_value == 6:
            consecutive_sixes += 1
            dado.roll()
            if consecutive_sixes == max_consecutive_sixes:
                print(f"Giocatore ha ottenuto {max_consecutive_sixes} 6 consecutivi. Turno passa all'avversario.")
                consecutive_sixes = 0
        else:
            # Se il dado non ritorna 6, resetta il conteggio
            consecutive_sixes = 0

        # Se il dado non ritorna 6, cambia automaticamente il turno all'altro giocatore
        if dice_value != 6:
            dado.roll()

        if tokens[0].position == (7, 6) and tokens[1].position == (7, 6):
            reward += 1
        #elif tokens[2].position == (6, 7) and tokens[3].position == (6, 7):
        #    reward -= 0.7

        return dado, observation, reward, consecutive_sixes, end
