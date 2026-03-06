import random
from game_board import GameBoard
from save_name import SaveName

class GameController:
    def __init__(self, rows, cols, cell_size):
        self.gb = GameBoard(rows, cols, cell_size)
        self.current_player = 'Red'
        self.turn_text = 'Red turn (you)'
        self.is_human = True
        self.computer_delay = None
        self.winner = None
        self.preview_col = None
        self.save_name = SaveName()

    def draw(self):
        """Draw the board to the screen and display user_turn text
        or winner information, and draw the preview if human player"""
        # Draw the gameboard
        self.gb.draw()
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(32)
        if self.winner == 'Red':
            text('Red wins!\n Game over', width / 2, 200)
        elif self.winner == 'Yellow':
            text('Yellow wins!\n Game over', width / 2, 200)
        elif not self.gb.get_available_spots():
            text('No possible moves\n Game over', width / 2, 200)
        else:
            text(self.turn_text, width / 2, 25)
        # Draw preview if human
        if self.is_human and self.preview_col is not None and self.winner is None:
            fill(255, 0, 0, 150)
            ellipse(self.preview_col * self.gb.cell_size + self.gb.cell_size / 2, 50, 80, 80)

    def human_move(self):
        """Handle human move"""
        col = mouseX // self.gb.cell_size
        if 0 <= col < self.gb.cols:
            placed = self.gb.drop_circle(col, self.current_player)
            if placed:
                if self.gb.check_winner(self.current_player):
                    self.winner = 'Red'
                    self.save_name.save_name_to_file()
                    return
                # Switch to computer's turn
                self.current_player = 'Yellow'
                self.turn_text = 'Yellow turn (computer)'
                self.is_human = False
                # Record start for computer
                self.computer_delay = millis()

    def computer_move(self):
        """Handle computer move"""
        # Handle delay
        if millis() - self.computer_delay >= 1000:
            spots = self.gb.get_available_spots()
            for col in spots:
                if self.gb.would_win(col, 'Red'):
                    self.gb.drop_circle(col, self.current_player)
                    if self.gb.check_winner(self.current_player):
                        self.winner = 'Yellow'
                        # self.save_name.no_update()
                    # Switch back to human's turn
                    self.current_player = 'Red'
                    self.turn_text = 'Red turn (you)'
                    self.is_human = True
                    return
            if spots:
                col = random.choice(spots)
                self.gb.drop_circle(col, self.current_player)
                if self.gb.check_winner(self.current_player):
                    self.winner = 'Yellow'
            # Switch back to human's turn
            self.current_player = 'Red'
            self.turn_text = 'Red turn (you)'
            self.is_human = True

    def update_preview(self):
        """Update preview for human player"""
        if self.is_human:
            col = mouseX // self.gb.cell_size
            if 0 <= col <= self.gb.cols:
                self.preview_col = col
            else:
                self.preview_col = None
        else:
            self.preview_col = None
