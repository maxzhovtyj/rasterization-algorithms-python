from tkinter import *

PIXEL_SIZE = 3
HEIGHT = 600
WIDTH = 1000


class RastAlgorithms:
    def __init__(self):
        # window initializing
        window = Tk()
        window.title("Computer Graphics. Laboratory work #1")

        # place canvas in the window
        self.canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.canvas.create_text(300, 50, text="Maksym Zhovtaniuk KV-03", fill="black", font="Helvetica 15 bold")

        dda_btn = Button(frame, text="DDA", command=self.callback("dda"))
        dda_btn.grid(row=1, column=2)

        bres_btn = Button(frame, text="Bresenham", command=self.callback("bresenham"))
        bres_btn.grid(row=1, column=3)

        circle_bres_btn = Button(frame, text="Circle Bresenham", command=self.callback("circle_bresenham"))
        circle_bres_btn.grid(row=1, column=4)

        wu_btn = Button(frame, text="Wu", command=self.callback("wu"))
        wu_btn.grid(row=1, column=5)

        clear_btn = Button(frame, text="Clear", width=30, command=self.clean)
        clear_btn.grid(row=1, column=6)

        window.mainloop()

    def callback(self, func):
        if func == "dda":
            return lambda func_name=func: getattr(self, func_name)(10, 10, 300, 180)
        elif func == "bresenham":
            return lambda func_name=func: getattr(self, func_name)(10, 10, 300, 180)
        elif func == "circle_bresenham":
            return lambda func_name=func: getattr(self, func_name)(150, 100, 50)
        elif func == "wu":
            return lambda func_name=func: getattr(self, func_name)(10, 10, 300, 180)
        elif func == "surname":
            return lambda func_name=func: getattr(self, func_name)

    def surname(self):
        self.canvas.create_text(300, 50, text="Maksym Zhovtaniuk KV-03", fill="black",
                                font="Helvetica 15 bold")

    def dda(self, x1: int, y1: int, x2: int, y2: int):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        # find maximum difference
        steps = max(dx, dy)

        # calculate the increment in x and y
        x_inc = dx / steps
        y_inc = dy / steps

        # start with 1st point
        x = float(x1)
        y = float(y1)

        # make a list for coordinates
        coordinates = []

        for i in range(steps):
            # append the x,y coordinates in respective list
            coordinates.append((x, y))

            # increment the values
            x = x + x_inc
            y = y + y_inc

        self.draw(coordinates)

    def bresenham(self, x1: int, y1: int, x2: int, y2: int):
        x, y = x1, y1
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        p = 2 * dy - dx

        # Initialize the plotting points
        coordinates = [(x, y)]

        for k in range(2, dx + 2):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy

            x = x + 1 if x < x2 else x - 1

            coordinates.append((x, y))

        self.draw(coordinates)

    def circle_bresenham(self, xc, yc, radius):
        x = 0
        y = radius
        delta = 1 - 2 * radius

        points = []
        while y >= 0:
            points.append((xc + x, yc + y))
            points.append((xc + x, yc - y))
            points.append((xc - x, yc + y))
            points.append((xc - x, yc - y))
            error = 2 * (delta + y) - 1
            if (delta < 0) and (error <= 0):
                x += 1
                delta += 2 * x + 1
                continue
            error = 2 * (delta - x) - 1
            if delta > 0 and error > 0:
                y -= 1
                delta += 1 - 2 * y
                continue
            x += 1
            delta += 2 * (x - y)
            y -= 1

        self.draw(points)

    def wu(self, x1, y1, x2, y2):
        def _fpart(x):
            return x - int(x)

        def _rfpart(x):
            return 1 - _fpart(x)

        points = []
        dx, dy = x2 - x1, y2 - y1
        x, y = x1, y1

        if dy == 0:
            points.append([x, y1])
            while abs(x) < abs(x2):
                x += 1
                points.append([x, y1])

        elif dx == 0:
            points.append([x1, y])
            while abs(y) < abs(y2):
                y += 1
                points.append([x1, y])
        else:
            grad = dy / dx
            float_y = y1 + _rfpart(x1) * grad

            def compute_endpoint(a, b):
                x_endpoint = a
                y_endpoint = b + grad * (x_endpoint - a)
                px, py = int(x_endpoint), int(y_endpoint)
                points.append([px, py])
                points.append([px, py + 1])
                return px

            x_start = compute_endpoint(x1, y1)
            x_end = compute_endpoint(x2, y2)

            for x in range(x_start, x_end):
                y = int(float_y)
                points.append([x, y])
                points.append([x, y + 1])
                float_y += grad

        self.draw(points)

    def draw(self, coordinates):
        for point in coordinates:
            self.canvas.create_rectangle(
                PIXEL_SIZE * point[0], PIXEL_SIZE * point[1],
                PIXEL_SIZE * point[0] + PIXEL_SIZE, PIXEL_SIZE * point[1] + PIXEL_SIZE, fill="black")

    def clean(self):
        self.canvas.delete("all")
        self.surname()


if __name__ == "__main__":
    RastAlgorithms()
