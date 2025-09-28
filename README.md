# Sistema de Gerenciamento Ágil de Tarefas

## Objetivo
Desenvolver um sistema de gerenciamento de tarefas utilizando metodologias ágeis, permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

## Escopo
O sistema implementa funcionalidades básicas de CRUD para tarefas, controle de prioridade e integração com testes automatizados, simulando um projeto ágil real.

## Metodologia Adotada
- Kanban para gestão de tarefas (A Fazer, Em Progresso, Concluído)
- Integração contínua com GitHub Actions
- Testes automatizados utilizando PyTest
- Versionamento e histórico de commits claros e detalhados

## Estrutura do Projeto
projeto-agil-github/
│
├── src/
│ ├── app.py # Aplicação Flask
│ ├── models.py # Modelos SQLAlchemy
│ └── init.py
│
├── tests/
│ ├── test_api.py # Testes automatizados com PyTest
│ └── init.py
│
├── docs/
│ ├── casos_de_uso.drawio # Diagrama de casos de uso
│ └── classes.drawio # Diagrama de classes
│
├── .github/
│ └── workflows/
│ └── python-app.yml # Pipeline de CI/CD
│
├── README.md
└── requirements.txt

bash
Copiar código

## Instruções para Execução
1. Clonar o repositório:
```bash
git clone https://github.com/SEU_USUARIO/projeto-agil-github.git
cd projeto-agil-github
Criar e ativar ambiente virtual:

bash
Copiar código
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux / Mac
Instalar dependências:

bash
Copiar código
pip install -r requirements.txt
Rodar a aplicação:

bash
Copiar código
python -m src.app
Executar testes automatizados:

bash
Copiar código
pytest -v
Controle de Qualidade
Todos os testes passam com sucesso.

Pipeline GitHub Actions configurado para rodar testes automaticamente em cada push.

Quadro Kanban
O Kanban do projeto está disponível na aba Projects do GitHub, com as colunas:

A Fazer

Em Progresso

Concluído

Histórico de Commits
Commits detalhados, refletindo todas as etapas de desenvolvimento, desde a implementação inicial até ajustes finais e simulação de mudança no escopo.

Mudança no Escopo
Foi adicionada a prioridade nas tarefas, documentada no README e refletida no Kanban.
