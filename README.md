# Android Test Automation Project

Este projeto é uma aplicação de automação de testes para dispositivos Android utilizando Python, Appium e pytest. O objetivo é fornecer uma base para testar aplicativos Android, como a calculadora, câmera e contatos, de forma automatizada.

## Pré-requisitos

Antes de começar, você precisará ter os seguintes softwares instalados no seu computador:

- [Python](https://www.python.org/downloads/) (versão 3.x)
- [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [Android Studio](https://developer.android.com/studio) (inclui o Android SDK)
- [Node.js](https://nodejs.org/) (necessário para Appium)
- [Appium Desktop](https://github.com/appium/appium-desktop/releases)

## Configuração do Ambiente

1. **Instale o Python**, o JDK e o Android Studio conforme as instruções nos links acima.
2. **Configure as variáveis de ambiente** para o JDK e o Android SDK.
3. **Instale o Appium** via npm:

   ```bash
   npm install -g appium
Crie um ambiente virtual para o projeto:
mkdir android_test_project
cd android_test_project
python -m venv venv
venv\Scripts\activate  # No Windows

Instale as dependências do projeto:
pip install Appium-Python-Client pytest pytest-html


Estrutura do Projeto

android_test_project/
│
├── venv/                  # Ambiente virtual
├── test_android.py        # Script de testes
└── report.html            # Relatório gerado pelos testes
Executando os Testes
Inicie o servidor Appium:

bash
Copiar código
appium
Execute os testes com pytest:

bash
pytest test_android.py
O relatório será gerado em report.html.

Funcionalidades
Teste da Calculadora: Realiza operações básicas (ex: 1 + 2).
Teste da Câmera: Abre a câmera e tira uma foto.
Teste dos Contatos: Acessa o aplicativo de contatos e simula uma interação.
Contribuição
Se você deseja contribuir para o projeto, sinta-se à vontade para abrir um pull request ou relatar problemas. Todas as contribuições são bem-vindas!

Licença
Este projeto é licenciado sob a MIT License.









