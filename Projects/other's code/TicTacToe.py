import tkinter as tk
import turtle as tl
import time

root = tk.Tk()
root.title("Rifat's tic tac toe")

current_player = "O"


def change_player():
    global current_player
    if current_player == "O":
        current_player = "X"
    elif current_player == "X":
        current_player = "O"


def checkwin():
    for i in range(3):
        if cells[0][i].value == cells[1][i].value == cells[2][i].value != "":
            for j in range(3):
                cells[j][i].tt.color("red")
            cells[0][i].tt.up()
            cells[0][i].tt.speed(10)
            cells[1][i].tt.speed(10)
            cells[2][i].tt.speed(10)
            cells[0][i].tt.goto(0, 50)
            cells[0][i].tt.down()
            cells[0][i].tt.goto(0, -115)
            cells[1][i].tt.up()
            cells[1][i].tt.goto(0, 115)
            cells[1][i].tt.down()
            cells[1][i].tt.goto(0, -115)
            cells[2][i].tt.up()
            cells[2][i].tt.goto(0, 115)
            cells[2][i].tt.down()
            cells[2][i].tt.goto(0, -50)

            time.sleep(2)

            newboard()
    for i in range(3):
        if cells[i][0].value == cells[i][1].value == cells[i][2].value != "":
            for j in range(3):
                cells[i][j].tt.color("red")
            cells[i][0].tt.up()
            cells[i][0].tt.speed(10)
            cells[i][1].tt.speed(10)
            cells[i][2].tt.speed(10)
            cells[i][0].tt.goto(-50, 0)
            cells[i][0].tt.down()
            cells[i][0].tt.goto(115, 0)
            cells[i][1].tt.up()
            cells[i][1].tt.goto(-115, 0)
            cells[i][1].tt.down()
            cells[i][1].tt.goto(115, 0)
            cells[i][2].tt.up()
            cells[i][2].tt.goto(-115, 0)
            cells[i][2].tt.down()
            cells[i][2].tt.goto(50, 0)

            time.sleep(2)

            newboard()
    if cells[0][0].value == cells[1][1].value == cells[2][2].value != "":
        for i in range(3):
            cells[i][i].tt.color("red")
        cells[0][0].tt.speed(10)
        cells[1][1].tt.speed(10)
        cells[2][2].tt.speed(10)
        cells[0][0].tt.up()
        cells[0][0].tt.goto(-50, 50)
        cells[0][0].tt.down()
        cells[0][0].tt.goto(115, -115)
        cells[1][1].tt.up()
        cells[1][1].tt.goto(-115, 115)
        cells[1][1].tt.down()
        cells[1][1].tt.goto(115, -115)
        cells[2][2].tt.up()
        cells[2][2].tt.goto(-115, 115)
        cells[2][2].tt.down()
        cells[2][2].tt.goto(50, -50)

        time.sleep(2)
        newboard()
    if cells[0][2].value == cells[1][1].value == cells[2][0].value != "":
        cells[0][2].tt.speed(10)
        cells[0][2].tt.color("red")
        cells[1][1].tt.speed(10)
        cells[1][1].tt.color("red")
        cells[2][0].tt.speed(10)
        cells[2][0].tt.color("red")
        cells[0][2].tt.up()
        cells[0][2].tt.goto(50, 50)
        cells[0][2].tt.down()
        cells[0][2].tt.goto(-115, -115)
        cells[1][1].tt.up()
        cells[1][1].tt.goto(115, 115)
        cells[1][1].tt.down()
        cells[1][1].tt.goto(-115, -115)
        cells[2][0].tt.up()
        cells[2][0].tt.goto(115, 115)
        cells[2][0].tt.down()
        cells[2][0].tt.goto(-50, -50)

        time.sleep(2)
        newboard()

    for i in range(3):
        if cells[i][0].value == "" or cells[i][1].value == "" or cells[i][2].value == "":
            break
    else:
        time.sleep(2)
        newboard()


class Box():
    global current_player

    def __init__(self, mrow, mcolumn):

        self.row = mrow
        self.column = mcolumn
        self.value = ""
        self.label = tk.LabelFrame(root, width=235, height=235, bg="Black")

        # grid manager to set label localization
        self.label.grid(row=mrow, column=mcolumn)

        # Create button and set it localization. You can change it font without changing size of button, but if You set too big not whole will be visible

        self.cell = tk.Button(master=root,
                              bg="Black",
                              command=self.turn,
                              state="normal",
                              activebackground="Black",
                              relief="ridge"
                              )

        # Use sticky to button took up the whole label area
        self.cell.grid(row=mrow, column=mcolumn, sticky='nesw')
        self.sc = tk.Canvas(root, width=230, height=230, bd=0, bg="Black")
        self.nop = tl.TurtleScreen(self.sc)

    def turn(self):

        # self.cell["state"]="disabled"
        # self.cell["text"]=current_player
        # self.cell["font"]=("Arial","72")
        self.sc.grid(row=self.row, column=self.column, sticky='nsew')
        self.tt = tl.RawTurtle(self.sc)
        self.tt.speed(0)
        self.nop.bgcolor("Black")
        self.tt.color("White")

        self.tt.hideturtle()

        self.tt.pensize(20)

        self.value = current_player
        self.draw(current_player)

        change_player()
        checkwin()

    def draw(self, x):

        if x == "X":
            self.tt.speed(4)
            self.tt.up()
            self.tt.goto(-80, 80)
            self.tt.down()
            self.tt.seth(-45)
            self.tt.goto(80, -80)
            self.tt.up()
            self.tt.goto(80, 80)
            self.tt.down()
            self.tt.goto(-80, -80)

        elif x == "O":
            self.tt.speed(10)
            self.tt.up()
            self.tt.goto(0, 80)
            self.tt.down()
            self.tt.circle(-80)


cells = []


def newboard():
    global current_player
    current_player = "O"
    cells.clear()
    for i in range(3):
        cells.append([])
    for i in range(3):
        for j in range(3):
            cells[i].append(Box(i, j))


newboard()

root.mainloop()