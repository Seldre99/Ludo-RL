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
