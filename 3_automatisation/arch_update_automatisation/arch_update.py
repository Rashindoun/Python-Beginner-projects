import requests
from bs4 import BeautifulSoup

def get_arch_news():
    responce = requests.get("https://archlinux.org/news/")
    html = responce.text
    if responce.status_code == 200:
        n = 1
        soup = BeautifulSoup(html, "html.parser")
        arch_news_content = soup.find_all("tr", limit = 4)
        for i in range (1,4):
            arch_news_content_temp = arch_news_content[i]
            news_title = arch_news_content_temp.find("a")
            news_date = arch_news_content_temp.find_all("td")
            news_date = news_date[0]
            news_title = news_title.get_text()
            news_date = news_date.get_text()
            print(f"{n}. {news_title} publié le {news_date}")
            n = n+1
    elif responce.status_code != 200:
        print(f"nous avons rencontrer une erreur dans le chargement de la page ({responce.status_code})")
    else:
        print("nous avons rencontrer une erreur externe au chargement de la pages")

get_arch_news()
            

        