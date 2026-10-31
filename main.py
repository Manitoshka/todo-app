import ui
import logic
import storage

def main():
    manager = logic.TaskManager()
    manager.tasks = storage.load_tasks()

    while True:
        ui.print_menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            title = input("Название дела: ")
            deadline = input("Срок выполнения: ")
            manager.add_task(title, deadline)
            storage.save_tasks(manager.tasks)
        elif choice == "2":
            ui.show_tasks(manager.tasks)
        elif choice == "3":
            ui.show_tasks(manager.tasks)
            try:
                idx = int(input("Номер дела для отметки: "))
                manager.mark_done(idx)
                storage.save_tasks(manager.tasks)
            except ValueError:
                print("Введите число!")
        elif choice == "4":
            ui.show_tasks(manager.tasks)
            try:
                idx = int(input("Номер дела для удаления: "))
                manager.delete_task(idx)
                storage.save_tasks(manager.tasks)
            except ValueError:
                print("Введите число!")
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()