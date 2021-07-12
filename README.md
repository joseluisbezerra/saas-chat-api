# SaaS Chat API
API REST de um chat para empresas feita com o Django REST Framework para aprender mais sobre isolamento de um SaaS

# Instalação
1. Crie um ambiente virtual:
```
python3 -m venv venv
```
2. Ative o ambiente virtual;
3. Instale as dependências:
```
(venv) pip install -r requirements.txt
```
4. Em seguida você vai precisar criar um arquivo .env:
```
(venv) python env_gen.py
```
5. Sincronize a base de dados:
```
(venv) python manage.py migrate
```
6. Crie um super usuário (Administrador do sistema):
```
(venv) python manage.py createsuperuser
```
7. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000):
```
(venv) python manage.py runserver
```