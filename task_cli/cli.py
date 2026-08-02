import argparse
from task_cli.manager import add_task
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # subcomando: add
    parser_add = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    parser_add.add_argument("descricao", help="Descrição da tarefa")

    # subcomando: list
    parser_list = subparsers.add_parser("list", help="Lista as tarefas")

    # subcomando: delete
    parser_delete = subparsers.add_parser("delete", help="Remove uma tarefa")
    parser_delete.add_argument("id", type=int, help="ID da tarefa a remover")

    args = parser.parse_args()

    if args.comando == "add":
        print(f"Adicionando tarefa: {args.descricao}")
        add_task(args.descricao)
    elif args.comando == "list":
        print("Listando tarefas...")
    elif args.comando == "delete":
        print(f"Removendo tarefa {args.id}")

if __name__ == "__main__":
    main()