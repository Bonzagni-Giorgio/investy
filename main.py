from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import chromedriver_autoinstaller

# service = Service("chromedriver")  # Cambia "chromedriver" con il percorso completo se necessario
# driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()



# Create a webdriver instance
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options)

# URL target (azioni più attive su Yahoo Finance)
url = "https://finance.yahoo.com/most-active"

try:
    # Apri il browser
    driver.get(url)

    # Attendi 5 secondi per caricare la pagina
    time.sleep(5)


# prova

    #banner
    xpathAccetta = "/html/body/div/div/div/div/form/div[2]/div[2]/button[1]"
    
    button_accetta = driver.find_element(By.XPATH, xpathAccetta)
    button_accetta.click()
    
    time.sleep(5)
    

    
    
    #titolo
    xpath = "//*[@id='nimbus-app']/section/section/section/article/section[1]/header/h2"
    
    title_element = driver.find_element(By.XPATH, xpath)
    title = title_element.text

    print("il titolo é" + title)

finally:
    # Chiudi il browser
    driver.quit()