import time 
import json

tasks = ["Dev TODO list en python","faire le repassage","faire a manger","abandonner le projet git en python"]

def show_task():
    print("-"*3 ," Show task " , "-"*3)
    n=1
    if len(tasks) > 0:
        print("voicit vos tache en cour :")
        for task in tasks:
            print(f"{n}. {tasks[n-1]}")
            n = n + 1
        print("#"*38)
    elif len(tasks) == 0:
        print("vous avez pas de tache a l'heure actuel")
        add_task()
        
def add_task():
    print("-"*3 ," remove task " , "-"*3)
    while True:
        choice = input("vous les vous ajouter des tache a votre TODO(O/n): ")
        if choice == "O":
            number = int(input("combien de tache a ajouter: "))
            if number == 0:
                print(f"entrée utilisateur impossibe ({number})")
                continue
            for i in range(1,number+1):
                future_task = input("quel est la tache a ajouter :")
                tasks.append(future_task)
            print(f"vos {number} taches ont bien été ajouté")
        elif choice == "n":
            break
        else:
            print(f"format de réponse non prise en charge ({choice})")
        break

def del_task():
    print("-"*3 ," add task " , "-"*3)
    del_index_number = int(input("numéro de la tache a supprimer : "))
    tasks.pop(del_index_number-1)
    print("la tache a bien été supprimé")
    
def modify_task():
    while True:
        choice = input("vous les vous changer (contenu/ordre): ")
        if choice == "ordre":
            temp_task = []
            n = int(input("numéro de la tache a rétrograder"))-1
            y = int(input("numéro de la tache a élever"))-1
            temp_task.extend((tasks[n],tasks[y]))
            tasks[n]=temp_task[1]
            tasks[y]=temp_task[0]
        elif choice == "contenu":
            n = int(input("numéro de la tache a changer"))-1
            new_content = intput("quel est le nouveaux contenue de la tache: ")
            tasks[n] = new_content
        else:
            print(f"le format de réponse réponse n'est pas bon: {choice}")
            continue
        break

def export():
    save = task
    with open("save_task.json" , "w+") as file:   
        file.write(save)
def import_task():
    with open("save_task.json" , "r+") as file:
        

def menu():
    while True:
        time.sleep(3)
        print("-"*3 ," Menu " , "-"*3)
        print("1. vous les vous voire vos tache en cour")
        print("2. vous les vous ajouter des tache a faire")
        print("3. vous les vous supprimer des tache ")
        print("4. vous les vous modifier les tache en cour")
        print("5. vous les vous partir de TODO liste")
        choice = int(input("qu'es ce que vous voulez chosir (1-5): "))
        print("#"*40)
        if choice == 1:
            show_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            del_task()
        elif choice == 4:
            modify_task()
        elif choice == 5:
            break

menu()
