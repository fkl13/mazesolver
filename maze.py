import time
from objects import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for c in range(self._num_cols):
            col = []
            for c in range(self._num_rows):
                cell = Cell(self._win)
                col.append(cell)
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._cell_size_x * i + self._x1
        y1 = self._cell_size_y * j + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False
        self._draw_cell(0, 0)

        bottom_right_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        bottom_right_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
