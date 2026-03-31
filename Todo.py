# Initialize an empty to-do list
todo_list = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not todo_list:
            print("No tasks yet.")
        else:
            for i, task in enumerate(todo_list, 1):
                print("{}. {}".format(i, task))

    elif choice == "2":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == "3":
        if not todo_list:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(todo_list):
                removed = todo_list.pop(task_no - 1)
                print("'{}' removed.".format(removed))
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
