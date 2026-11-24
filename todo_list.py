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


def complete_task(task_list, task_number):
    """ update a task´s status to completed based on its 1-based index in the task_list """
    #convert 1-based index to 0-based index
    index = task_number - 1

    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
        print(f'Task "{task_list[index]["title"]}" marked as completed.')
    else:
        print("Invalid task number. Please choose a valid task number.")


def delete_task(task_list, task_number):
    """ Deletes a task from the list based on its 1-based index"""
    index = task_number -1
    if 0<= index < len(task_list):
        removed = task_list.pop(index)
        print(f"task {removed['title']}' deleted permanently.")
    else:
        print("Invalid task number.")


if __name__ == "__main__":
    tasks = []

    while True:
        print("\n--- CONSOLOE TODO LIST ---")
        print("1. Add a new task")
        print("2. view all tasks")
        print("3. mark a task as completed")
        print("4. Delete a task")
        print("5. exit")



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
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter the task number to complete:"))
                    complete_task(tasks,num)
                except ValueError:
                    print("erro: please enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter the task number to delete"))
                    delete_task(tasks,num)
                except ValueError:
                    print("please enter a valid number")

        elif choice == "5":
            print("\n Exitin to do list . goodbye.")
            break
        else:
            print("Invalid option. Please choose a valid option (1-3).")