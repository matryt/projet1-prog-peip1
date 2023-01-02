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


def dessinePolygone(cotes, longueur, x, y, t, couleur):
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


def dessineCercle(x, y, t, couleur, longueur):
    """
    x:int position en abscisse
    y:int position en ordonnée
    t turtle
    couleur:str or tuple 
    longueur:float/int
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

def numero(coords, n, t, couleur):
    """
    Permet d'écrire un numéro aux coordonnées spécifiées
    :param coords: Les coordonnées du texte
    :type coords: tuple
    :param n: Le numéro à afficher
    :type n: int
    :param t: La tortue à utiliser
    :type t: Turtle
    :param couleur: couleur texte
    :type couleur: str or tuple
    """
    t.up()
    t.goto(coords[0], coords[1])
    t.down()
    t.color(couleur)
    t.write('Tas ' + str(n), align="center",font=('Arial',16,"bold"))

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
        tu.forward(154.96)
    else:
        tu.forward(135.2)
    tu.right(70.47)
    tu.forward(42.64)
    tu.left(54.03)
    tu.forward(41.08)
    tu.left(45.28)
    tu.forward(49.92)
    tu.left(46.512)
    tu.forward(42.12)
    tu.left(39.02)
    tu.forward(34.32)
    tu.left(71.08)
    tu.forward(18.2)
    tu.left(180)
    tu.forward(18.2)
    tu.left(27.56)
    tu.forward(19.76)
    tu.left(54.61)
    tu.forward(55.12)
    tu.left(51.3)
    tu.forward(34.32)
    tu.left(42.74)
    tu.forward(50.96)
    tu.left(48.79)
    tu.forward(33.8)
    tu.left(18.55)
    tu.forward(29.12)
    tu.right(71.93)
    if not droite:
        tu.forward(154.96)
    else:
        tu.forward(135.2)
    tu.left(105.09)
    tu.down()
    tu.up()
    tu.forward(79.04)
    tu.forward(-79.04)
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
