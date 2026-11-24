def add_task(task_list, title):
    """ create a new task dictionary and append it to the task_list """
    new_task = {
        "title": title,
        "completed": False
    }
    task_list.append(new_task)
    print(f'Task "{title}" added to the list.')


def show_tasks(task_list):
    """ reads and displays all tasks in the task_list """
    print("\n--- YOUR TODO LIST---")
    if not task_list:
        print("your list is currently empty.")
        return

    for index, task in enumerate(task_list, start=1):
        status = "✓ Done" if task["completed"] else " pending"
        print(f"{index}. {task['title']} [{status}]")






if __name__ == "__main__":
    tasks = []

    while True:
        print("\n--- CONSOLOE TODO LIST ---")
        print("1. Add a new task")
        print("2. view all tasks")
        print("3. exit")


        choice = input("choose an option (1-3): ").strip()


        if choice == "1":
            task_title = input("Enter task  description: "). strip()
            if task_title:
                add_task(tasks, task_title)
            else:
                print("Task description cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            print("Exiting the todo list , goodbye.")
            break
        else:
            print("Invalid option. Please choose a valid option (1-3).")