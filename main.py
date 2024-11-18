
import requests
from bs4 import BeautifulSoup

# URL 
url = "https://finance.yahoo.com/markets/stocks/most-active/"  # Sostituisci con il sito desiderato

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# richiesta GET al sito
response = requests.get(url, headers=headers)

# Verifica la richiesta 
if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

    titles = soup.find_all('h1')  # Cambia 'h1' con altri tag se necessario
    paragraphs = soup.find_all('p')

    # Stampa 
    print("Titoli trovati:")
    for title in titles:
        print(f"- {title.text.strip()}")

else:
    print(f"Errore durante la richiesta: {response.status_code}")