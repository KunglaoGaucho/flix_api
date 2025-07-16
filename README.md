# Flix API

Uma API RESTful desenvolvida com Django para gerenciar filmes, atores, gêneros e reviews.  
Foi feita como exercício prático para aprender a construir um CRUD completo com autenticação via JWT.

---

## 📌 Descrição do Projeto

- **Propósito:** Permitir o cadastro, listagem, edição e remoção de filmes, atores, gêneros e avaliações.
- **Problema que resolve:** Nenhum específico — é um projeto educacional para treinar Django e APIs REST.

---

## 🚀 Principais Recursos e Endpoints

A API oferece um CRUD completo para os seguintes recursos:

- Filmes (`/movies/`)
- Atores (`/actors/`)
- Gêneros (`/genres/`)
- Reviews (`/reviews/`)

### Métodos disponíveis em todos os endpoints:

- `GET`: Lista todos os registros ou detalha um item específico (`/movies/1/`)
- `POST`: Cria um novo item
- `PUT`: Atualiza um item existente
- `DELETE`: Remove um item
- `OPTIONS`: Detalhes do endpoint

---

## Tecnologias e Dependências

- **Linguagem:** Python
- **Framework:** Django + Django REST Framework
- **Banco de dados:** SQLite
- **Autenticação:** JWT com `djangorestframework-simplejwt`

---

## Instruções de Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/KunglaoGaucho/flix_api.git
cd flix_api
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrations

```bash
python manage.py migrate
```

### 5. Crie um SuperUser (Obrigatório por conta da autenticação JWT)

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor localmente
```bash
python manage.py runserver
```

# Autenticação JWT

Para acessar qualquer endpoint, você precisa estar autenticado.

### 1. Faça um POST para /api/token/ com o seguinte JSON no corpo da requisição:
``` json
 {"username": "seu_usuario",
  "password": "sua_senha"}
```
### 2. O retorno será:
```json
{ "access": "seu_token_aqui"
  "refresh": "seu_refresh_token_aqui"}
```

### 3. Use o token no header das requisições seguintes
``` makefile
Authorization: Bearer seu_token_aqui

```

## 🤝 Contribuição

Contribuições são bem-vindas! Se quiser sugerir melhorias, corrigir bugs ou adicionar novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.

