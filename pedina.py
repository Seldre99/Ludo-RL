import costanti
from costanti import *


class Token:
    def __init__(self, color, initial_position, number, dimensione_cella):
        self.color = color
        self.position = initial_position
        self.number = number
        self.size = dimensione_cella // 2  # Set the size to half of the cell size
        self.previous_position = None  # Add a variable to store the previous position
        self.count = 62

    def move(self, direction):
        # Save the current position as the previous position
        self.previous_position = self.position
        x, y = self.position
        while direction > 0:
            if x in range(0, 6) and y == 8:
                if self.color == (0, 100, 0) and x == 1:
                    y -= 1
                else:
                    x += 1
            elif x in range(1, 6) and y == 7:
                x += 1
            elif x == 6 and y in range(8, 14):
                y += 1
            elif x in range(6, 8) and y == 14:
                x += 1
            elif x == 8 and y in range(9, 15):
                y -= 1
            elif x in range(8, 14) and y == 8:
                x += 1
            elif x == 14 and y in range(7, 9):
                y -= 1
            elif x in range(9, 15) and y == 6:
                x -= 1
            elif x == 8 and y in range(1, 7):
                y -= 1
            elif x in range(7, 9) and y == 0:
                x -= 1
            elif x == 6 and y in range(0, 6):
                if self.color == (139, 0, 0) and y == 1:
                    x += 1
                else:
                    y += 1
            elif x == 7 and y in range(1, 6):
                y += 1
            elif x in range(1, 7) and y == 6:
                x -= 1
            elif x == 0 and y in range(6, 8):
                y += 1
            direction -= 1
        '''
        if direction == 'UP' and y > 0:
            x -= 1
        elif direction == 'DOWN' and y < 14:
            x += 1
        elif direction == 'LEFT' and x > 0:
            y -= 1
        elif direction == 'RIGHT' and x < 14:
            y += 1
        '''
        self.position = (x, y)

        # Return the current and previous positions
        return self.position

'''
# Scelta del token da spostare
def turn(tokens, dado, phase, tok):
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
'''


