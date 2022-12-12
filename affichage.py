from turtle import *
import time

# dessine une allumette avec la tortue t
def dessineAllumette(x,y,l,c,t):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.setheading(90)
    t.width(10)
    t.forward(l)

def dessinePaquet(x, y, l, c, t, nb):
    coords = [x, y]
    for i in range(nb):
        dessineAllumette(coords[0], coords[1], l, c, t)
        coords[0] += 20
