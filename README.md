# UniAgenda

Sistema web simples para gerenciamento de atividades pessoais, desenvolvido como parte da Atividade 2 (CRUD com persistência em arquivo JSON).

## Funcionalidades

-  Cadastro de atividades (Título, Descrição, Data, Hora)
-  Listagem em cards com estilo Bulma
-  Edição e exclusão de atividades
-  Dados salvos em arquivo JSON (`atividades.json`)

## Tecnologias

- Django (backend)
- HTML + JavaScript puro (frontend)
- Bulma (framework CSS)
- JSON como base de dados local

## Estrutura do Projeto

/backend/
```
├── atividades/
│ ├── views.py
│ ├── urls.py
│ ├── utils.py
│ ├── templates/atividades/index.html
│ └── static/js/script.js
├── data/
│ └── atividades.json
```

## Como Executar

1. Clone o repositório
2. Instale os pacotes com `pip install -r requirements.txt` (se aplicável)
3. Inicie o servidor: `python manage.py runserver`
4. Acesse no navegador: `http://localhost:8000/`

## Vídeo Explicativo

[Insira aqui o link do vídeo no YouTube]
