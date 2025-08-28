from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Configuração do driver (exemplo com Chrome)
driver = webdriver.Chrome()

# URL do sistema
url = "https://www.exemplo.com/login"
driver.get(url)

# Login
usuario = "seu_usuario"
senha = "sua_senha"

# Localiza os campos e faz login
driver.find_element(By.ID, "campo_usuario").send_keys(usuario)
driver.find_element(By.ID, "campo_senha").send_keys(senha)
driver.find_element(By.ID, "botao_login").click()

# Aguarda o carregamento
time.sleep(5)

# Lê o Excel
df = pd.read_excel("dados.xlsx")

# Loop para inserir dados
for index, row in df.iterrows():
    # Navega até a página de input
    driver.get("https://www.exemplo.com/formulario")

    # Preenche os campos
    driver.find_element(By.ID, "campo_nome").send_keys(row["Nome"])
    driver.find_element(By.ID, "campo_idade").send_keys(str(row["Idade"]))
    driver.find_element(By.ID, "campo_email").send_keys(row["Email"])

    # Envia o formulário
    driver.find_element(By.ID, "botao_enviar").click()

    # Aguarda antes de continuar
    time.sleep(2)

# Finaliza
driver.quit()
