import argparse
from task_cli.manager import add_task, list_tasks, update_task, update_status, delete
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # subcomando: add
    parser_add = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    parser_add.add_argument("descricao", help="Descrição da tarefa")

    # subcomando: list
    parser_list = subparsers.add_parser("list", help="Lista as tarefas")
    parser_list.add_argument("status", type=str, nargs="?", default=None, choices=["todo", "in-progress", "done"], help="Status das tarefas a listar")

    # subcomando: update
    parser_update = subparsers.add_parser("update", help="Atualiza a descrição das tarefas")
    parser_update.add_argument("id", type=int, help="ID da tarefa a atualizar")
    parser_update.add_argument("nova_descricao", type=str, help="Nova descrição da tarefa")

    # subcomando: mark-in-progress
    parser_update = subparsers.add_parser("mark-in-progress", help="Atualiza o status das tarefas")
    parser_update.add_argument("id", type=int, help="ID da tarefa para ser marcada como 'in-progress'")

    # subcomando: mark-done
    parser_update = subparsers.add_parser("mark-done", help="Atualiza o status das tarefas")
    parser_update.add_argument("id", type=int, help="ID da tarefa para ser marcada como 'done'")

    # subcomando: delete
    parser_delete = subparsers.add_parser("delete", help="Remove uma tarefa")
    parser_delete.add_argument("id", type=int, help="ID da tarefa a remover")

    args = parser.parse_args()

    if args.comando == "add":
        print(f"Adicionando tarefa: {args.descricao}")
        add_task(args.descricao)
    elif args.comando == "list":
        print("Listando tarefas...")
        if not args.status:
            list_tasks("all")
        else:
            list_tasks(args.status)
    elif args.comando == "update":
        update_task(args.id, args.nova_descricao)
    elif args.comando == "mark-in-progress":
        update_status("in-progress", args.id)
    elif args.comando == "mark-done":
        update_status("done", args.id)
    elif args.comando == "delete":
        print(f"Removendo tarefa {args.id}")
        delete(args.id)

if __name__ == "__main__":
    main()