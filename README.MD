\# TraceMind — Plataforma Colaborativa de Requisitos



> Projeto Aplicado I — SENAI 2026  

> Tecnologia em Análise e Desenvolvimento de Sistemas



\---



\## Sobre o Projeto



O \*\*TraceMind\*\* é uma plataforma web colaborativa desenvolvida para apoiar o processo de levantamento, organização e gestão de requisitos em projetos de software. A solução centraliza a comunicação entre stakeholders, padroniza a documentação e promove rastreabilidade das informações ao longo do ciclo de desenvolvimento.



\---



\## Equipe



| Nome | Função |

|---|---|

| Julio Cezar de Souza Azevedo | Back-end (Django + PostgreSQL) |

| Nicolas Kaenan Silveira | Front-end (Django REST) |

| Thiago Brito Novaes | DevOps (GitHub + CI/CD) |

| Vitor Henrik Lopes | Segurança (OAuth 2.0) |

| Yuri de Almeida Lima | Full-stack (Python avançado) |



\---



\## Stack Tecnológica



| Tecnologia | Uso |

|---|---|

| Python 3.11 | Linguagem principal |

| Django 5.0.6 | Framework web |

| PostgreSQL 18 | Banco de dados |

| Bootstrap 5 | Interface |

| django-simple-history | Versionamento de requisitos |

| ReportLab | Exportação PDF |

| python-docx | Exportação DOCX |



\---



\## Funcionalidades



\### MVP Implementado

\- Login com autenticação Django nativa

\- Dashboard com métricas e status dos requisitos

\- CRUD completo de Stakeholders

\- CRUD completo de Requisitos com filtros por tipo e status

\- Versionamento de requisitos com histórico de alterações

\- Chat colaborativo por requisito com sistema de likes

\- Matriz de Rastreabilidade (Requisitos x Stakeholders)

\- Exportação em JSON, PDF, DOCX e Markdown

\- Django Admin configurado e personalizado



\### Features Futuras

\- OAuth2 com Google

\- Upload de imagens e documentos

\- Edição simultânea com WebSockets (Django Channels)

\- Integração com GitHub, Jira e Trello

\- Módulo de IA para sugestão de requisitos



\---



\## Instalação e Configuração



\### Pré-requisitos

\- Python 3.11+

\- PostgreSQL 14+

\- Git



\### 1. Clonar o repositório



```bash

git clone https://github.com/seu-usuario/tracemind.git

cd tracemind

```



\### 2. Criar e ativar o ambiente virtual



```bash

python -m venv venv



\# Windows

venv\\Scripts\\activate



\# Linux/Mac

source venv/bin/activate

```



\### 3. Instalar dependências



```bash

pip install -r requirements.txt

```



\### 4. Configurar o banco de dados



No pgAdmin ou psql, execute:



```sql

CREATE DATABASE reqplatform\_db

&#x20; ENCODING 'UTF8'

&#x20; LC\_COLLATE 'Portuguese\_Brazil.1252'

&#x20; LC\_CTYPE 'Portuguese\_Brazil.1252'

&#x20; TEMPLATE template0;

```



\### 5. Criar o arquivo `.env`



Crie um arquivo `.env` na raiz do projeto:



```env

SECRET\_KEY=django-insecure-mude-esta-chave-em-producao

DEBUG=True

DB\_NAME=reqplatform\_db

DB\_USER=postgres

DB\_PASSWORD=postgres

DB\_HOST=localhost

DB\_PORT=5432

```



\### 6. Aplicar migrações



```bash

python manage.py makemigrations stakeholders

python manage.py makemigrations requisitos

python manage.py migrate

```



\### 7. Popular dados de demonstração



```bash

chcp 65001

python manage.py shell < seed\_demo.py

```



\### 8. Iniciar o servidor



```bash

python manage.py runserver

```



Acesse: \[http://localhost:8000](http://localhost:8000)



\---



\## Credenciais de Acesso



| Campo | Valor |

|---|---|

| Usuário | `admin` |

| Senha | `admin123` |

| Admin Django | \[http://localhost:8000/admin/](http://localhost:8000/admin/) |



\---



\## Estrutura do Projeto



```

tracemind/

├── manage.py

├── requirements.txt

├── seed\_demo.py

├── .env

├── reqplatform/

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── core/               # Dashboard e configurações base

├── stakeholders/       # CRUD de Stakeholders e Projetos

├── requisitos/         # CRUD, Chat, Exportação, Matriz

└── templates/

&#x20;   ├── base.html

&#x20;   ├── core/

&#x20;   ├── stakeholders/

&#x20;   └── requisitos/

```



\---



\## Diagrama de Casos de Uso



Os principais atores do sistema são:



\- \*\*Analista de Requisitos\*\* — gerencia stakeholders, cria e edita requisitos, gera documentação

\- \*\*Cliente Solicitante\*\* — participa do chat, valida requisitos

\- \*\*Dev/QA\*\* — consulta requisitos e rastreabilidade

\- \*\*PMO\*\* — visualiza dashboards e exporta relatórios



\---



\## Exportações Disponíveis



| Formato | Rota |

|---|---|

| JSON | `/requisitos/exportar/json/` |

| PDF | `/requisitos/exportar/pdf/` |

| DOCX | `/requisitos/exportar/docx/` |

| Markdown | `/requisitos/exportar/markdown/` |



\---



\## Referências



\- SOMMERVILLE, Ian. \*Engenharia de Software\*. 10. ed. Pearson, 2018.

\- PRESSMAN, Roger S.; MAXIM, Bruce R. \*Engenharia de Software: Uma Abordagem Profissional\*. 8. ed. AMGH, 2016.

\- WIEGERS, Karl E.; BEATTY, Joy. \*Software Requirements\*. 3. ed. Microsoft Press, 2013.

\- \[Django Documentation](https://docs.djangoproject.com/)

\- \[PostgreSQL Documentation](https://www.postgresql.org/docs/)



\---



\*Florianópolis, 2026\*

