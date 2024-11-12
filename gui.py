import functions
import tkinter
import FreeSimpleGUI as sig

label = sig.Text("Type in a todo")
input_box = sig.InputText(tooltip="Enter To-Do")
add_button = sig.Button("Add")



windows = sig.Window("My To-Do App", layout=[[label,input_box,add_button]])
windows.read()
windows.close()