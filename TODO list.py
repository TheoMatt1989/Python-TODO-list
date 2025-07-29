import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
        
        return []
    
def save_tasks(tasks):    
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not done"
        print(f"{idx}. {task['task']} [{status}]")

def add_task(tasks):
    new_task = input("Enter new task:")
    tasks.append({"task": new_task, "done": False})
    print("Task added!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) -1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")    

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index =int(input("Enter task number to delete: ")) -1
        if 0 <= index <len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")    
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add Task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__=="_main_":
    main()