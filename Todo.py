# A simple to-do app written in python
# start with importing relevant libraries
from tkinter import *
from tkinter import messagebox

# functions
# newTask function
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")


# delTask function
def deleteTask():
    lb.delete(ANCHOR)


# create & configure window
ws = Tk()
ws.geometry('500x550+500+200')
ws.title('To-Do App')
ws.config(bg = '#ededed')
#ws.resizable(width = False, height = False)

# creating the frame for our app
frame = Frame(ws)
frame.pack(pady = 10)

# adding the listbox
lb = Listbox(
    frame,
    width = 25,
    height = 8,
    font = ('Times', 18),
    bd = 0,
    fg = '#464646',
    highlightthickness = 0,
    selectbackground = '#a6a6a6',
    activestyle = "none"
)
lb.pack(side = LEFT, fill = BOTH)

# adding dummy data into our task list
task_list = [
    'Eat apple',
    'drink water',
    'go to gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ] 

# for loop
for item in task_list:
    lb.insert(END, item)

# adding scrollbars
sb = Scrollbar(frame)
sb.pack(side = RIGHT, fill = BOTH)

lb.config(yscrollcommand = sb.set)
sb.config(command = lb.yview)

# adding the entry box
my_entry = Entry(
    ws,
    font = ('times', 18)
    )

my_entry.pack(pady = 20)

# adding another frame for the buttons
button_frame = Frame(ws)
button_frame.pack(pady = 20)

# adding the buttons
# add task button
addTask_btn = Button(
    button_frame,
    text = 'Add Task',
    font = ('times 14'),
    bg = '#c5f776',
    padx = 20,
    pady = 10,
    command = newTask
)
addTask_btn.pack(fill = BOTH, expand = True, side = LEFT)

# delete task button
delTask_btn = Button(
    button_frame,
    text = 'Delete Task',
    font = ('times', 14),
    bg = '#ff8b61',
    padx = 20,
    pady = 10,
    command = deleteTask
)
delTask_btn.pack(fill = BOTH, expand = True, side = LEFT)



ws.mainloop()
