from random import randint

print("Bienvenu au juste prix !")
juste_prix = randint(0,100)

while True:
    votre_prix = int(input("Entrer le bon prix pour gagner :"))    
    if juste_prix > votre_prix:
        print("Le juste prix est supérieur au votre")
        
    elif juste_prix < votre_prix:
        print("le juste prix est inférieur au votre")
        
    elif juste_prix == votre_prix:
         print(F"Vous avez gagné !! Voici le juste prix",juste_prix)
         break
