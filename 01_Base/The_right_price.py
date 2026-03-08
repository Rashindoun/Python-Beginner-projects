import random
def juste_prix():
    n_tour=0
    numéro_chercher= random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    while True:
        print("vous etes au tour ",n_tour)
        proposition_joeur = int(input("quel est votre proposition :"))
        n_tour= n_tour+1
        if numéro_chercher == proposition_joeur:
            print("vous avez trouver le juste prix")
            print("voicit votre score : ",n_tour)
            break
        elif proposition_joeur > 30 or proposition_joeur < 0 :
            print("vous etes hors de la fourchette de prix")
            break
        elif proposition_joeur < numéro_chercher:
            print("c'est plus !")
        elif proposition_joeur > numéro_chercher:
            print("c'est moins !") 
        
    
juste_prix()

rejouer=input("vous vouler rejouez ? o/n ")
if rejouer == "o" or rejouer == "O":
    print("Une partit de plus!")
    juste_prix()
elif rejouer == "n" or rejouer == "N":
    print("Pour une prochaine fois ...")
