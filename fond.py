# Loic LAMOUR et Mathieu CUVELIER - Groupe 5

import math
import turtle as tu


def dessinePolygone(cotes, longueur, x, y, couleur=(1, 106, 136)):
    """
    Permet de dessiner un polygone quelconque
    :param cotes: Le nombre de côtés à tracer
    :type cotes: int
    :param longueur: La longueur des côtés du polygone
    :type longueur: int/float
    :param x: L'abscisse du début du polygone
    :type x: int/float
    :param y: L'ordonnée du début du polygone
    :type y: int/float
    :param couleur: La couleur dans laquelle tracer le polygone
    :type couleur: tuple / str
    """
    tu.up()
    tu.color(couleur)
    tu.goto(x, y)
    tu.down()
    tu.seth(0)
    for i in range(cotes):
        tu.forward(longueur)
        tu.left(360 / cotes)


def dessineTriangle(longueur, x, y, couleur):
    """
    :param longueur: La longueur des côtés du triangle
    :type longueur: int/float
    :param x: L'abscisse du début du triangle
    :type x: int/float
    :param y: L'ordonnée du début du triangle
    :type y: int/float
    :param couleur: La couleur dans laquelle tracer le triangle
    :type couleur: tuple/str
    """
    dessinePolygone(3, longueur, x, y, couleur)


def sapin_foret(longueur, x, y):
    """
    Permet de dessiner un sapin qui compose la forêt
    :param longueur: La longueur du tronc du sapin
    :type longueur: int/float
    :param x: L'abscisse de début du sapin
    :type x: int/float
    :param y: L'ordonnée de début du sapin
    :type y: int/float
    """
    tu.hideturtle()
    tu.begin_fill()
    dessinePolygone(4, longueur, x, y, 'brown')
    tu.end_fill()
    tu.begin_fill()
    dessinePolygone(3, 2 * longueur, x - longueur / 2, y + longueur, 'green')
    tu.end_fill()


def foret(longueur, x, y):
    """
    Permet de dessiner une forêt de sapins
    :param longueur: La longueur du tronc des sapins
     :type longueur: int/float
    :param x: L'abscisse du début de la forêt
    :type x: int/float
    :param y: L'ordonnée du début de la forêt
    :type y: int/float
    """
    tu.speed(0)
    for i in range(9):
        sapin_foret(longueur, x + i * 2 * longueur, y)


def rectangle(longueur, x, y, couleur):
    """
    :param longueur: La largeur du rectangle
    :type longueur: int/float
    :param x: L'abscisse du début du rectangle
    :type x: int/float
    :param y: L'ordonnée du début du rectangle
    :type y: int/float
    :param couleur: La couleur dans laquelle tracer le rectangle
    :type couleur: tuple/str
    """
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
    """
    Permet de dessiner un sapin seul
    :param longueur: La longueur du tronc du sapin
    :type longueur: int/float
    :param x: L'abscisse de début du sapin
    :type x: int/float
    :param y: L'ordonnée de début du sapin
    :type y: int/float
    """
    tu.hideturtle()
    tu.begin_fill()
    rectangle(longueur, x, y, 'brown')
    tu.end_fill()
    tu.seth(0)
    tu.begin_fill()
    tu.up()
    dessineTriangle(2 * longueur, x - longueur / 2, y + 3 / 2 * longueur, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle((3 / 2) * longueur, x - longueur / 3,
                    y + 3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1, 'green')
    tu.end_fill()
    tu.begin_fill()
    dessineTriangle(longueur, x - longueur / 4 + 10,
                    y + 3 / 2 * longueur + math.sqrt(longueur ** 2 / 4 + longueur ** 2) - 1 + longueur, 'green')
    tu.end_fill()


def fond_():
    """
    Permet de tracer le fond complet
    """
    TAILLE_ECRAN = (1400, 700)
    t = tu.Turtle()
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
    foret(50, -430, -300)
    sapin(50, -60, -60)
    sapin(50, -140, -100)
    sapin(50, 60, -120)


if __name__ == "__main__":
    fond_()
    tu.exitonclick()
