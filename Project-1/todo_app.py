my_tasks = []

def view_tasks():
    print("Todo List:")
    for idx, task in enumerate(my_tasks, start=1):
        print(f"{idx}. {task}")
    if not my_tasks:
        print("No tasks to show")
        
    

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        my_tasks.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def update_task():
    view_tasks()
    if not my_tasks:
        return
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(my_tasks):
            new_task = input("Enter new task description: ").strip()
            if new_task:
                my_tasks[num-1] = new_task
                print("Task updated.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not my_tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(my_tasks):
            removed = my_tasks.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n1. View tasks\n2. Add task\n3. Update task\n4. Delete task\n5. Exit")
        try:
            choice = input("Choose option: ").strip()
        except EOFError:
            choice = "5"
            print("\nExiting.")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()