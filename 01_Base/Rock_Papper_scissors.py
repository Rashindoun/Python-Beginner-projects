import random

while True:
    choix_joueur = input("Pierre, Papier ou Ciseaux ? ")
    choix_ordi = random.choice(["Pierre", "Papier", "Ciseaux"])

    choix_autoriser = ["Pierre","Papier","Ciseaux"]
    if choix_joueur in choix_autoriser:
        print("le choix de l'ordinateur est",choix_ordi)
        if choix_joueur == choix_ordi:
            print("Égalité !")
        elif choix_joueur == "Pierre" and choix_ordi == "Ciseaux":
            print("joueur vainceur!")
        elif choix_joueur == "Papier" and choix_ordi == "Pierre": 
            print("joueur vainceur!")
        elif choix_joueur == "Ciseaux" and choix_ordi == "Papier":
            print("joueur vainceur!")
        else:
            print("l ordinateur a gagné")
        #partit pour donner le choix de contineur ou non pour éviter les break    
        rejouer=input("vous vouler rejouez ? o/n ")
        if rejouer == "o" or rejouer == "O":
            print("Une partit de plus!")
            continue
        elif rejouer == "n" or rejouer == "N":
            print("Pour une prochaine fois ...")
            break
    else:
        print("sorry mais tu as fait un choix impossible")
        break