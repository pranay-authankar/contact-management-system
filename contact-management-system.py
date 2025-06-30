def home_page():
    print("\n------------------------------------------\nEnter digit in front of the task\n")
    print("\n0. Exit the program\n1. Add contact\n2. View all contacts\n3. Search a contact by name\n4. Delete a contact")
def add_contact(name, number):
    contact.update({name:number})
    print("\n----Contact Updated-----")
def view_all_contact():
    print("\n---Contact List---\n")
    if len(contact) > 0:
        i = 1
        for x in contact:
            print(f"{i})\t{x.capitalize()} : {contact[x]}")
            i += 1
        print(f"\nTotal contacts : {len(contact)}\n")
    else:
        print("\nYou don't have any saved contacts till now\n")
def search_contact_by_name(name):
    if name in contact:
        print(name, "-", contact[name])
    else:
        print("Contact not found")
        print("\nWant to save this name with an number?\n")
        yn = False
        while yn == False:
            inp = input("[y/n] : ").strip().lower()
            if inp:
                if inp == "y":
                    num_check = False
                    while num_check == False:
                        number = input(f"\nEnter {name}'s number : ")
                        if number:
                            if number.isdigit():
                                number = int(number)
                                contact.update({name:number})
                                num_check = True
                                yn = True
                                print("\n----Contact Updated----")
                            else:
                                print("\nEnter a numeric value\n")
                                continue
                        else:
                            print("\nYou didn't Enter anything\nEnter Something\n")
                            continue
                elif inp == "n":
                    yn = True
                else:
                    print("\nEnter either 'y' or 'n'")
                    continue
            else:
                print("\nYou didn't enter anything\nTry entering 'y' or 'n'")
                continue
def del_a_contact(name):
    if name in contact:
        del contact[name]
        print(f"\nContact '{name}' deleted")
    else:
        print("Contact Not Found")
def contact_book():
    global contact
    contact = {}
    print("\nWelcome to your Contact Book\n")
    stop = False
    while stop == False:
        home_page()
        inp = input("\nTask to perform -> ")
        if inp:
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    print("\nSee you next Time")
                    stop = True
                elif inp == 1:
                    name_check = False
                    while name_check == False:
                        name = input("Enter name : ")
                        if name in contact:
                            stop1 = False
                            while stop1 == False:
                                exist = input("\nWant to update this contact?\n[y/n] -> ").lower().strip()
                                if exist:
                                    if exist == "y":
                                        stop2 = False
                                        while stop2 == False:
                                            number = input("Enter number : ")
                                            if number and number.isdigit():
                                                contact[name] = int(number)
                                                print(f"\n{name}'s contact Updated\n")
                                                stop1 = True
                                                name_check = True
                                            else:
                                                print("\nTry Again with digit")
                                                continue
                                    elif exist == "n":
                                        print("\nOkay\n------------")
                                        stop1 = True
                                        name_check = True
                                    else:
                                        print("\nType either y/n")
                                else:
                                    print("\nNot answerd\n")
                        elif name not in contact:
                            number = input("Enter number : ")
                            if name and number.isdigit():
                                add_contact(name, number)
                                name_check = True
                        else:
                            print("\nTry Again")
                            continue

                elif inp == 2:
                    view_all_contact()

                elif inp == 3:
                    name_check = False
                    while name_check == False:
                        name = input("Enter name : ")
                        if name:
                            search_contact_by_name(name)
                            name_check = True
                        else:
                            print("\nEnter Something")
                            continue

                elif inp == 4:
                    name_check = False
                    while name_check == False:
                        name = input("Enter name : ")
                        if name:
                            del_a_contact(name)
                            name_check = True
                        else:
                            print("\nEnter Something")
                            continue
                    
                else:
                    print("\nEnter a valid input")
                    continue
            else:
                print("\nEnter digit in front of the tasks")
                continue
        else:
            print("\nYou didn't enter anything")
            continue

contact_book()
