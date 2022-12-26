import random as rd
import turtle as tu
from math import *


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

foret(50,0,0)

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


