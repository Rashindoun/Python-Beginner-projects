contacts= {
    "bob":{
        "numéro de téléphone":"06 65 76 89 99",
        "email":"bob@gmail.com",
        "pays":"France"
    },
    "alice":{
        "numéro de téléphone":"08 77 88 32 11",
        "email":"Alice@gmail.com",
        "pays":"Allemagne"
    },
    "sam":{
        "numéro de téléphone":"03 32 55 67 77",
        "email":"sam@gmail.com",
        "pays":"grande bretagne"
    },
    "micheal":{
        "numéro de téléphone":"11 78 55 34 87",
        "email":"michael@gmail.com",
        "pays":"suisse"
    },
    "george":{
        "numéro de téléphone":"15 98 00 30 23",
        "email":"george@gmail.com",
        "pays":"canada"
    }
}


def add_contacts():
    global contacts
    global contacts_name
    while True:
        new_contacts_name = input("quel est le nom de se contacts: ")
        if new_contacts_name not in contacts_name:
            new_contacts_phone_num =input("quel est le numéro de téléphone de ce contacts: ")
            if len(new_contacts_phone_num) == 14:
                pass
            else:
                print("numéro de téléphone non pris en charge (nb de caractère)") 
                continue
            choice=input(f"es ce que vous voulez ajouter: {new_contacts_name} au numéro {new_contacts_phone_num} (O/n): ")
            if choice == "O" or choice == "o":
                contacts[f"{new_contacts_name}"] = {"numéro de téléphone":new_contacts_phone_num} 
                print(f"{new_contacts_name} a bien été ajouté")
            elif choice == "n" or choice == "N":
                print(f"{new_contacts_name} n'a pas été ajouté")
            print("*"*10)
            more_information_choice = input(f"vous les vous ajouter plus d'information vis-à-vis de {new_contacts_name} ? (O/n): ")
            if more_information_choice == "O" :
                more_information_choice_email = input("voulez vous ajoutez un email ? (O/n) : ")
                if more_information_choice_email == "O": 
                    new_contacts_email = input(f"quel est l'email de {new_contacts_name} : ")
                    contacts[f"{new_contacts_name}"]["email"] = new_contacts_email
                elif more_information_choice_email == "n":
                    pass
                more_information_choice_contry = input("voulez vous ajoutez un pays ? (O/n) : ")
                if more_information_choice_contry == "O":
                    new_contacts_contry = input (f"quel est le pays de résidence de {new_contacts_name} : ")
                    contacts[f"{new_contacts_name}"]["pays"] = new_contacts_contry
                elif more_information_choice_contry == "n":
                    pass
            elif more_information_choice == "n":
                pass
            break
        else:
            print("contacts existant donc impossiblité d'excuté la fonction")
            continue


def del_contacts():
    while True:
        del_name = input("tapez le nom de celui que vous voulez supprimer : ")
        if del_name  in contacts_name:
            choix=input(f"es ce que vous voulez supprimer :{del_name} O/n: ")                                          
            if choix == "O":
                del contacts[f"{del_name}"]
                print(f"{del_name} a bien été supprimer")
            elif choix == "n":
                print(f"{del_name} a pas été supprimer")
        else:
            print("ce contact n'existe pas")
            continue
        break

def show_contacts():
    if len(contacts) > 0:
        print(f"voicit le nom de vos contacts :{list(contacts.keys())}")
        more_information_choice = input("voulez vous plus d'information vis a vis d'un de vos contacts (O/n): ")
        if more_information_choice == "O":
            contact = input("quel est le nom de se contact: ")
            print(contacts.get(f"{contact}","ce contact n'existe pas"))
        elif more_information_choice == "n":
            pass
    else:
        print("vous avez pas de contacts a l'heure actuel")
        choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
        if choix == "O":
            print("commençons donc maintenant :")
            add_contacts()
        elif choix == "n":
            print("domages peut etre une prochaine fois")
            break

def search_contacts():
    while True:
        if len(contacts) > 0:
            search = input("quel est le nom du contact que vous voulez cherchez : ")
            if search in contacts_name:
                print(f"voicit les info de ce contact: {search} , {contacts[f"{search}"]["numéro de téléphone"]} , {contacts[f"{search}"]["email"]} , {contacts[f"{search}"]["pays"]}")
                break
            else:
                print("ce contact n'existe pas")
        else:
            print("vous avez pas de contacts a l'heure actuel")
            choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
            if choix == "O" or choix == "o":
                print("commençons donc maintenant :")
                add_contacts()
            elif choix == "n" or choix == "N":
                print("domages peut etre une prochaine fois")
                break
        break    
        

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
        return


while True:
    contacts_name = list(contacts.keys())
    menu()