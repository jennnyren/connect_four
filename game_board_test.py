from game_board import GameBoard


def test_constructor():
    rows = 2
    cols = 2
    cell_size = 100
    gb = GameBoard(rows, cols, cell_size)
    assert (gb.rows == 2 and
            gb.cols == 2 and
            gb.cell_size == 100)


def test_drop_circle():
    rows = 6
    cols = 6
    cell_size = 100
    gb = GameBoard(rows, cols, cell_size)
    assert gb.drop_circle(2, 'red') == (5, 2)


def test_get_available_spots():
    rows = 6
    cols = 2
    cell_size = 100
    gb = GameBoard(rows, cols, cell_size)
    assert gb.get_available_spots() == [0, 1]


def test_check_winner():
    rows = 6
    cols = 6
    cell_size = 100
    gb = GameBoard(rows, cols, cell_size)
    gb.drop_circle(1, 'red')
    gb.drop_circle(2, 'red')
    gb.drop_circle(3, 'red')
    gb.drop_circle(4, 'red')
    assert gb.check_winner('red') is True
    gb.drop_circle(1, 'yellow')
    gb.drop_circle(2, 'yellow')
    gb.drop_circle(3, 'yellow')
    assert gb.check_winner('yellow') is False


def test_would_win():
    rows = 6
    cols = 6
    cell_size = 100
    gb = GameBoard(rows, cols, cell_size)
    gb.drop_circle(1, 'red')
    gb.drop_circle(2, 'red')
    gb.drop_circle(3, 'red')
    assert gb.would_win(4, 'red') is True
    assert gb.would_win(4, 'yellow') is False
