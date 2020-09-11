import os, time
from data.readfile import *
cwd = os.getcwd()
grid = readfile(f'{cwd}\\data')
print(*grid)
from processing_py import * # pip install processing-py
from data.block_class import *
from data.update import *

def delay(seconds : float):
	time.sleep(seconds)

delta = 0
rez = 150

def showDir(pos, i,j):
    PI = 3.14
    a = pos.dir
    app.pushMatrix()
    app.translate(i,j)
    if a[1] == 1:
        app.rotate(PI)
    app.rotate(PI/2 * a[0])
    app.translate(0,-65)
    app.ellipse(0,0,20,20)
    app.popMatrix()

h = len(grid) * rez
w = len(grid[0]) * rez
app = App(w,h)
app.background(0)
app.noStroke()
iter = 0
boolean = True
agrid = []
for i in range(len(grid)):
    agrid.append([])
    for j in range(len(grid[0])):
        agrid[i].append(block(grid[i][j]))

while boolean:
    for i in range(0, w, rez):
        for j in range(0, h, rez):
            pos = agrid[int(j / rez)][int(i / rez)]
            if pos.val == 'p':
            	app.fill(20,20,255)
            elif pos.val == "n":
                app.fill(255, 10, 30)
            elif pos.val == "b":
                app.fill(150, 150, 20)
            else:
                g = pos.val * 255
                app.fill(20, g, 10)
            app.rect(i, j, rez, rez)
            app.textAlign(CENTER, CENTER)
            app.fill(255)
            app.textSize(22)
            app.pushMatrix()
            app.translate(rez / 2, rez / 2)
            if pos.isDigit:
                app.text(f'{pos.val : .2f}', i, j)
            else: app.text(pos.pval, i, j)
            if pos.isDigit:
                showDir(pos, i,j)
            app.popMatrix()
    delta, agrid = update(agrid)
    delay(0.2)
    if delta >= 0.005*(1-l)/l:
    	app.redraw()
    else:
    	boolean = False
    	print(f'total iteration before convergence : {iter}')
    iter +=1