
class Token:
    def __init__(self, color, initial_position, dimensione_cella):
        self.color = color
        self.position = initial_position
        self.size = dimensione_cella // 2  # Set the size to half of the cell size

    def move(self, direction):
        x, y = self.position
        if direction == 'UP' and y > 0:
            y -= 1
        elif direction == 'DOWN' and y < 14:
            y += 1
        elif direction == 'LEFT' and x > 0:
            x -= 1
        elif direction == 'RIGHT' and x < 14:
            x += 1
        self.position = (x, y)