class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        self._x1 = top_left_x
        self._y1 = top_left_y

        self._x2 = bottom_right_x
        self._y2 = bottom_right_y
        if self.has_top_wall:
            line = Line(
                Point(top_left_x, top_left_y), Point(bottom_right_x, top_left_y)
            )
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(
                Point(bottom_right_x, top_left_y), Point(bottom_right_x, bottom_right_y)
            )
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(
                Point(top_left_x, bottom_right_y), Point(bottom_right_x, bottom_right_y)
            )
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(
                Point(top_left_x, top_left_y), Point(top_left_x, bottom_right_y)
            )
            self._win.draw_line(line)
