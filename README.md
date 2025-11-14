# CraseApp: Validador de Crase

Este projeto é uma aplicação web desenvolvida com o framework **Django** que tem como objetivo validar a ocorrência da crase em combinações de termos regentes e regidos, aplicando a lógica gramatical de forma programática.

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias principais:

![Tecnologias](https://skillicons.dev/icons?i=python,django,mysql,html,css )

| Tecnologia | Função no Projeto |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **Django** | Framework web para o desenvolvimento da aplicação. |
| **MySQL/MariaDB** | Sistema de gerenciamento de banco de dados (SGBD) para persistência dos dados de mapeamento e regras. |
| **HTML & CSS** | Estrutura e estilização da interface do usuário. |

## 🏗️ Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com algumas configurações específicas:

djangodjango/
├── craseapp/             # Aplicação principal (App)
│   ├── migrations/
│   ├── templates/
│   │   └── craseapp/     # Templates HTML específicos da aplicação
│   ├── init.py
│   ├── admin.py          # Configuração do painel administrativo
│   ├── apps.py
│   ├── forms.py          # Definição do formulário de consulta
│   ├── models.py         # Definição dos modelos (TermoRegente, TermoRegido, MapeamentoCrase, Regra)
│   ├── tests.py
│   ├── urls.py           # Rotas da aplicação
│   └── views.py          # Lógica de negócio (Validação e Consulta Dinâmica)
├── craseproject/         # Configurações do Projeto (Project)
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py       # Configurações principais (DB, Apps, Templates, Static)
│   ├── urls.py           # Rotas globais do projeto
│   └── wsgi.py
├── manage.py             # Utilitário de linha de comando do Django
└── static/               # Arquivos estáticos globais (ex: styles.css)
└── styles.css
Plain Text

## ⚙️ Como Foi Feito (Instruções de Configuração)

O desenvolvimento seguiu os passos típicos de um projeto Django com banco de dados externo:

### 1. Configuração do Ambiente

*   **Instalação do Django:** O projeto foi iniciado com a instalação do framework Django.
*   **Instalação do Driver MySQL:** Foi necessário instalar o driver de conexão do Python com o MySQL (ex: `mysqlclient`).

### 2. Configuração do Banco de Dados

O arquivo `craseproject/settings.py` foi configurado para utilizar o **MySQL** (ou MariaDB) como SGBD, conforme as linhas 65-77:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Motor do MariaDB/MySQL
        'NAME': 'djangodjango',                  # O nome do SEU banco no Workbench
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',                  # Geralmente 127.0.0.1
        'PORT': '3306',                       # Porta padrão do MySQL/MariaDB
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
Atenção: Para rodar o projeto, é fundamental que o banco de dados djangodjango esteja criado no seu SGBD e que as credenciais (USER, PASSWORD, HOST, PORT) estejam corretas.
3. Modelagem e Lógica de Crase
Modelos (craseapp/models.py): Foram criados modelos para:
TermoRegente: Define se o termo exige a preposição 'a'.
TermoRegido: Define se o termo aceita o artigo 'a'.
Regra: Para catalogar regras gramaticais específicas.
MapeamentoCrase: Relaciona um regente e um regido, e opcionalmente uma regra, para mapear a ocorrência da crase.
Lógica de Validação (craseapp/views.py): A lógica central da crase é implementada na função validar_crase e consulta_dinamica, que se baseia na regra fundamental:
Crase Ocorre se e somente se o Termo Regente exige a preposição 'a' E o Termo Regido aceita o artigo 'a'.
A função consulta_dinamica utiliza um formulário (ConsultaCraseForm em craseapp/forms.py) para permitir que o usuário selecione dinamicamente os termos e veja o resultado da validação.
4. Configurações Adicionais
Internacionalização: O settings.py foi ajustado para o padrão brasileiro: LANGUAGE_CODE = 'pt-br' e TIME_ZONE = 'America/Sao_Paulo'.
Templates e Estáticos: Os diretórios templates e static foram configurados no nível do projeto para facilitar a organização de arquivos base (base.html) e estilos globais (styles.css).
💻 Como Rodar o Projeto
Clone o repositório:
Bash
git clone https://github.com/gabriel7alencar/djangodjango.git
cd djangodjango
Crie e ative um ambiente virtual (recomendado ):
Bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate   # No Windows
Instale as dependências (assumindo que você tem um requirements.txt ou precisa instalar o Django e o driver MySQL):
Bash
# Exemplo de instalação
pip install Django mysqlclient
Configure o Banco de Dados:
Crie o banco de dados djangodjango no seu SGBD (MySQL/MariaDB).
Ajuste as credenciais em craseproject/settings.py se necessário.
Aplique as Migrações:
Bash
python manage.py makemigrations craseapp
python manage.py migrate
Crie um Superusuário (opcional, para acessar o Admin):
Bash
python manage.py createsuperuser
Inicie o Servidor:
Bash
python manage.py runserver
Acesse a Aplicação: Abra seu navegador e acesse http://127.0.0.1:8000/. O painel administrativo estará em http://127.0.0.1:8000/admin/.
