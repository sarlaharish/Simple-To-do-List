tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nYour Tasks:")
        print("-" * 20)
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
        print("-" * 20)

    elif choice == "2":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Task added: {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                removed = tasks[num - 1]
                tasks.pop(num - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Enter 1 to 4.")