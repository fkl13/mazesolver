from window import Window
from point import Line
from point import Point


def main():
    win = Window(800, 600)
    p1 = Point(2, 2)
    p2 = Point(20, 23)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
