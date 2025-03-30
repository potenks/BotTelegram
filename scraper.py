from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def get_followers(username):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta Chrome sin interfaz gráfica
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-cache")
    options.add_argument("--disk-cache-size=0")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    url = f"https://www.instagram.com/{username}/"
    driver.get(url)

    try:
        # Esperar a que el elemento esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[property="og:description"]'))
        )
        followers_element = driver.find_element(By.CSS_SELECTOR, 'meta[property="og:description"]')
        followers_text = followers_element.get_attribute("content")
        followers_count = followers_text.split(" ")[0]  # Extrae el número de seguidores
    except:
        followers_count = "Error"
    finally:
        driver.quit()
    
    return followers_count