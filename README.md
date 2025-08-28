# rpagen

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

├── rpa.py                  # Script principal de automação

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
