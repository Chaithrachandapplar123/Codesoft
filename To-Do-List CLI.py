
import json
tasks = []
def add_task(description):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    print(f'Task added: {description}')



def view_tasks():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        status = "Done" if task['completed'] else "Not Done"
        print(f"{task['id']}. {task['description']} - {status}")



def update_task(task_id, new_description=None, completed=None):
    for task in tasks:
        if task['id'] == task_id:
            if new_description:
                task['description'] = new_description
            if completed is not None:
                task['completed'] = completed
            print(f'Task {task_id} updated.')
            break
    else:
        print("Task not found.")


def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f'Task {task_id} deleted.')



def save_tasks(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)
    print("Tasks saved.")



def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No previous tasks found.")


def menu():
    load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description (or press Enter to skip): ")
            completed_input = input("Mark as completed? (y/n): ").lower()
            completed = True if completed_input == 'y' else False if completed_input == 'n' else None
            update_task(task_id, new_description if new_description else None, completed)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            save_tasks()
            break
        else:
            print("Invalid choice, please try again.")
            if __name__ == "__main__":
                menu()