import requests 

def user_information():
    user=input("quel est le nom de l'utilisateur que vous chercher : ")
    r = requests.get("https://api.github.com/users/"+user)
    if r.status_code == 200:
        data = r.json()
        print("voicit le nom de l'utilisateur : " ,data.get('login',""))
        print("voicit l'ID de l'utilisitateur : " ,data.get('id',))
        print("voicit la bio de l'utilisateur : " ,data.get('bio',))
        print("voicit le nombre de repo qu'a l'utilisateur : " ,data.get('public_repos',))
        print("voicit le nombre de followers de l'utilisateur : " ,data.get('followers',))

    else:
        print("erreur d'accès au site web github")

user_information()