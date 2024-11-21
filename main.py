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
url = "https://previsionieuro.com/tesla#google_vignette"

try:
    # Apri il browser
    driver.get(url)

    # Attendi 5 secondi per caricare la pagina
    time.sleep(5)

# per poter cliccare i banner 

    #banner
    xpathAccetta = "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]/p"
    
    button_accetta = driver.find_element(By.XPATH, xpathAccetta)
    button_accetta.click()
    
    time.sleep(5)

  #primo elemento
    xpath = "/html/body/div[1]/div/div/main/article/div/div[1]/div[1]/table/tbody/tr[2]/td[5]/strong"
    first_element = driver.find_element(By.XPATH, xpath)
    uno = first_element.text

    print("il primo elemento é " + uno)

finally:
    # Chiudi il browser
    driver.quit()








    

    
    
  

