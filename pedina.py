class Token:
    def __init__(self, color, initial_position, number, dimensione_cella):
        self.color = color
        self.position = initial_position
        self.number = number
        self.size = dimensione_cella // 2  # Set the size to half of the cell size
        self.previous_position = None  # Add a variable to store the previous position

    def move(self, direction):
        # Save the current position as the previous position
        self.previous_position = self.position

        x, y = self.position
        if direction == 'UP' and y > 0:
            x -= 1
        elif direction == 'DOWN' and y < 14:
            x += 1
        elif direction == 'LEFT' and x > 0:
            y -= 1
        elif direction == 'RIGHT' and x < 14:
            y += 1
        self.position = (x, y)

        # Return the current and previous positions
        return self.position, self.previous_position
