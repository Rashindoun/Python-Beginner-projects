contacts= {
    "contact3":{
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
    "contact1":{
        "name":"sam",
        "numéro de téléphone":"03 32 55 67 77",
        "email":"sam@gmail.com",
        "pays":"grande bretagne"
    }
}

def add_contacts():
    global contacts
    while True:
        n = len(contacts)+1
        new_contacts_name = input("quel est le nom de se contacts: ")
        new_contacts_phone_num =input("quel est le numéro de téléphone de ce contacts: ")
        if len(new_contacts_phone_num) == 14:
            pass
        else:
            print("numéro de téléphone non pris en charge (nb de caractère)") 
            continue
        choice=input(f"es ce que vous voulez ajouter: {new_contacts_name} au numéro {new_contacts_phone_num} (O/n): ")
        if choice == "O" or choice == "o":
            dict_temp = {
                f"contact{n}":{
                    "name":new_contacts_name,
                    "numéro de téléphone":new_contacts_phone_num
                }
            }
            new_dict = dict_temp | contacts
            contacts = new_dict | contacts
            print(f"{new_contacts_name} a bien été ajouté")
        elif choice == "n" or choice == "N":
            print(f"{new_contacts_name} n'a pas été ajouté")
        print("*"*10)
        more_information_choice = input(f"vous les vous ajouter plus d'information vis-à-vis de {new_contacts_name} ? (O/n): ")
        if more_information_choice == "O" or more_information_choice == "o":
            more_information_choice_email = input("voulez vous ajoutez un email ? (O/n) : ")
            if more_information_choice_email == "O" or more_information_choice_email == "o": 
                new_contacts_email = input(f"quel est l'email de {new_contacts_name} : ")
                contacts[f"contact{n}"]["email"] = new_contacts_email
            else:
                pass
            more_information_choice_contry = input("voulez vous ajoutez un pays ? (O/n) : ")
            if more_information_choice_contry == "O" or more_information_choice_contry == "o":
                new_contacts_contry = input (f"quel est le pays de résidence de {new_contacts_name} : ")
                contacts[f"contact{n}"]["pays"] = new_contacts_contry
            else:
                pass
        verification()


def del_contacts():
    while True:
        del_name = input("tapez le nom de celui que vous voulez supprimer : ")
        choix=input(f"es ce que vous voulez supprimer :{del_name} O/n")                         
        max = len(contacts)                  
        for i in range(1, max + 1):               
            contact = contacts.get(f"contact{i}")  
            if contact != None and contact.get("name") == del_name:     
                if choix == "O" or choix == "o":
                    del contacts[f"contact{i}"]
                    print(del_name,"a bien été supprimer")
                elif choix == "n" or choix == "N":
                    print(del_name,"a pas été supprimer")
        verification()

def show_contacts():
    while True:
        if len(contacts) > 0:
            contacts_name = {}
            for  i in range(1,len(contacts)+1):
                contacts_name[i] = contacts[f"contact{i}"]["name"]
            print(f"voicit le nom de vos contacts :{contacts_name.values()}")
        else:
            print("vous avez pas de contacts a l'heure actuel")
            choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
            if choix == "O" or choix == "o":
                print("commençons donc maintenant :")
                add_contacts()
            elif choix == "n" or choix == "N":
                print("domages peut etre une prochaine fois")
                menu()
        verification()

def search_contacts():
    while True:
        if len(contacts) > 0:
            search = input("quel est le nom du contact que vous voulez cherchez : ")
            bouche_troue = False
            contacts_name = {}
            for i in range(1,len(contacts)+1):
                contacts_name[i] = contacts[f"contact{i}"]["name"]
                match = contacts_name[i]
                if  match == search:
                    print(f"{search} existe belle est bien")
                    print(f"les information suivante de {search} sont : {contacts[f"contact{i}"]}")
                    bouche_troue = True # trouver une meilleur solution
                    break
            if bouche_troue != True:
                print(f"{search} est introuvable")

        else:
            print("vous avez pas de contacts a l'heure actuel")
            choix = input("Comme vous avez pas de contacts . Es ce que il serait pas donc le temps dans ajouter quelque un : O/n")
            if choix == "O" or choix == "o":
                print("commençons donc maintenant :")
                add_contacts()
            elif choix == "n" or choix == "N":
                print("domages peut etre une prochaine fois")
                menu()
        verification()

def verification():
    while True:
        choix_continuer = input("vous les vous continuer vos action (O/n) : ")
        if choix_continuer == "O" or choix_continuer == "o":
            return
        elif choix_continuer == "n" or choix_continuer == "N":
            menu()
        else:
            print(f"choix non pris en charge {choix_continuer}")
            continue

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


menu()