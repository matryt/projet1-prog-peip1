from random import randint, choice

REGLE = [1, 2, 3]
fini = False

nombreAllumettes = randint(10, 20)

def minimum(l):
    return l[0]

def enleverAllumettes(allumettes, regle):
    nombre = input(f"Joueur, combien voulez-vous prendre d'allumettes ?")

    while type(nombre) != int:
        try:
            nombre = int(nombre)
        except:
            print("Vouz devez rentrer un nombre !")
            nombre = input("Joueur, combien voulez-vous prendre d'allumettes ?")
    
    while nombre > allumettes or nombre not in regle:
        print(f"Vous voulez prendre {nombre} allumettes, ce qui est impossible !")
        nombre = int(input(f"Joueur, combien voulez-vous prendre d'allumettes ?"))

    return allumettes - nombre
    
def afficherAllumettes(allumettes):
    for i in range(allumettes):
        print('|', end=" ")
    print("\n")

def jeuPossible(allumettes, regle):
    m = minimum(regle)
    return allumettes != 0 and allumettes - m < 0

def tirageOrdi(allumettes):
    c = choice(REGLE)
    while c > allumettes:
        c = choice(REGLE)
    allumettes -= c
    print(f"L'ordi a pris {c} allumettes")
    return allumettes

REGLE.sort()

while not fini:
    afficherAllumettes(nombreAllumettes)
    nombreAllumettes = enleverAllumettes(nombreAllumettes, REGLE)
    allumettesVides = nombreAllumettes == 0
    if allumettesVides or not jeuPossible(nombreAllumettes, REGLE):
        if allumettesVides:
            print("Bravo, vous avez gagné !")
            fini = True
        else:
            print("Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
            fini = True
    else:
        afficherAllumettes(nombreAllumettes)
        nombreAllumettes = tirageOrdi(nombreAllumettes)
        if nombreAllumettes == 0:
            print("Malheureusement l'ordi a gagné ! Peut-être la prochaine fois !")
            fini = True
        if not jeuPossible(nombreAllumettes, REGLE):
            print("Le nombre d'allumettes est tel qu'il n'est plus possible de jouer ! Match nul.")
            fini = True
