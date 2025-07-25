def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(tasks):
                tasks.pop(index - 1)
                save_tasks(tasks)
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
