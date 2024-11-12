import functions
import tkinter
import FreeSimpleGUI as sig


label = sig.Text("Type in a todo")
input_box = sig.InputText(tooltip="Enter To-Do", key="todo")
add_button = sig.Button("Add")



windows = sig.Window("My To-Do App",
                     layout=[[label], [input_box,add_button]],
                     font=('Arial',20))
while True:
    event, values = windows.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
        case sig.WIN_CLOSED:
            break


windows.close()