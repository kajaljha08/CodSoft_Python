

class To_Do_List():
    def __init__(self):
        self.tasks=[]
        
    def view_tasks(self):
        print("To-Do-List")
        for i, task in enumerate(self.tasks,1):
            print(f"{i}. {task}")
            
    def add_task(self):
        task = input("Enter the  task: ")
        if task != "":
            self.tasks.append(task)
            print(f"Task {task} is added successfully to the List.")
            
    def delete_task(self):
        task_number = int(input("Enter the task number to delete: "))
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} is deleterd successfully.")
        except IndexError:
            print("Invalid task number.")
            
    def update_task(self):
        task_number = int(input("Enter the task number to be updated: "))
        try:
            task = input("Enter the new task: ")
            if task != "":
                self.tasks[task_number - 1] = task
                print(f"Task {task_number} updated successfully.")
        except IndexError:
            print("Invalid task number.")
                
ToDoList = To_Do_List()
while True:
    print("\nTo-Do-List Menu: ")
    print("1. Display Tasks")
    print("2. Add task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Quite")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        ToDoList.view_tasks()
    elif choice == 2:
         ToDoList.add_task()
    elif choice == 3:
         ToDoList.delete_task()
    elif choice == 4:
         ToDoList.update_task()
    elif choice == 5:
         print("Bye!")
         break
    else:
        print("Invalid choice. Please Enter correct number: ")
        
        
