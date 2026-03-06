from game_controller import GameController


def test_constructor():
    rows = 2
    cols = 2
    cell_size = 100
    gc = GameController(rows, cols, cell_size)
    assert (gc.gb.rows == 2 and
            gc.gb.cols == 2 and
            gc.gb.cell_size == 100 and
            gc.current_player == 'Red' and
            gc.turn_text == 'Red turn (you)' and
            gc.is_human is True and
            gc.computer_delay is None and
            gc.winner is None and
            gc.preview_col is None)
