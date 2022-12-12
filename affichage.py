from turtle import *
import time

# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def dessineCroix(x,y,l,c,t):
    for i in range(
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x+l,y+l)
    t.up()
    t.goto(x+l,y)
    t.down()
    t.goto(x,y+l)
    t.width(1)

# dessine une allumette avec la tortue t
def dessineAllumette(x,y,l,c,t):
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(90)
    t.color(c)
    t.width(10)
    t.forward(l)
def dessineLesAllumettes(x,y,l,c,t,n):
    for i in range(n):
        dessineAllumette(x+i*20,y,l,c,t)
