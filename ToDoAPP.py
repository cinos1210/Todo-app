import time

from functions import *


while True:
    now = time.strftime("it's %b - %d, %H:%M:%S")
    print(now)
    user_action = input("type 'add', 'show' or edit: ")
    user_action.strip()
    #show()
    # Obtiene la respuesta del usuario y borra espacios añadidos

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"  # take the todo after the first 4 characters of the string.

        todos = get_todos()

        todos.append(todo)

        set_todos(todos)

        #clear_screen()

    elif user_action.startswith("show"):
        #clear_screen()
        show()


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])  # take the number of todo after the 5 characters and then convert it to integer
            number = number - 1

            todos = get_todos()

            # "number = int(input("Number of the todo to edit: "))
            # number = number -1

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            set_todos(todos)

            #clear_screen()
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])  # take the number of todo after the 5 characters and then convert it to integer

            todos = get_todos()
            index = number - 1
            todo_completed = todos[index]
            todos.pop(index)

            set_todos(todos)

            message = f"The Todo:\n {todo_completed} has been completed"

            print(message)
        except IndexError:
            print("The number of to do that you introduce is not valid")
            continue
        #clear_screen()


    elif 'exit' in user_action:
        break

print("bye bye...")

result = {}

