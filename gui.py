import functions
import tkinter
import FreeSimpleGUI as sig

#Add layout
label = sig.Text("Type in a todo")
input_box = sig.InputText(tooltip="Enter To-Do", key="todo")
add_button = sig.Button("Add")

#edit layout
list_box = sig.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 10])
edit_button = sig.Button("Edit")



windows = sig.Window("My To-Do App",
                     layout=[[label], [input_box,add_button],[list_box,edit_button]],
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
            windows['todos'].update(values=todos)


        case "Edit":
            todos = functions.get_todos()
            edit_todo = values['todos'][0]
            new_todo = values['todo'] + "\n"
            index = todos.index(edit_todo)
            todos[index]= new_todo
            functions.set_todos(todos)
            windows['todos'].update(values=todos)
        case"todos":
            windows['todo'].update(value=values['todos'][0])
        case sig.WIN_CLOSED:
            break


windows.close()