from turtle import *
from time import sleep

# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def dessineCroix(x,y,l,c,t):
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
    t.color(c)
    t.setheading(90)
    t.width(20)
    t.forward(l)
    t.width(30)
    t.color("red")
    t.forward(2)

def dessinePaquet(x, y, l, c, t, nb):
    for i in range(nb):
        dessineAllumette(x+i*50,y,l,c,t)
    
def couronne(s : Screen) -> None:
    s.clear()
    s.colormode(255)
    hideturtle()
    color(236, 228, 0)
    up()
    goto(-100, -100)
    seth(0)
    down()
    forward(215)
    left(90)
    forward(200)
    pointe(26.57)
    pointe(53.13)
    setheading(270)
    forward(200)


def pointe(angle):
    left(180 - angle)
    forward(120)
    right(180-53.13)
    forward(120)