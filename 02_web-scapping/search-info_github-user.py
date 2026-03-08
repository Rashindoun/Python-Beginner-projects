import requests 

#fonction principal du projet github-user-info
def user_information():
    #gestion du nombre de requète en fonction de la variable n_requete (penser ajouter aussi un système de timer)
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
        n_requetes +=2
        response = requests.get(f"https://api.github.com/users/{user}")
        response_repo = requests.get(f"https://api.github.com/users/{user}/repos")
        if response.status_code == 200:
            data = response.json()
            donnés = response_repo.json()
            print(f"L'utilisateur: {data.get('login')}")
            print("📊 Infos :")
            print(f"ID: {data.get('id')}")
            print(f"Bio: {data.get('bio')}")
            print(f"followers: {data.get('followers')}")
            print("📚 Ses repos :")
            print(f"Nombre de repo: {data.get('public_repos')}")
            n = 0
            for donné in donnés:
                print(f"{n}. {donné['name']} (⭐ {donné['stargazers_count']})")
                n += 1
        else:
            if response.status_code != 200:
                print(f"attention , nous avons rencontrer une erreur lors du processus : {response.status_code}")
                break
            else:
                print(f"attention , nous avons rencontrer une erreur lors du processus : {response_repo.status_code}")
        # gestion de la boucle
        choix = input("voulez-vous utiliser encore le programme (O/n): ")
        if choix == "O":
            continue
        elif choix == "n":
            break

user_information()