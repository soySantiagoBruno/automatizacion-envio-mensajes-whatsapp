from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# 📄 Leer números desde archivo
def leer_numeros(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        return [f"549{linea.strip()}" for linea in lineas if linea.strip()]

# ✅ Mensaje que vas a enviar
mensaje = "Hola, te consulto tenes alojamiento disponible para 4 personas para este jueves 17? y que precio? Sería para pasar la noche ya que estamos de paso.."

# 🛠️ Ruta del archivo de números
archivo_numeros = "numeros.txt"
if not os.path.exists(archivo_numeros):
    print(f"⚠️ El archivo '{archivo_numeros}' no existe.")
    exit()

numeros_formateados = leer_numeros(archivo_numeros)

# 🧭 Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("📲 Escaneá el código QR con tu celular y presioná Enter para continuar...")

for numero in numeros_formateados:
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}"
    driver.get(url)
    time.sleep(10)  # Esperar que cargue el chat

    try:
        try:
            # Esperar hasta que aparezca el input de texto
            input_box = WebDriverWait(driver, 15).until(
                lambda d: d.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            )
            input_box.send_keys(Keys.ENTER)
            print(f"✅ Mensaje enviado a {numero}")
        
        except Exception as e:
            print(f"❌ No se pudo enviar a {numero}: {e}")


        print(f"✅ Mensaje enviado a {numero}")
    except Exception as e:
        print(f"❌ No se pudo enviar a {numero}: {e}")

    time.sleep(5)

driver.quit()
