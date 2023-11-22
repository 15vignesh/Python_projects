import tkinter as tk
from tkinter import messagebox
class TASK:
    def __init__(self):
        self.tasks=[]
        self.window=tk.Tk()
        self.window.title("Tasks List To Do")
        
        self.frame_tasks=tk.Frame(self.window)
        self.frame_tasks.pack(pady=10)
        
        self.list_tasks=tk.Listbox(self.frame_tasks,width=150)
        self.list_tasks.pack(side=tk.LEFT,fill=tk.BOTH)
        
        self.scroll_tasks=tk.Scrollbar(self.frame_tasks)
        self.scroll_tasks.pack(side=tk.RIGHT,fill=tk.BOTH)
        
        self.list_tasks.config(yscrollcommand=self.scroll_tasks.set)
        self.scroll_tasks.config(command=self.list_tasks.yview)
        
        self.frame_input=tk.Frame(self.window)
        self.frame_input.pack(pady=10)
        
        self.entry_task=tk.Entry(self.frame_input,width=100)
        self.entry_task.pack(side=tk.LEFT)
        
        self.button_add=tk.Button(self.frame_input,text="Add Task",command=self.add_task)
        self.button_add.pack(side=tk.LEFT,padx=10)
        
        self.button_remove=tk.Button(self.window,text="Remove Task",command=self.remove_task)
        self.button_remove.pack(pady=10)
        
    def add_task(self):
        task=self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.list_tasks.insert(tk.END,task)
            self.entry_task.delete(0,tk.END)
            messagebox.showinfo("Success","Task Added Successfully.")
        else:
            messagebox.showwarning("Warning","Please Enter a Task.")
    
    def remove_task(self):
        try:
            selected_index=self.list_tasks.curselection()
            if selected_index:
                index=int(selected_index[0])
                removed_task=self.tasks.pop(index)
                self.list_tasks.delete(selected_index)
                messagebox.showinfo("Success",f"Task `{removed_task}` removed successfully.")
            else:
                messagebox.showwarning("Warning","No Task Selected.")
        except IndexError:
            messagebox.showwarning("Warning","Invalid Selection.")
    
    def run(self):
        self.window.mainloop()

task=TASK()
task.run()
        