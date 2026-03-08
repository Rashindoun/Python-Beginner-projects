contacts= {
    "contact1":{
        "name":"bob",
        "numéro de téléphone":"06 65 76 89 99",
        "email":"bob@gmail.com",
        "pays":"France"
    },
    "contact2":{
        "name":"Alice",
        "numéro de téléphone":"08 77 88 32 11",
        "email":"Alice@gmail.com",
        "pays":"Allemagne"
    },
    "contact3":{
        "name":"sam",
        "numéro de téléphone":"03 32 55 67 77",
        "email":"sam@gmail.com",
        "pays":"grande bretagne"
    }
}

def add_contacts():
    while True:
        n = len(contacts)+1
        new_contacts_name = input("quel est le nom de se contacts: ")
        new_contacts_phone_num =input("quel est le numéro de téléphone de ce contacts: ")
        if len(new_contacts_phone_num) == 14:
            pass
        else:
            print("numéro de téléphone non pris en charge (nb de caractère)") 
            continue
        choix=input("es ce que vous voulez ajouter : "+ new_contacts_name+" au numéro "+ new_contacts_phone_num +" (O/n): ")
        if choix == "O" or choix == "o":
            contacts[f"contact{n}"]["name"]=new_contacts_name
            contacts[f"contact{n}"]["numéro de téléphone"]=new_contacts_phone_num
            print(new_contacts_name,"a bien été ajouté")
        elif choix == "n" or choix == "N":
            print(new_contacts_name,"n'a pas été ajouté")
        print("*"*10)
        more_information_choice = input(f"vous les vous ajouter plus d'information vis-à-vis de f{new_contacts_name} ? (O/n): ")
        if more_information_choice == "O" or more_information_choice == "o":
            new_contacts_email = input("quel est l'email de ",new_contacts_name," : ")
            new_contacts_pays = input ("quel est le pays de résidence de ",new_contacts_name," : ")
            print(new_contacts_name," a pour email : ",new_contacts_email," et pour pays de résidence : ",new_contacts_pays)
        choix = input("voulez vous ajoutez d'autre personne ? (O/n): ")
        if choix == "O" or choix == "o":
            continue
        elif choix == "n" or choix == "N":
            menu()


def del_contacts():
    while True:
        del_name = input("tapez le nom de celui que vous voulez supprimer : ")
        choix=input("es ce que vous voulez supprimer :"+del_name+" O/n")                         
        max = len(contacts_base)                  
        for i in range(1, max + 1):               
            contact = contacts.get(f"contact{i}")  
            if contact != None and contact.get("name") == del_name:     
                if choix == "O" or choix == "o":
                    del contacts[f"contact{i}"]
                    print(del_name,"a bien été supprimer")
                elif choix == "n" or choix == "N":
                    print(del_name,"a pas été supprimer")
        choix_continuer = input("voulez vous supprimer d'autre personne ? (O/n): ")
        if choix_continuer == "O" or choix_continuer == "o":
            continue
        elif choix_continuer == "n" or choix_continuer == "N":
            menu()

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
            menu()

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
    print("*"*38)
    print("*"*5+"  gestion de vos contacts  "+"*"*5)
    print("*"*38)
    print("1: ajouter un contact")
    print("2: supprimer un contact")
    print("3: montrer vos contacts")
    print("4: chercher un contact")
    print("5: quitter le gestionnaire de contacts")
    print("*"*38)
    choix = int(input("qu'es ce que vous voulez faire (1-5): "))
    print("*"*38)
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

menu()