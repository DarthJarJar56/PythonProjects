import os
from os import path

# helper function to print out the main menu of the interface
def main_menu():
    print("\n--------------------------------------\nWelcome to The ToDo List Interface\n--------------------------------------\nEnter one of the following choices:")
    print("1) Create todo list")
    print("2) Edit ToDo List")
    print("3) Display ToDo List")
    print("4) Exit")

# helper function to print out the editing sub menu
def edit_menu():
    print("\nWhat would you like to do?")
    print("1) Add a task")
    print("2) Delete a task")
    print("3) Clear ToDo List")
    print("4) Return to main menu")

# Menu system with multiple potential choices
def menu_loop():
    while True:
        try:
            main_menu()
            inp = int(input("Enter your choice: "))
            if inp == 1:
                init_list()
                break
            elif inp == 2:
                edit_loop()
                break
            elif inp == 3:
                display()
                break
            elif inp == 4:
                print("Thanks!")
                break
        except Exception as e:
            print(e)
    exit

# todo list editing sub menu
def edit_loop():
    while True:
        try:
            edit_menu()
            inp = int(input("Enter your choice: "))
            if inp == 1:
                edit_add()
                break
            elif inp == 2:
                del_task()
                break
            elif inp == 3:
                clear_list()
                break
            elif inp == 4:
                menu_loop()
                break
        except Exception as e:
            print(e)
    exit

# check to see if the user already has a todo list,
# if not, create one and allow the user to add their first
# task and return to the main menu. Otherwise, just return
# to the main menu to allow user to edit their list instead
def init_list():
    if path.exists('todo.txt') == False:
        file = open("todo.txt", "w")
        task = input("\nEnter task to add: ")
        file.write(task + "\n")
        file.close()
        menu_loop()
    
    print("\nYou already have a todo list! Try editing it instead!")
    menu_loop()

# Checks if a todo list exists for the script to display
# if so, read the contents of the file and print them
# to the screen, then call back to the menu loop
def display():
    if path.exists('todo.txt') == False:
        print("\nYou do not have a todo list!")
        menu_loop()
    f = open('todo.txt', 'r')
    list = f.read()
    print("\n")
    print(list)
    f.close()
    menu_loop()

# Editing submenu option to add a task to the list
def edit_add():
    file = open("todo.txt", "a")
    task = input("\nEnter a task to add: ")
    file.write(task + "\n")
    file.close()
    edit_loop()

# Editing submenu option to delete a task from the list
# We do this by first storing the contents of the file
# into "lines", then storing a secondary version of the file
# that removes all newline characters and allows us to search
# for the element we want to delete. If the element does exist
# within the file, rewrite the file with a conditional statement
# denying the target string from being placed. 
def del_task():
    task = input("\nWhat is the task you want to delete? ")
    file = open("todo.txt", "r")
    lines = file.readlines()
    y = [x.strip("\n") for x in lines]
    if task not in y:
        print("This task does not exist!")
        file.close()
        edit_loop()
    file.close()
    file = open("todo.txt", "w")
    for l in lines:
        if task not in l:
            file.write(l)
    file.close()
    edit_loop()

def clear_list():
    print("Are you sure you would like to clear your list? You will not be able to undo this action.")
    ans = input("Y/N: ")
    if ans == 'Y':
        open('todo.txt', 'w').close()
        print('To do list cleared!')
        edit_loop()
    elif ans == 'N':
        edit_loop()
    else:
        print('Invalid input, returning to edit menu')
        edit_loop()
# driver code
menu_loop()