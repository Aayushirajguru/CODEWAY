import os

def display_menu():
    print("\n==== TO-DO LIST ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Save To-Do List")
    print("6. Exit")

def view_todo_list():
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\n=== TO-DO LIST ===")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")

def add_tasks():
        num_tasks = int(input("\nEnter the number of tasks you want to add: "))
        with open("todo.txt", "a") as file:
            for _ in range(num_tasks):
                task = input("Enter the task: ")
                file.write(f"{task}\n")
        print(f"{num_tasks} task(s) added successfully.")

def update_task():
    view_todo_list()
    task_number = int(input("\nEnter the task number to update: "))
    with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                updated_task = input("Enter the updated task: ")
                tasks[task_number - 1] = updated_task + "\n"
                with open("todo.txt", "w") as file:
                    file.writelines(tasks)
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

def delete_task():
    view_todo_list()
    task_number = int(input("\nEnter the task number to delete: "))
    with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                with open("todo.txt", "w") as file:
                    file.writelines(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
                
def save_todo_list():
    view_todo_list()
    save_confirmation = input("\nDo you want to save your to-do list? (yes/no): ").lower()
    if save_confirmation == "yes":
        print("To-do list saved successfully.")
    elif save_confirmation == "no":
        print("To-do list not saved.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_todo_list()
        elif choice == "6":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    if not os.path.isfile("todo.txt"):
        open("todo.txt", "w").close()
    main()