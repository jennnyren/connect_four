from game_controller import GameController
ROWS = 6
COLS = 7
CELL_SIZE = 100
TOP_MARGIN = 50

gc = GameController(ROWS, COLS, CELL_SIZE)

def setup():
    size(gc.gb.cols * gc.gb.cell_size, gc.gb.rows * gc.gb.cell_size + TOP_MARGIN)

def draw():
    background(240)
    gc.draw()
    if not gc.is_human and not gc.winner:
        gc.computer_move()

def mouseMoved():
    gc.update_preview()

def mousePressed():
    if gc.is_human and not gc.winner:
        gc.human_move()
