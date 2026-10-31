def print_menu():
    print("\n=== Список дел ===")
    print("1. Добавить дело")
    print("2. Показать все дела")
    print("3. Отметить выполненным")
    print("4. Удалить дело")
    print("0. Выход")

def show_tasks(tasks):
    if not tasks:
        print("Список пуст.")
        return
    for i, task in enumerate(tasks):
        status = "[x]" if task.done else "[ ]"
        print(f"{i}. {status} {task.title} (до {task.deadline})")