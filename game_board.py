class GameBoard:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.board = [[None for _ in range(cols)]for _ in range(rows)]

    def draw(self):
        """Draw the gameboard and
        drop circles in cells that have color values"""
        # Draw the gameboard
        stroke(0)
        for i in range(self.cols + 1):
            line(i * self.cell_size, 50, i * self.cell_size, self.rows * self.cell_size + 50)  # Adjust for top text
        for j in range(self.rows + 1):
            line(0, j * self.cell_size + 50, self.cols * self.cell_size, j * self.cell_size + 50)

        # drop circles
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "Red":
                    fill(255, 0, 0)
                    ellipse(col * self.cell_size + self.cell_size / 2, row * self.cell_size + self.cell_size / 2 + 50, 80, 80)
                elif self.board[row][col] == "Yellow":
                    fill(255, 255, 0)
                    ellipse(col * self.cell_size + self.cell_size / 2, row * self.cell_size + self.cell_size / 2 + 50, 80, 80)

    def drop_circle(self, col, player):
        """Assign color values to cells"""
        for row in reversed(range(self.rows)):
            if self.board[row][col] is None:
                self.board[row][col] = player
                return row, col
        return None

    def get_available_spots(self):
        """Identify avalable spots to drop"""
        spots = []
        for col in range(self.cols):
            # If the column is not full
            if self.board[0][col] is None:
                spots.append(col)
        return spots

    def check_winner(self, player):
        """Check if four circles of the same color connect
        horizontally, vertically or diagonally"""
        WINNING = 4
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - (WINNING - 1)):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True
        # Check vertical
        for row in range(self.rows - (WINNING - 1)):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True
        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - (WINNING - 1)):
            for col in range(self.cols - (WINNING - 1)):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
        # Check diagonal (top-right to bottom-left)
        for row in range((WINNING - 1), self.rows):
            for col in range(self.cols - (WINNING - 1)):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True
        # No more possible moves, it is a tie
        # if self.no_possible_moves():
        #     return False
        return False


    def would_win(self, col, player):
        """To check potential cells for winning"""
        temp_cell = self.drop_circle(col, player)
        if temp_cell is not None:
            row, col = temp_cell
            result = self.check_winner(player)
            # Undo the move
            self.board[row][col] = None
            return result
        return False

    # def no_possible_moves(self):
    #     for col in self.get_available_spots():
    #         if not self.would_win(col, 'Red') or\
    #                 not self.would_win(col, 'Yellow'):
    #             return True
