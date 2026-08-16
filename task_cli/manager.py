from datetime import datetime 
from task_cli.storage import load_tasks, save_task
from pprint import pprint

def add_task(description:str)->None:
    """Cria uma nova task e salva no arquivo JSON"""
    tasks = load_tasks()

    new_id = max([task["id"] for task in tasks], default = 0)+1
    now = datetime.now().isoformat()

    nova_task = {
        "id": new_id,
        "description": description,
        "status": "todo", 
        "creatAt": now,
        "updateAt": now 
    }
    
    tasks.append(nova_task)
    save_task(tasks)
    print(f"Tarefa adicionada com sucesso! (ID={new_id})")

def list_tasks(status:str)->None:
    """Lista todas as tarefas salvas"""
    tasks = load_tasks()       

    if status != "all":
         tasks = [task for task in tasks if task["status"]==status]

    if not tasks:
        print("\nNenhuma tarefa encontrada com esse status!\n")
        return
    
    print("-"*22+"TAREFAS"+"-"*22)

    for task in tasks:
        print_task(task)

def print_task(task:dict)->None:
        """Exibe uma tarefa em formato de card"""
        print("┌" + "─" * 52 + "┐")
        print(f"│ TAREFA #{task['id']:<42} │")
        print("├" + "─" * 52 + "┤")
        print(f"│ Descrição:     {task['description']:<35} │")
        print(f"│ Status:        {task['status']:<35} │")
        print(f"│ Criado em:     {task['creatAt']:<35} │")
        print(f"│ Atualizado em: {task['updateAt']:<35} │")
        print("└" + "─" * 52 + "┘")
        print()

def update_task(id:int, new_description:str)->None:
    tasks = load_tasks()
    task_update = next((task for task in tasks if task["id"]==id), None)
    now = datetime.now().isoformat()
    if task_update: 
        task_update.update(description = new_description)
        task_update["updateAt"]=now
        print("Tarefa atualizada com sucesso")
        save_task(tasks)
    else:
        print("Nenhuma task com esse ID encontrado...")

def update_status(new_status:str, id:int)->None:
    """Altera o status da tarefa desejada"""

    tasks = load_tasks()
    task_update = next((task for task in tasks if task["id"]==id), None)
    now = datetime.now().isoformat()
    if task_update:
         task_update["status"]=new_status
         task_update["updateAt"]=now
         save_task(tasks)
         print("Tarefa atualizada com sucesso!")
    else:
         print("Nenhuma task com esse ID encontrado...")

def delete(id:int)->None:
    tasks = load_tasks()
    task_delete = next((task for task in tasks if task["id"]==id), None)
    if task_delete:
        tasks.remove(task_delete)
        save_task(tasks)
        print("\nTarefa removida com sucesso!\n")
    else:
        print("Nenhuma task com esse ID encontrado...")