# Scelta del token da spostare
def turn(tokens, dado, phase, tok):
    global observations
    win = False
    if phase == "red" and tok == 1:
        if tokens[0].position == (2, 2) and dado.value == 6:
            tokens[0].position = (6, 2)
            if tokens[1].position != (2, 3):
                observations = {
                    'into the base': 0,
                    'in the path': 2,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0

                }
            else:
                observations = {
                    'into the base': 1,
                    'in the path': 1,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
        elif tokens[0].position == (2, 2) and dado.value != 6 and tokens[1].position == (2, 3):
            observations = {
                'into the base': 2,
                'in the path': 0,
                'into the safe zone': 0,
                'arrived at destination': 0,
                'passed 1': 0,
                'passed 2': 0
            }
        elif tokens[0].position != (2, 2):
            new_position = tokens[0].move(dado.value)
            # Verifico se la prima pedina che non è nella base è nella safe zone
            if new_position in costanti.red_safe_zone:
                if tokens[1].position not in costanti.red_safe_zone and tokens[1].position != (2, 3):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[1].position not in costanti.red_safe_zone and tokens[1].position == (2, 3):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[1].position in costanti.red_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 2,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }

            elif new_position == (7, 6):
                if tokens[1].position == (7, 6):
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 2,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                    win = endgame('red')

                elif tokens[1].position not in costanti.red_safe_zone and tokens[1].position!=(2,3):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                elif tokens[1].position in costanti.red_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[1].position == (2,3):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
    elif phase == "red" and tok == 2:
        if tokens[1].position == (2, 3) and dado.value == 6:
            tokens[1].position = (6, 2)
            if tokens[0].position != (2, 2):
                observations = {
                    'into the base': 0,
                    'in the path': 2,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
            else:
                observations = {
                    'into the base': 1,
                    'in the path': 1,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
        elif tokens[1].position == (2, 3) and dado.value != 6 and tokens[0].position == (2, 2):
            observations = {
                'into the base': 2,
                'in the path': 0,
                'into the safe zone': 0,
                'arrived at destination': 0,
                'passed 1': 0,
                'passed 2': 0
            }
        elif tokens[1].position != (2, 3):
            new_position = tokens[1].move(dado.value)
            # Verifico se la prima pedina che non è nella base è nella safe zone
            if new_position in costanti.red_safe_zone:
                if tokens[0].position not in costanti.red_safe_zone and tokens[0].position != (2, 2):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[0].position not in costanti.red_safe_zone and tokens[0].position == (2, 2):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[0].position in costanti.red_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 2,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }

            elif new_position == (7, 6):
                if tokens[0].position == (7, 6):
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 2,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                    win = endgame('red')

                elif tokens[0].position not in costanti.red_safe_zone and tokens[0].position!=(2,2):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                elif tokens[0].position in costanti.red_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[0].position == (2, 2):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
    elif phase == "green" and tok == 1:
        if tokens[2].position == (2, 11) and dado.value == 6:
            tokens[2].position = (2, 8)
            if tokens[3].position != (2, 12):
                observations = {
                    'into the base': 0,
                    'in the path': 2,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
            else:
                observations = {
                    'into the base': 1,
                    'in the path': 1,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
        elif tokens[2].position == (2, 11) and dado.value != 6 and tokens[3].position == (2, 12):
            observations = {
                'into the base': 2,
                'in the path': 0,
                'into the safe zone': 0,
                'arrived at destination': 0,
                'passed 1': 0,
                'passed 2': 0
            }
        elif tokens[2].position != (2, 11):
            new_position = tokens[2].move(dado.value)
            # Verifico se la prima pedina che non è nella base è nella safe zone
            if new_position in costanti.green_safe_zone:
                if tokens[3].position not in costanti.green_safe_zone and tokens[3].position != (2, 12):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[3].position not in costanti.green_safe_zone and tokens[3].position == (2, 12):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[3].position in costanti.green_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 2,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }

            elif new_position == (6, 7):
                if tokens[3].position == (6, 7):
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 2,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                    win = endgame('green')

                elif tokens[3].position not in costanti.green_safe_zone and tokens[3].position!=(2, 12):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                elif tokens[3].position in costanti.green_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[3].position == (2,12):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }

    elif phase == "green" and tok == 2:
        if tokens[3].position == (2, 12) and dado.value == 6:
            tokens[3].position = (2, 8)
            if tokens[2].position != (2, 11):
                observations = {
                    'into the base': 0,
                    'in the path': 2,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
            else:
                observations = {
                    'into the base': 1,
                    'in the path': 1,
                    'into the safe zone': 0,
                    'arrived at destination': 0,
                    'passed 1': 0,
                    'passed 2': 0
                }
        elif tokens[3].position == (2, 12) and dado.value != 6 and tokens[2].position == (2, 11):
            observations = {
                'into the base': 2,
                'in the path': 0,
                'into the safe zone': 0,
                'arrived at destination': 0,
                'passed 1': 0,
                'passed 2': 0
            }
        elif tokens[3].position != (2, 12):
            new_position = tokens[3].move(dado.value)
            # Verifico se la prima pedina che non è nella base è nella safe zone
            if new_position in costanti.green_safe_zone:
                if tokens[2].position not in costanti.green_safe_zone and tokens[2].position != (2, 11):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[2].position not in costanti.green_safe_zone and tokens[2].position == (2, 11):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[2].position in costanti.green_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 2,
                        'arrived at destination': 0,
                        'passed 1': 0,
                        'passed 2': 0
                     }

            elif new_position == (6, 7):
                if tokens[2].position == (6, 7):
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 2,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                    win = endgame('green')

                elif tokens[2].position not in costanti.green_safe_zone and tokens[2].position!=(2,11):
                    observations = {
                        'into the base': 0,
                        'in the path': 1,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                    }
                elif tokens[2].position in costanti.green_safe_zone:
                    observations = {
                        'into the base': 0,
                        'in the path': 0,
                        'into the safe zone': 1,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }
                elif tokens[2].position == (2, 11):
                    observations = {
                        'into the base': 1,
                        'in the path': 0,
                        'into the safe zone': 0,
                        'arrived at destination': 1,
                        'passed 1': 0,
                        'passed 2': 0
                     }

    return observations, win


# Controllo se ci sia un vincitore
def endgame(phase):
    if phase == "red":
        costanti.red_wins += 1
        print('Hai vinto rosso')
        return True
    else:
        costanti.green_wins += 1
        print('Hai vinto verde')
        return True


# Controllo per evitare di perdere il turno
def check_end_position(tokens, phase, tok):
    if phase == "red" and tok == 1:
        return True if (tokens[0].position == (7, 6)) else False
    elif phase == "red" and tok == 2:
        return True if (tokens[1].position == (7, 6)) else False
    elif phase == "green" and tok == 1:
        return True if (tokens[2].position == (6, 7)) else False
    elif phase == "green" and tok == 2:
        return True if (tokens[3].position == (6, 7)) else False
