import random
def trouverNombreSecret():
    nombre_secret = random.randint(0, 100)
    coups = 0
    valeurs_saisies = []
    while True:
        coups += 1
        valeur_proposee = int(input("Proposez un nombre entre 0 et 100 : "))
        valeurs_saisies.append(valeur_proposee)
        if valeur_proposee < nombre_secret:
            print("Le nombre est trop petit.")
        elif valeur_proposee > nombre_secret:
            print("Le nombre est trop grand.")
        else:
            print(f"Bravo, vous avez trouvé le nombre secret en {coups} coups !")
            return True, coups, valeurs_saisies
        if coups >= 9:
            print(f"Désolé, vous n'avez pas trouvé en 10 coups. Le nombre secret était {nombre_secret}.")
            return False, coups, valeurs_saisies
        
#appel fonction
trouverNombreSecret()