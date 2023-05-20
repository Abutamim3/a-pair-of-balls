

# Developed by Abdulrahman Alharbi


import tkinter

FPS = 25
WIDTH, HEIGHT = 500, 500


def main():
    tkinter.NoDefaultRoot()
    root = tkinter.Tk()
    root.resizable(False, False)
    canvas = tkinter.Canvas(root, bg='red', width=WIDTH, height=HEIGHT)
    canvas.grid()
    balls = (
        Ball(canvas, 10, 10, 40, 40, 'black'),
        Ball(canvas, 50, 50, 80, 80, 'blue')
     

    )
    root.after(1000 // FPS, update_balls, root, balls)
    root.mainloop()


def update_balls(root, balls):
    root.after(1000 // FPS, update_balls, root, balls)
    for ball in balls:
        ball.update()


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.__canvas = canvas
        self.__x_velocity = 9
        self.__y_velocity = 5
        self.__id = canvas.create_oval(x1, y1, x2, y2, fill=color)

    def update(self):
        self.__canvas.move(self.__id, self.__x_velocity, self.__y_velocity)
        x1, y1, x2, y2 = self.__canvas.coords(self.__id)
        if x1 < 0 or x2 > WIDTH:
            self.__x_velocity *= -1
        if y1 < 0 or y2 > HEIGHT:
            self.__y_velocity *= -1

print ("Developed by Abdulrahman Alharbi")


if __name__ == '__main__':
    main()
