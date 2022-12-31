import turtle as tu
from math import sqrt

# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def dessineCroix(x, y, longueur, c, t):
    """"
    x:int position en abscisse 
    y:int position en ordonnée
    longueur:int longueur
    c:str or tuple  couleur 
    t:turtle
    Fonction pour dessiner une croix
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x + longueur, y + longueur)
    t.up()
    t.goto(x + longueur, y)
    t.down()
    t.goto(x, y + longueur)
    t.width(1)


def dessinePolygone(cotes, longueur, x, y, t, couleur=(1, 106, 136)):
    """

    cotes:int nombre de cotes
    longueur:int longueur 
    x:int position en abcisse
    y:int position en ordonnée
    t turtle
    couleur:tuple 
    fonction pour dessinner un polygone quelconque 

    """
    t.up()
    t.color(couleur)
    t.goto(x, y)
    t.down()
    t.seth(0)
    for i in range(cotes):
        t.forward(longueur)
        t.left(360 / cotes)


def dessineCercle(x, y, t, couleur, longueur=1):
    """
    x:int position en abscisse
    y:int position en ordonnée
    t turtle
    couleur:str or tuple 
    longueur:int
    Fonction pour dessiner un cercle

    """
    t.color(couleur)
    t.begin_fill()
    dessinePolygone(250, longueur, x, y, t, couleur)
    t.end_fill()


def buisson(x, y, fruits, t):
    """
    x:int position abscisse
    y:int position ordonnée 
    fruits:int nombre de fruits dans un buisson
    t turtle 
    fonction pour dessiner un buisson avec les fruits 
    """
    t.hideturtle()
    for i in range(3):
        dessineCercle(x + 25 * i, y, t, (110, 196, 0), 1)
    for j in range(min(7, fruits)):
        dessineCercle(x + 15 * (j - 1.5), y + 20, t, (196, 14, 0), 0.1)
    fruits -= 7
    for i in range(min(7, fruits)):
        dessineCercle(x + 15 * (i - 1.5), y + 50, t, (196, 14, 0), 0.1)


def couronne(s) -> None:
    """
    
    fonction pour dessiner une couronne à la fin lorsque le joueur gagne
    """
    s.clear()
    s.colormode(255)
    tu.hideturtle()
    tu.color(186, 180, 0)
    tu.width(2)
    tu.up()
    tu.goto(-100, -100)
    tu.seth(0)
    tu.down()
    tu.forward(215)
    tu.left(90)
    tu.forward(200)
    pointe(26.57)
    pointe(53.13)
    tu.setheading(270)
    tu.forward(200)


def pointe(angle):
    """
    angle:float
    dessine une pointe pour le dessin de la couronne 
    fonction réutilisée dans la fonction couronne()
    """
    tu.left(180 - angle)
    tu.forward(120)
    tu.right(180 - 53.13)
    tu.forward(120)

def os(x, y, droite = True):
    """
    x:int position abscisse 
    y:int position ordonnée
    droite:bool indique la position de l'os( droite ou gauche )
    fonction pour dessiner un os 
    """
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.left(15)
    if droite:
        tu.forward(2.98*52)
    else:
        tu.forward(2.6*52)
    tu.right(180-109.53)
    tu.forward(0.82*52)
    tu.left(180-125.97)
    tu.forward(0.79*52)
    tu.left(180-134.72)
    tu.forward(0.96*52)
    tu.left(180-133.488)
    tu.forward(0.81*52)
    tu.left(180-140.98)
    tu.forward(0.66*52)
    tu.left(180-108.92)
    tu.forward(0.35*52)
    tu.left(180)
    tu.forward(0.35*52)
    tu.left(180-152.44)
    tu.forward(0.38*52)
    tu.left(180-125.39)
    tu.forward(1.06*52)
    tu.left(180-128.7)
    tu.forward(0.66*52)
    tu.left(180-137.26)
    tu.forward(0.98*52)
    tu.left(180-131.21)
    tu.forward(0.65*52)
    tu.left(180-161.45)
    tu.forward(0.56*52)
    tu.right(180-108.07)
    if not droite:
        tu.forward(2.98*52)
    else:
        tu.forward(2.6*52)
    tu.left(105.09)
    tu.down()
    tu.up()
    tu.forward(1.52*52)
    tu.forward(-1.52*52)
    tu.up()
    tu.goto(x, y)

def bouche(x, y, angle):
    """
    x:int position abscisse 
    y:int position ordonnée
    angle:float
    fonction pour dessinner une bouche 
    """
    tu.seth(angle)
    tu.right(90)
    tu.up()
    tu.goto(x, y)
    tu.down()
    tu.forward(115.44000000000001)
    tu.seth(0)
    tu.forward(191.88)
    tu.seth(90)
    tu.forward(115.44000000000001)
    tu.forward(-46.800000000000004)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(28.080000000000002)
    tu.forward(-56.160000000000004)
    tu.forward(28.080000000000002)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(19.24)
    tu.forward(-38.48)
    tu.forward(19.24)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(28.080000000000002)
    tu.forward(-56.160000000000004)
    tu.forward(28.080000000000002)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(19.24)
    tu.forward(-38.48)
    tu.forward(19.24)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(28.080000000000002)
    tu.forward(-56.160000000000004)
    tu.forward(28.080000000000002)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.right(90)
    tu.forward(19.24)
    tu.forward(-38.48)
    tu.forward(19.24)
    tu.left(90)
    tu.forward(27.411428571428573)
    tu.up()
    tu.goto(x, y)
    tu.right(180)
    tu.up()
    tu.forward(191.88)
    tu.down()

def crane():
    """
    fonction pour dessiner un crâne
    """
    tu.seth(45)
    tu.forward(100)
    tu.left(45)
    tu.forward(100)
    tu.left(45)
    tu.forward(100)
    tu.left(45)
    tu.forward(190)
    tu.left(45)
    tu.forward(100)
    tu.left(45)
    tu.forward(100)
    tu.left(45)
    tu.forward(100)

def yeux():
    """
    fonction pour dessiner des yeux
    """
    tu.seth(90)
    tu.up()
    tu.forward(150)
    tu.right(90)
    tu.down()
    rectangle(70, 40)
    tu.up()
    tu.forward(110)
    tu.down()
    rectangle(70, 40)

def rectangle(x, y):
    """
    x:float longueur rectangle
    y:float largeur rectangle 
    fonction pour dessiner un rectangle
    """
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.left(90)
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.left(90)

def tete(s):
    """
    s:screen
    fonction pour dessiner une tête de mort reprenant d'autres fonctions définies précedements
    """
    tu.hideturtle()
    s.clear()
    bouche(-110, -100, 0)
    crane()
    yeux()
    tu.seth(315)
    os(-110+191.88, -100)
    tu.seth(201)
    os(-110-sqrt(5000), -100+sqrt(5000), False)
