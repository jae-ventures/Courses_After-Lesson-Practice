import tkinter as tk
import ttkbootstrap as ttk

# setup
window = ttk.Window(title = 'buttons', minsize = (600, 400), themename = 'darkly')

# button
def button_func():
  print('a basic button')
  print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A simple button', textvariable = button_string, command = button_func)
button.pack(pady = 20)

# checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(
  window,
  text = 'checkbox 1',
  variable = check_var,
  command = lambda: print(f"Type: {type(check_var.get())} value: {check_var.get()}"))
check.pack()

# radio buttons
# Always set a custom value, otherwise your radiobuttons will be synced
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
  window,
  text = 'Radiobutton 1',
  value = 'radio 1',
  variable = radio_var,
  command = button_func)
radio1.pack()

radio2 = ttk.Radiobutton(
  window,
  text = 'Radiobutton 2',
  value = 2,
  variable = radio_var)
radio2.pack()
# run
window.mainloop()