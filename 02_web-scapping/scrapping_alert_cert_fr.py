import requests
from bs4 import BeautifulSoup

def scraping_alert_cert_fr():
    responce = requests.get('https://www.cert.ssi.gouv.fr/')
    main_page = responce.content
    if responce.status_code == 200:
        soup = BeautifulSoup(main_page,'html.parser')
        alerts_cert_fr = soup.find_all("div" , class_ = "item cert-alert open" , limit = 100)
        for i in range(0,len(alerts_cert_fr)):
            alerts_cert = alerts_cert_fr[i]
            alerts_cert_title = alerts_cert.find_all("a")
            alerts_date = alerts_cert.find("span",class_ = "item-date")
            print(alerts_cert_title)
            alerts_title = alerts_cert_title[1]
            alerts_title = alerts_title.get_text()
            alerts_date = alerts_date.get_text()
            print(f"voicit les alerte en court : {alerts_title} depuis {alerts_date}")
    elif responce.status_code != 200:
        print(f"nous avons rencontrer une erreur ({responce.status_code})")

scraping_alert_cert_fr()