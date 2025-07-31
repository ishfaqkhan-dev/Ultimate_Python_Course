
contacts = {}

def add_contact (name, number):
    contacts[name] = number
    print("Contact Added Successfully")

def search_contact (name):
    if name in contacts:
        print(f"Name : {name} and Number : {contacts[name]}")
    else :
        print("Contact Not Found")

while True:
    print("\n 1: Add New Contact Number \n 2: Search Contact Number \n 3: Exit" )
    choice = int(input("Enter the Choice number : "))

    if choice == 1:
        name = input("Enter the Name : ")
        number = input("Enter the Number : ")
        add_contact(name, number)
    elif choice == 2:
        contact_name = input("Enter the Contact Name: ")
        search_contact(contact_name)
    elif choice == 3:
        print("You Exit the Contacts Dictionary.")
        break
    else :
        print("Invalid Choice")