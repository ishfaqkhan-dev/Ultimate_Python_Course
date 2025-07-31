
tasks = []

def Add_Task (item):
    tasks.append(item)
    print("Task_Added")

def Show_List ():
    print("Your To-Do List :")
    for index, item in enumerate(tasks, 1):
        print(f"{index} : {item}")

def Remove_task (index):
    if 0 < index <= len(tasks) :
        delete = tasks.pop(index - 1)
        print(f"Removed : {delete}")
    else:
        print("Invalid Item Number")


while True:
    print("\n 1: Add task \n 2: Show Task \n 3: Delete Task \n 4: Exit" )
    choice = int(input("Enter the Choice No : "))

    if choice == 1:
        item = input("Enter the new Item : ")
        Add_Task(item)
    elif choice == 2:
        Show_List()
    elif choice == 3:
        item_no = int(input("Enter the Item No :"))
        Remove_task(item_no)
    elif choice == 4:
        print("You Exit the List.")
        break
    else:
        print("You Choice the Invalid Operation.")