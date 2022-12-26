import random as rd
import turtle as tu
import math


def dessinePolygone(nb_cotes, longueur, x, y, couleur):
    tu.up()
    tu.color(couleur)
    tu.goto(x, y)
    tu.down()
    a = 360 / nb_cotes
    i = 1
    while i <= nb_cotes:
        tu.forward(longueur)
        tu.left(a)
        i += 1


def dessineTriangle(longueur, x, y, couleur):
    dessinePolygone(3, longueur, x, y, couleur)


def sapin_foret(longueur, x, y):
    tu.hideturtle()
    tu.begin_fill()
    dessinePolygone(4, longueur, x, y, 'brown')
    tu.end_fill()
    tu.begin_fill()
    dessinePolygone(3, 2 * longueur, x - longueur / 2, longueur, 'green')
    tu.end_fill()


def foret(longueur, x, y):
    tu.speed(0)
    for i in range(rd.randint(1, 9)):
        sapin_foret(longueur, x + i * 2 * longueur, y)



def rectangle(longueur, x, y, couleur):
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.begin_fill()
    tu.color(couleur)
    tu.forward(longueur)
    tu.left(90)
    tu.forward(3 / 2 * longueur)
    tu.left(90)
    tu.forward(longueur)
    tu.left(90)
    tu.forward(3 / 2 * longueur)
    tu.end_fill()


def sapin(longueur, x, y):
    tu.hideturtle()
    tu.begin_fill()
    rectangle(longueur, x, y, 'brown')
    tu.end_fill()
    tu.seth(0)
    tu.begin_fill()
    tu.up()
    dessineTriangle(2 * longueur, x - longueur / 2, 3 / 2 * longueur, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle((3 / 2) * longueur, x - longueur / 3,
                    3 / 2 * longueur + sqrt(longueur ** 2 / 4 + longueur ** 2) - 1, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle(longueur, x - longueur / 4 + 10,
                    3 / 2 * longueur + sqrt(longueur ** 2 / 4 + longueur ** 2) - 1 + longueur, 'green')
    tu.end_fill()

def dessineCercle (x,y,couleur):
    tu.speed(0)
    dessinePolygone(100,l,x,y,couleur)



TAILLE_ECRAN = (1400, 700)
s = tu.Screen()
s.colormode(255)
s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])
tu.speed(0)
s.bgcolor(15,135,228)

def fond_():
    tu.up()
    tu.goto(-700,27.5)
    tu.down()
    tu.begin_fill()
    tu.color(8,40,100)
    tu.goto(-350,150)
    tu.goto(0,40)
    tu.goto(350,220)
    tu.goto(700,45)
    tu.goto(700,-400)
    tu.goto(-700,-400)
    tu.goto(-700,27.5)
    tu.end_fill()
    tu.exitonclick()
     

fond_()

