import requests as r

def download():
    choix = input("qu'es ce que vous voulez télécharger (Text/Images) : ")
    url_doc=input("qu'elle est l'url de votre "+choix+": ")
    responce = r.get(url_doc)
    if responce.status_code == 200:
        if choix == "Text" or choix == "text":
            with open("text.txt","w+") as Text:
                Text.write(responce.text)
                print("le télchargement a bien été excuté")
        elif choix == "Images" or choix == "images":
            with open("Image.png","wb") as picture:
                picture.write(responce.content)
    elif responce.status_code != 200:
        print("le téléchargement a été interrompu")
    else:
        print("format non supporté")

download()