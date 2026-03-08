contacts = {"bob": "08 09 87 66 11", "Alice": "05 65 55 67 99", "Sam": "10 89 77 66 85"}

def add_contacts():
    new_contacts_name = input("quel est le nom de se contacts: ")
    new_contacts_phone_num =input("quel est le numéro de téléphone de ce contacts: ")
    choix=input("es ce que vous voulez ajouter :"+ new_contacts_name + "au numéro"+ new_contacts_phone_num +" O/n")
    if choix == "O" or choix == "o":
        contacts[new_contacts_name]=new_contacts_phone_num
        print(new_contacts_name,"a bien été ajouté")
    elif choix == "n" or choix == "N":
        print(new_contacts_name,"n'a pas été ajouté")

def del_contacts():
    print("voicit le nom de vos contact :")
    del_name = input("tapez le nom de celui que vous voulez supprimer : ")
    choix=input("es ce que vous voulez supprimer :"+del_name+" O/n")
    if choix == "O" or choix == "o":
        del contacts[del_contacts]
        print(del_name,"a bien été supprimer")
    elif choix == "n" or choix == "N":
        print(del_name,"a pas été supprimer")

def show_contacts():
    if len(contacts) > 0:
        print("voicit le nom de vos contacts :",contacts.keys())
        print("voicit le numéro de téléphone de vos contacts",contacts.values())
    else:
        print("vous avez pas de contacts a l'heure actuel")
        choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
        if choix == "O" or choix == "o":
            print("commençons donc maintenant :")
            add_contacts()
            print(del_name,"a bien été supprimer")
        elif choix == "n" or choix == "N":
            print("domages peut etre une prochaine fois")

def search_contacts():
    if len(contacts) > 0:
        search =input("quel est le nom du contact que vous voulez cherchez : ")
        name = search in contacts
        if name == True:
            print("ce contact existe belle et bien")
        else:
            print("ce contact n'existe pas")
    else:
        print("vous avez pas de contacts a l'heure actuel")
        choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
        if choix == "O" or choix == "o":
            print("commençons donc maintenant :")
            add_contacts()
            print(del_name,"a bien été supprimer")
        elif choix == "n" or choix == "N":
            print("domages peut etre une prochaine fois")

def menu():
    print("-- gestion de vos contacts --")
    print("1: ajouter un contact")
    print("2: supprimer un contact")
    print("3: montrer vos contacts")
    print("4: chercher un contact")
    print("5: quitter le gestionnaire de contacts")
    choix = input(" qu'es ce que vous voulez faire (1-5): ")
    if choix == 1:
        add_contacts()
    elif choix == 2:
        del_contacts()
    elif choix == 3:
        show_contacts()
    elif choix == 4:
        search_contacts()
    elif choix == 5:
        print("A une prochaine fois!")