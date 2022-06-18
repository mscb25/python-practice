import csv
from collections import namedtuple
import tkinter
from tkinter.filedialog import askopenfilename

Task = namedtuple("Task", ["title", "duration", "prerequisites"])
#defines a namedtuple called Task that has value names of title, duration, and prerequisites

def read_tasks(filename):
    tasks = {}
    for row in csv.reader(open(filename)):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = set(map(int, row[3].split()))
        #the prereqs are split and recognized as seperate integers by the map funct; then the vals returned by map are converted to a set
        tasks[number] = Task(title, duration, prerequisites) #(title, duration, prereq)

    return tasks

def order_tasks(tasks):
    incomplete = set(tasks)
    completed = set()
    start_days = {}
    while incomplete: #aka looping over any tasks that are still incomplete
        for tasknum in incomplete:
            task = tasks[tasknum]
            if task.prerequisites.issubset(completed): #checks to see if the prereqs are completed // issubset checks if one set is contained in another set
                earliest_start_day = 0
                for prereqnum in task.prerequisites: #computes earliest day task can begin given prereqs
                    prereq_end_day = start_days[prereqnum] + tasks[prereqnum].duration
                    if prereq_end_day > earliest_start_day:
                        earliest_start_day = prereq_end_day
                start_days[tasknum] = earliest_start_day
                incomplete.remove(tasknum)
                completed.add(tasknum)
                break 
    return start_days

def draw_chart(tasks, canvas, row_height=40, title_width=300, line_height=40, day_width=20, bar_height=20, title_indent=20, font_size=-16):
    #params are defult vals that specify where to draw elements and how much space they take
    height = canvas["height"]
    width = canvas["width"]
    week_width = 5 * day_width
    canvas.create_line(0, row_height, width, line_height, fill="gray")
    for week_number in range(5): #loops for up to five weeks (0-4)
        x = title_width + week_number * week_width
        canvas.create_line(x, 0, x, height, fill="gray")
        canvas.create_text(x + week_width / 2, row_height / 2, text=f"Week {week_number + 1}", font=("Helvetica", font_size, "bold"))
        start_days = order_tasks(tasks) #getting the order the tasks need to be completed in
        y = row_height
        for tasknum in start_days: #loops over task nums in the order they occur in the dictionary 
            task = tasks[tasknum]
            canvas.create_text(title_indent, y + row_height / 2, text=task.title, anchor=tkinter.W, font=("Helvetica", font_size)) #drawing task title on left
            bar_x = title_width + start_days[tasknum]  * day_width
            bar_y = y + (row_height - bar_height) / 2
            bar_width = task.duration * day_width
            # above three lines calculate the coordinates for the box that represents the task
            canvas.create_rectangle(bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, fill="red")
            y+= row_height #ensures the next box is drawn on a new line

def open_project():
    filename = askopenfilename(title="Open Project", initialdir=".", filetypes=[("CSV Document", "*.csv")])
    #specifies dialog title, the directory to find it in, and the acceptable formats it will take
    tasks = read_tasks(filename) #reads tasks from the CSV
    draw_chart(tasks, canvas) #draws chart of the tasks
    filename_label.config(text=filename) #updates the text attribute of label to the filename

def clear_canvas(): #allows user to clear the canvas
    filename_label.config(text="")
    canvas.delete(tkinter.ALL)

root = tkinter.Tk() #creates top level widget
root.title("Project Planner")
root.resizable(width=False, height=False) #prevents the project window from being resized

button_frame = tkinter.Frame(root, padx=5, pady=5) #creates the frame at the top, which the 'open project' button sits in
button_frame.pack(side="top", fill="x")
open_button = tkinter.Button(button_frame, text="Open Project...", command=open_project) #creates the button
open_button.pack(side="left") #specifies button should be at this edge
clear_button = tkinter.Button(button_frame, text="Clear", command=clear_canvas)
clear_button.pack(side="left")

filename_label = tkinter.Label(button_frame)
filename_label.pack(side="right")

canvas = tkinter.Canvas(root, width=800, height=400, bg="white")
canvas.pack(side='bottom') #creates a canvas widget that's placed on bottom

tkinter.mainloop()
