CraseApp: Validador de Crase

Este projeto é uma aplicação web desenvolvida com o framework Django que tem como objetivo validar a ocorrência da crase em combinações de termos regentes e regidos, aplicando a lógica gramatical de forma programática.

🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias principais:











Tecnologia
Função no Projeto
Python
Linguagem de programação principal.
Django
Framework web para o desenvolvimento da aplicação.
MySQL/MariaDB
Sistema de gerenciamento de banco de dados (SGBD) para persistência dos dados de mapeamento e regras.
HTML & CSS
Estrutura e estilização da interface do usuário.


🏗️ Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com algumas configurações específicas:

Plain Text


djangodjango/
├── craseapp/             # Aplicação principal (App)
│   ├── migrations/
│   ├── templates/
│   │   └── craseapp/     # Templates HTML específicos da aplicação
│   ├── __init__.py
│   ├── admin.py          # Configuração do painel administrativo
│   ├── apps.py
│   ├── forms.py          # Definição do formulário de consulta
│   ├── models.py         # Definição dos modelos (TermoRegente, TermoRegido, MapeamentoCrase, Regra)
│   ├── tests.py
│   ├── urls.py           # Rotas da aplicação
│   └── views.py          # Lógica de negócio (Validação e Consulta Dinâmica)
├── craseproject/         # Configurações do Projeto (Project)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Configurações principais (DB, Apps, Templates, Static)
│   ├── urls.py           # Rotas globais do projeto
│   └── wsgi.py
├── manage.py             # Utilitário de linha de comando do Django
└── static/               # Arquivos estáticos globais (ex: styles.css)
    └── styles.css


⚙️ Como Foi Feito (Instruções de Configuração)

O desenvolvimento seguiu os passos típicos de um projeto Django com banco de dados externo:

1. Configuração do Ambiente

•
Instalação do Django: O projeto foi iniciado com a instalação do framework Django.

•
Instalação do Driver MySQL: Foi necessário instalar o driver de conexão do Python com o MySQL (ex: mysqlclient).

2. Configuração do Banco de Dados

O arquivo craseproject/settings.py foi configurado para utilizar o MySQL (ou MariaDB) como SGBD, conforme as linhas 65-77:

Python


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

•
Modelos (craseapp/models.py): Foram criados modelos para:

•
TermoRegente: Define se o termo exige a preposição 'a'.

•
TermoRegido: Define se o termo aceita o artigo 'a'.

•
Regra: Para catalogar regras gramaticais específicas.

•
MapeamentoCrase: Relaciona um regente e um regido, e opcionalmente uma regra, para mapear a ocorrência da crase.



•
Lógica de Validação (craseapp/views.py): A lógica central da crase é implementada na função validar_crase e consulta_dinamica, que se baseia na regra fundamental:

4. Configurações Adicionais

•
Internacionalização: O settings.py foi ajustado para o padrão brasileiro: LANGUAGE_CODE = 'pt-br' e TIME_ZONE = 'America/Sao_Paulo'.

•
Templates e Estáticos: Os diretórios templates e static foram configurados no nível do projeto para facilitar a organização de arquivos base (base.html) e estilos globais (styles.css).

💻 Como Rodar o Projeto

1.
Clone o repositório:

2.
Crie e ative um ambiente virtual (recomendado ):

3.
Instale as dependências (assumindo que você tem um requirements.txt ou precisa instalar o Django e o driver MySQL):

4.
Configure o Banco de Dados:

•
Crie o banco de dados djangodjango no seu SGBD (MySQL/MariaDB).

•
Ajuste as credenciais em craseproject/settings.py se necessário.



5.
Aplique as Migrações:

6.
Crie um Superusuário (opcional, para acessar o Admin):

7.
Inicie o Servidor:

8.
Acesse a Aplicação: Abra seu navegador e acesse http://127.0.0.1:8000/. O painel administrativo estará em http://127.0.0.1:8000/admin/.

