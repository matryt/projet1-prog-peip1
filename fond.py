import random as rd
import turtle as tu
from math import *


def dessinePolygone(nb_cotes, l, x, y, couleur):
    tu.up()
    tu.color(couleur)
    tu.goto(x, y)
    tu.down()
    a = 360 / nb_cotes
    i = 1
    while i <= nb_cotes:
        tu.forward(l)
        tu.left(a)
        i += 1


def dessineTriangle(l, x, y, couleur):
    dessinePolygone(3, l, x, y, couleur)


def sapin_foret(l, x, y):
    tu.hideturtle()
    tu.begin_fill()
    dessinePolygone(4, l, x, y, 'brown')
    tu.end_fill()
    tu.begin_fill()
    dessinePolygone(3, 2 * l, x - l / 2, l, 'green')
    tu.end_fill()


def foret(l, x, y, n):
    for i in range(rd.randint(1, 9)):
        sapin_foret(l, x + i * 2 * l, y)


def rectangle(l, x, y, couleur):
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.begin_fill()
    tu.color(couleur)
    tu.forward(l)
    tu.left(90)
    tu.forward(3 / 2 * l)
    tu.left(90)
    tu.forward(l)
    tu.left(90)
    tu.forward(3 / 2 * l)
    tu.end_fill()


def sapin(l, x, y):
    tu.hideturtle()
    tu.begin_fill()
    rectangle(l, x, y, 'brown')
    tu.end_fill()
    tu.seth(0)
    tu.begin_fill()
    tu.up()
    dessineTriangle(2 * l, x - l / 2, 3 / 2 * l, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle((3 / 2) * l, x - l / 3, 3 / 2 * l + sqrt(l ** 2 / 4 + l ** 2) - 1, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle(l, x - l / 4 + 10, 3 / 2 * l + sqrt(l ** 2 / 4 + l ** 2) - 1 + l, 'green')
    tu.end_fill()

sapin(60,0,0)
