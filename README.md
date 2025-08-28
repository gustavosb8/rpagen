# rpagen
# English below


🛠️ RPA Web Automation com Python

Este projeto é um robô de automação de processos (RPA) desenvolvido em Python, que acessa um sistema web, realiza login com usuário e senha, e insere dados automaticamente a partir de uma planilha Excel.

🚀 Funcionalidades

Acesso automático a sistemas web via navegador.

Login com credenciais fornecidas.

Leitura de dados de um arquivo Excel (.xlsx).

Preenchimento de formulários web com os dados da planilha.

Interações com elementos da tela usando pyautogui (cliques, movimentos, etc).

📦 Tecnologias Utilizadas

Python 3

Selenium

PyAutoGUI

Pandas

OpenPyXL

📁 Estrutura do Projeto

rpa-web/

│

├── dados.xlsx              # Planilha com os dados a serem inseridos

├── rpagen.py                  # Script principal de automação

├── README.md               # Documentação do projeto

📋 Requisitos
Instale as dependências com:
pip install selenium pandas openpyxl pyautogui

⚙️ Como Usar
Edite o arquivo rpagen.py com:

A URL do sistema web.
Os IDs ou seletores dos campos de login e formulário.
As coordenadas de tela para cliques com pyautogui.
Prepare o arquivo dados.xlsx com as colunas esperadas (ex: Nome, Idade, Email).

Execute o script:
python rpagen.py

🧠 Observações
O uso de pyautogui é recomendado para sistemas que não permitem automação direta via DOM.
Certifique-se de que a resolução da tela e a posição dos elementos estejam corretas para evitar falhas.


################################################################################################################################################################################################################################################

🛠️ RPA Web Automation with Python

This project is a Robotic Process Automation (RPA) script built with Python. It automates access to a web system, logs in using credentials, and inputs data from an Excel spreadsheet into web forms.

🚀 Features
Automated access to web systems via browser.

Login using username and password.

Reads data from an Excel file (.xlsx).

Fills out web forms with spreadsheet data.

Uses pyautogui for screen interactions (clicks, movements, etc.).

📦 Technologies Used

Python 3

Selenium

PyAutoGUI

Pandas

OpenPyXL

📁 Project Structure

rpa-web/

│

├── dados.xlsx              # Spreadsheet with input data

├── rpa.py                  # Main automation script

├── README.md               # Project documentation

📋 Requirements
Install dependencies with:
pip install selenium pandas openpyxl pyautogui

⚙️ How to Use

Edit the rpagen.py file with:

The URL of the web system.
The IDs or selectors of login and form fields.
Screen coordinates for pyautogui clicks.
Prepare the dados.xlsx file with the expected columns (e.g., Name, Age, Email).

Run the script:
python rpa.py

🧠 Notes
pyautogui is recommended for systems that do not allow direct DOM automation.
Make sure screen resolution and element positions are correct to avoid errors.
