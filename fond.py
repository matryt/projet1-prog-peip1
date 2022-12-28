import math
import random as rd
import turtle as tu


def dessinePolygone(cotes, longueur, x, y, couleur=(1, 106, 136)):
    tu.up()
    tu.color(couleur)
    tu.goto(x, y)
    tu.down()
    tu.seth(0)
    for i in range(cotes):
        tu.forward(longueur)
        tu.left(360 / cotes)


def dessineTriangle(longueur, x, y, couleur):
    dessinePolygone(3, longueur, x, y, couleur)


def sapin_foret(longueur, x, y):
    tu.hideturtle()
    tu.begin_fill()
    dessinePolygone(4, longueur, x, y, 'brown')
    tu.end_fill()
    tu.begin_fill()
    dessinePolygone(3, 2 * longueur, x - longueur / 2, y + longueur, 'green')
    tu.end_fill()


def foret(longueur, x, y):
    tu.speed(0)
    for i in range(9):
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
                    3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle(longueur, x - longueur / 4 + 10,
                    3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1 + longueur, 'green')
    tu.end_fill()


def fond_():
    TAILLE_ECRAN = (1400, 700)
    t=tu.Turtle()
    s = tu.Screen()
    s.colormode(255)
    s.screensize(TAILLE_ECRAN[0], TAILLE_ECRAN[1])
    t.speed(0)
    s.bgcolor(15, 135, 228)
    t.up()
    t.hideturtle()
    t.goto(-700, 27.5)
    t.down()
    t.begin_fill()
    t.color(8, 40, 100)
    t.goto(-350, 150)
    t.goto(0, 40)
    t.goto(350, 220)
    t.goto(700, 45)
    t.goto(700, -400)
    t.goto(-700, -400)
    t.goto(-700, 27.5)
    t.end_fill()
    foret(50, -450, -300)


fond_()
tu.exitonclick()
