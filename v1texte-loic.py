import random as rd
n=rd.randint(0,30)
gagnant=False
def regle():
    REGLE=[]
    for i in range(rd.randint(1,5)):
        REGLE.append(rd.randint(1,n))
    return REGLE
def afficheRegle(REGLE):
    for x in REGLE :
        print(x,end=" ")

        
def Maj_allumettes(allumettes_prises):
    val=False
    while val != True :
        try :
            nombre=int(allumettes_prises)
            val=True
        except:
            allumettes_prises=input("Entrer un nouveau nombre d'allumettes prises :")
    while int(allumettes_prises) not in REGLE or int(allumettes_prises)>n:
            print("Le nombre ",allumettes_prises,"est incorrect")
            allumettes_prises=input("Entrer un nouveau nombre d'allumettes prises :")
    return n-int(allumettes_prises)
def verifJeuPossible(allumettes_prises,REGLE):
    if 
def allumettes(n):
    while not gagnant :
        REGLE=regle()
        print("Vous pouvez choisir le nombre d'allumette parmi les suivants : ",end=" ")
        afficheRegle(REGLE)
        allumettes_prises=input("Combien d'allumette voulez-vous prendre ?")
        n=Maj_allumettes(allumettes_prises)
        if n==0 :
            gagnant=True
        else :
            allumettes_prises=rd.choice(REGLE)
            
        
        
        
    
    
