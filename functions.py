import os


#this function reads the file to get it in a list
def get_todos():
    """Read the file and get in a list all the todos in the file"""
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()

    return todos_local

#this function writes the todos in the file
def set_todos(lst):

    """Writes in the file all the todos in the parameter lst"""
    with open("todos.txt", "w") as file_local:
        file_local.writelines(lst)

def show():
    todos_local = get_todos()

    for i, todo_local in enumerate(todos_local):
        todo_local = todo_local.strip("\n")
        row = f"{i + 1}.- {todo_local.title()}"
        print(row)

# this function clears the terminal screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
