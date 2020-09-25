from processing_py import *

app = App(600,400) # create window: width, height
# app.background(255,0,0) # set background:  red, green, blue
# app.redraw() # refresh the window


# noLoop()
app.rectMode(CENTER)

# def redraw():

while True:
    app.background(200, 200, 200)
    c = color(255, 0,0)
    app.fill(c)
    app.rect(app.mouseX,app.mouseY,100,200)
    app.redraw()