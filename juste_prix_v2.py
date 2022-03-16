from random import randint
essais_max = 10
essais = 1
juste_prix = randint(0, 100)
print("Bienvenue au juste prix pour gagner introduisez le bon prix en 10 essais maximum")
votre_prix = int(input("Entrez votre prix entre 1 et 100 :"))

while essais < essais_max:
    if juste_prix > votre_prix:
        print("C'est plus")
        essais_max -= 1
        print(F"Votre nombre  d'essai", essais_max)
        votre_prix = int(input("Entrez le bon prix entre 1 et 100 pour gagner :"))
    elif juste_prix < votre_prix:
        print("C'est moins")
        essais_max -= 1
        print(F"Votre nombre  d'essai", essais_max)
        votre_prix = int(input("Entrez le bon prix entre 1 et 100 pour gagner :"))
    elif essais <= essais_max and juste_prix == votre_prix :
        print(F"Bravo!! tu as trouver",juste_prix, "en", essais_max, "essais")
        break
else:
        print(F"Vous avez utilisé vos 10 essais en vain.")
        print(F"le juste prix est", juste_prix)
