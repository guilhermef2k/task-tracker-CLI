# Task Tracker CLI

Uma ferramenta de linha de comando (CLI) simples para gerenciar tarefas, construída em Python com `argparse`. Permite adicionar, atualizar, remover, listar e marcar o status de tarefas diretamente pelo terminal.

Projeto criado como exercício prático, baseado no desafio [Task Tracker](https://roadmap.sh/projects/task-tracker) do roadmap.sh.

## Funcionalidades

- Adicionar novas tarefas
- Atualizar a descrição de uma tarefa existente
- Remover tarefas
- Listar todas as tarefas ou filtrar por status
- Marcar tarefas como "em progresso" ou "concluída"
- Persistência dos dados em um arquivo JSON local

## Requisitos

- Python 3.8 ou superior

## Instalação

Clone o repositório e instale o pacote em modo editável:

```bash
git clone https://github.com/guilhermef2k/task-tracker-CLI.git
cd task-tracker-CLI
pip install -e .
```

Isso disponibiliza o comando `task-cli` no seu terminal.

## Uso

### Adicionar uma tarefa

```bash
task-cli add "Estudar Python"
```

### Atualizar uma tarefa

```bash
task-cli update <id> "Nova descrição"
```

### Remover uma tarefa

```bash
task-cli delete <id>
```

### Marcar status de uma tarefa

```bash
task-cli mark-in-progress <id>
task-cli mark-done <id>
```

### Listar tarefas

Listar todas:

```bash
task-cli list
```

Listar por status (`todo`, `in-progress` ou `done`):

```bash
task-cli list done
task-cli list in-progress
task-cli list todo
```

## Estrutura do projeto

```
task-tracker/
├── pyproject.toml
└── task_cli/
    ├── __init__.py
    ├── cli.py         # Define os comandos e argumentos (argparse)
    ├── manager.py      # Lógica de negócio: criar, atualizar, listar e salvar tarefas
    └── storage.py     # Criar e carregar os dados do arquivo JSON
```

## Formato dos dados

As tarefas são armazenadas em um arquivo `tasks.json`, criado automaticamente na primeira execução, no seguinte formato:

```json
{
  "id": 1,
  "description": "Estudar Python",
  "status": "todo",
  "creatAt": "2026-09-02 10:00:00",
  "updateAt": "2026-09-02 10:00:00"
}
```

## Tecnologias utilizadas

- Python
- [`argparse`](https://docs.python.org/3/library/argparse.html) — parsing de argumentos de linha de comando
- `json` — persistência dos dados

## Possíveis melhorias futuras

- [ ] Suporte a exportação/importação de tarefas
- [ ] Filtro por data de criação/atualização

