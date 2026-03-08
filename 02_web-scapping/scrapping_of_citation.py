import requests
from bs4 import BeautifulSoup

def scrapping_citation():
    while True:
        pages = None # bout de code pour prévoire peut etre un moyen d'augementer le nombre de citation et d'auteur
        responce = requests.get("https://quotes.toscrape.com/")
        html = responce.text
        if responce.status_code == 200:
            soup = BeautifulSoup(html, "html.parser")
            authours = soup.find_all("small", class_ = "author")
            authours_cleans = []
            citations = soup.find_all("span",class_="text")
            citations_cleans = []
            n = 1
            for authour in authours:
                texte = authour.text.strip()
                authours_cleans.append(texte)
            for citation in citations:
                texte = citation.text.strip()
                citations_cleans.append(texte)
            with open(f"citation{pages}.txt" ,"w") as file:
                for citations_clean  in citations_cleans :
                    file.write(citations_clean+"\n")
            with open(f"auteur{pages}.txt" ,"w" ) as file:
                for authours_clean in authours_cleans:
                    file.write(authours_clean +"\n")
        else:
            print(f"une erreur est survenue : {responce.status_code}")
        #gestion de la boucle et des autre moyen d'augementer le nombre de page
        choix = input("veut tu continuer a imprimer d'autre pages de citation ? (O/n) : ")
        if choix == "O" or choix == "o":
            print("une de plus !")
            continue
        if choix == "n" or choix == "N":
            print("A la prochaine ")
            break


scrapping_citation()