# Create a simple command-line to-do list application that allows users to add, view, and delete tasks. 
def todo_list():
    tasks = []
    
    while True:
        print("\n==== To-Do List ====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task description: ")
            tasks.append({"description": task, "done": False})
            print("Task added!")
        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks):
                    status = "✓" if task["done"] else "✗"
                    print(f"{i+1}. [{status}] {task['description']}")
        elif choice == "3":
            if not tasks:
                print("No tasks to mark as done!")
            else:
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num-1]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

todo_list()
