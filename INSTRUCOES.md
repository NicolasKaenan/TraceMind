# ReqPlatform — Instruções de Setup Completo

## Pré-requisitos

- Python 3.11+
- PostgreSQL 14+
- pip

---

## 1. Criar e ativar ambiente virtual

```bash
python -m venv venv

# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

---

## 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 3. Configurar o PostgreSQL

Abra o psql ou pgAdmin e execute:

```sql
CREATE DATABASE reqplatform_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE reqplatform_db TO postgres;
```

> Se já tiver um usuário diferente, ajuste o arquivo `.env` abaixo.

---

## 4. Criar arquivo `.env` na raiz do projeto

Crie o arquivo `reqplatform/.env` com o seguinte conteúdo:

```env
SECRET_KEY=django-insecure-mude-esta-chave-em-producao-abc123xyz
DEBUG=True
DB_NAME=reqplatform_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

> O arquivo `.env` deve ficar na mesma pasta do `manage.py`.

---

## 5. Aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Popular dados de demonstração (para o vídeo)

```bash
python manage.py shell < seed_demo.py
```

Isso cria automaticamente:
- Superusuário: **admin / admin123**
- 5 stakeholders
- 10 requisitos (RF01–RF07, RNF01–RNF03)

---

## 7. Rodar o servidor

```bash
python manage.py runserver
```

Acesse:
- **App:** http://localhost:8000
- **Login:** admin / admin123
- **Admin Django:** http://localhost:8000/admin/
- **Exportar JSON:** http://localhost:8000/requisitos/exportar/

---

## Estrutura de pastas

```
reqplatform/
├── manage.py
├── requirements.txt
├── seed_demo.py
├── INSTRUCOES.md
├── reqplatform/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py        ← dashboard
│   ├── urls.py
│   └── admin.py
├── stakeholders/
│   ├── models.py       ← Stakeholder
│   ├── views.py        ← CRUD completo
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── requisitos/
│   ├── models.py       ← Requisito
│   ├── views.py        ← CRUD + exportar JSON
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html       ← sidebar + topbar (Bootstrap 5)
│   ├── core/
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── stakeholders/
│   │   ├── lista.html
│   │   ├── form.html
│   │   └── confirmar_exclusao.html
│   └── requisitos/
│       ├── lista.html
│       ├── form.html
│       └── confirmar_exclusao.html
└── static/
```

---

## Roteiro sugerido para o vídeo (3 minutos)

| Tempo | Ação |
|-------|------|
| 0:00–0:20 | Mostrar tela de login → entrar como admin |
| 0:20–0:50 | Dashboard — cards de totais, tabelas de últimos itens |
| 0:50–1:30 | Stakeholders — lista → criar novo → editar → excluir |
| 1:30–2:10 | Requisitos — lista com filtros → criar RF08 → status/prioridade |
| 2:10–2:30 | Exportar JSON — mostrar arquivo baixado |
| 2:30–3:00 | Django Admin — painel, filtros, fieldsets configurados |
