from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Ruta al chromedriver dentro de tu carpeta
service = Service("./chromedriver.exe")

# Inicializar navegador
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Ejemplo: buscar algo
search = driver.find_element(By.NAME, "q")
search.send_keys("hola elys")
search.submit()
