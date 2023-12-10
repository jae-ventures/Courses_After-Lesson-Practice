import tkinter as tk
import ttkbootstrap as ttk

def button_func():
  print(string_var.get())
  string_var.set('button pressed')

# create a window
window = ttk.Window(
  title='Tkinter Variables',
  minsize = (1000, 400),
  themename = 'darkly')

# tkinter variable
string_var = tk.StringVar()
string_var1 = tk.StringVar(value='test')

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack(pady = 20)

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text='button', command = button_func)
button.pack()

# exercise
label1 = ttk.Label(master = window, text = 'label1', textvariable = string_var1)
label1.pack(pady=30)
entry1 = ttk.Entry(master = window, textvariable = string_var1)
entry1.pack()
entry2 = ttk.Entry(master = window, textvariable = string_var1)
entry2.pack()

# run
# mainloop() will prevent any further execution. Any other lines of code have to wait until after
window.mainloop()
print('hello')