from random import randint

print("Bienvenue au juste prix, choisissez votre difficulté, facile(1), normal(2), personnalisé(3)")
lvl = int(input("Choisissez votre niveau : "))

if lvl == 1:
     juste_prix = randint(1, 100)    
     print("Difficulté facile, pour gagner introduisez le bon prix entre 1 et 100")
     while True:
        votre_prix = int(input("Entrer le bon prix pour gagner :"))    
        if juste_prix > votre_prix:
         print("C'est plus")
        
        elif juste_prix < votre_prix:
         print("C'est moins")
        
        elif juste_prix == votre_prix:
         print(F"Vous avez gagné !! Voici le juste prix",juste_prix)
         break
        
elif lvl == 2:
     essais_max = 10
     essais = 1
     tentative=0
     juste_prix = randint(1, 100)
     print("Difficulté normale, pour gagner introduisez le bon prix entre 1 et 100 en 10 essais maximum")
     votre_prix = int(input(" Entrez le bon prix entre 1 et 100 pour gagner : "))
     while essais < essais_max:
        tentative += 1

        if juste_prix > votre_prix:
         print("C'est plus")
         essais_max -= 1
         print(F"Votre nombre  d'essai", essais_max)
         votre_prix = int(input("Entrez le bon prix entre 1 et 100 pour gagner : "))

        elif juste_prix < votre_prix:
         print("C'est moins")
         essais_max -= 1
         print(F"Votre nombre  d'essai", essais_max)
         votre_prix = int(input("Entrez le bon prix entre 1 et 100 pour gagner :"))

        elif essais <= essais_max and juste_prix == votre_prix :
         print(F"Bravo!! vous avez trouver",juste_prix, "en", tentative, "essais")
         break
     else:
        print(F"Vous avez utilisé vos 10 essais en vain.")
        print(F"le juste prix était", juste_prix)

elif lvl == 3:
       print("Mode personnalisé, Veuillez choisir votre nombre maximal et le nombre d'essais")
       max = int(input("Choisissez votre chiffre max : "))
       essais_max = int(input("Choisissez le nombre d'essais : "))
       essais = 0
       juste_prix = randint(1, max)
       tentative = 0

       if essais_max == 0:
         mode = False
         essais_max = 4 

       while essais < essais_max :
        votre_prix = int(input("Entrer le bon prix pour gagner : ")) 
        tentative += 1

        if juste_prix > votre_prix:
         essais_max -= 1
         print("C'est plus")
         print(F"Votre nombre d'essais", essais_max)

        elif juste_prix < votre_prix:
         essais_max -= 1
         print("C'est moins")
         print(F"Votre nombre d'essais", essais_max)
         
           
        elif juste_prix == votre_prix :
         print(F"Bravo!! vous avez trouver",juste_prix, "en",tentative, "essais")
         exit()
         
       else:
         print(F"Vous avez utilisé vos essais en vain.")
         print(F"le juste prix étaitt", juste_prix)