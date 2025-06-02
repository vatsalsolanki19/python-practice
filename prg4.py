def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed = tasks.pop(task_num)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

todo_list()
