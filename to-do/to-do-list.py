import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('Welcome')

tk.Label(root, text='To Do List', font=('Arial', 28)).grid(row=4, column=2)


root.mainloop()
