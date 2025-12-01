from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Ruta del chromedriver dentro de la carpeta
service = Service(r"C:\Users\DELL\Desktop\mini_gestor_contactos_elys\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 1. Abrir la aplicación
driver.get("http://127.0.0.1:5000")
time.sleep(1)

print("Página cargada correctamente.")

# 2. Crear un nuevo contacto
driver.find_element(By.LINK_TEXT, "➕ Crear nuevo contacto").click()
time.sleep(1)

driver.find_element(By.NAME, "name").send_keys("Elys Test")
driver.find_element(By.NAME, "phone").send_keys("123456789")
driver.find_element(By.NAME, "email").send_keys("elys@test.com")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

print("Contacto creado.")

# 3. Editar el primer contacto
driver.find_element(By.LINK_TEXT, "Editar").click()
time.sleep(1)

campo_nombre = driver.find_element(By.NAME, "name")
campo_nombre.clear()
campo_nombre.send_keys("Elys Editada")

driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

print("Contacto editado.")

# 4. Eliminar contacto
driver.find_element(By.LINK_TEXT, "Eliminar").click()
time.sleep(1)

print("Contacto eliminado.")

# 5. Cerrar navegador
driver.quit()
print("Prueba finalizada con éxito.")
