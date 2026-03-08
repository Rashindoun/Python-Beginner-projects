def calculateur_age():
    année_actuel=int(input("quel année sommes nous :"))
    date_de_naissance=int(input("quel est votre date de naissance :"))
    age=année_actuel-date_de_naissance
    print("votre ages est :",age)

calculateur_age()