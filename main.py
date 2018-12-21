# ORGANIZATION
# ------------
# box on left with projects
# box on right with labels
# box in middle with assignments
# multiple labels can be selected, or none
# projects stored in a dictionary containing dictionaries of individual assignments and their data
# dict projects {"p1":{"tasks":["asdf":{"date_due":time}]}, p2:{"container":"p1", "tasks:["fdsa":{}]}}
# dict labels {"t1":{"tasks":["asdf"]},"t2":{"tasks":["asdf"]}}

from datetime import * 
from tkinter import *
from tkinter import ttk
import task
import project

root = Tk()
root.title("Todoist clone!")

root.mainloop()