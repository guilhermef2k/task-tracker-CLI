from datetime import datetime 
from task_cli.storage import load_tasks, save_task

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