# TO DO LIST - TASK 1

# Simple To-Do List Program using Python
# By: [Your Name] | For CodSoft Internship Task

def load_list():
    try:
        file = open("todo.txt", "r")
        lines = file.readlines()
        file.close()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def save_list(todo_list):
    file = open("todo.txt", "w")
    for task in todo_list:
        file.write(task + "\n")
    file.close()

def show_list(todo_list):
    if len(todo_list) == 0:
        print("Your task list is empty.\n")
    else:
        print("\nTasks to do:")
        for number in range(len(todo_list)):
            print(f"{number + 1}. {todo_list[number]}")
        print()

def add_new_task(todo_list):
    task = input("Enter a new task to add: ")
    todo_list.append(task)
    print("Task added.\n")

def edit_task(todo_list):
    show_list(todo_list)
    number = input("Enter the task number to update: ")
    if number.isdigit():
        num = int(number)
        if 1 <= num <= len(todo_list):
            updated = input("Write the updated task: ")
            todo_list[num - 1] = updated
            print("Task updated.\n")
        else:
            print("Number out of range.\n")
    else:
        print("Enter a valid number.\n")

def delete_task(todo_list):
    show_list(todo_list)
    number = input("Enter the number of the task to delete: ")
    if number.isdigit():
        num = int(number)
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Removed: {removed}\n")
        else:
            print("Number not in list.\n")
    else:
        print("Invalid input.\n")

def main():
    print("Welcome to the To-Do List Program\n")
    tasks = load_list()

    while True:
        print("Choose what you want to do:")
        print("1 - Add a Task")
        print("2 - Show All Tasks")
        print("3 - Edit a Task")
        print("4 - Delete a Task")
        print("5 - Exit the Program")
        
        choice = input("Type your choice (1 to 5): ")

        if choice == "1":
            add_new_task(tasks)
        elif choice == "2":
            show_list(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_list(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Please enter a correct option.\n")

if __name__ == "__main__":
    main()
