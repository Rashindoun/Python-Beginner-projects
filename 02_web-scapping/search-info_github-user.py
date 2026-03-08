import requests 

def user_information():
    n_requetes = 0
    while True:
        if n_requetes < 30:
            print(f"vous etes actuellement à ({n_requetes}/60)")
        elif n_requetes == 30:
            print(f"attention , vous avez consomez la moitié de vos reques permise ({n_requetes}/60)")
        elif n_requetes == 60:
            print(f"vous avez atteint la limite maximal autorisez par l'api de github ({n_requetes}/60)")
            print("vous les vous bien attendre 1H")
            break
        user=input("quel est le nom de l'utilisateur que vous chercher : ")
        n_requetes +=1
        r = requests.get("https://api.github.com/users/"+user)
        if r.status_code == 200:
            data = r.json()
            print("voicit le nom de l'utilisateur : " ,data.get('login',""))
            print("voicit l'ID de l'utilisitateur : " ,data.get('id',))
            print("voicit la bio de l'utilisateur : " ,data.get('bio',))
            print("voicit le nombre de repo qu'a l'utilisateur : " ,data.get('public_repos',))
            print("voicit le nombre de followers de l'utilisateur : " ,data.get('followers',))
        else:
            print(f"attention , nous avons rencontrer une erreur lors du processus : {r.status_code}")
            break
        choix = input("voulez-vous utiliser encore le programme (O/n): ")
        if choix == "O":
            continue
        elif choix == "n":
            break

user_information()