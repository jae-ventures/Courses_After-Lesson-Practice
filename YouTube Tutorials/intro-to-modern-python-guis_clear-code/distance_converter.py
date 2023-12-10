import tkinter as tk
import ttkbootstrap as ttk 

def convert():
  """
  Converts the users input of miles to kilometers

  Parameters:
  N/A

  Returns:
  Sets the output text label to the converted value
  """
  mile_input = entry_int.get()
  km_output = mile_input * 1.61
  output_string.set(f"{km_output} km")

def entry_validation(entry):
  '''
  Checks if the string is empty, a digit, or a deicimal number
  
  Parameters:
  entry (string): text user is typing in entry field

  Returns:
  bool: Determins if entered text is valid or not
  '''
  if entry in ('', '.', '-'):
    return True
  try:
    float(entry)
    return True
  except ValueError:
    return False

# window
window = ttk.Window(
  title = "Distance Converter",
  themename = 'darkly',
  minsize = (300, 200))

# title
title_label = ttk.Label(
  master = window,
  text = "Miles to Kilometers",
  font = ("Monospace", 24, "bold"))
title_label.pack(pady=10, padx=50)

# input field
input_frame = ttk.Frame(
  master = window)
entry_int = ttk.DoubleVar()
vcmd = (window.register(entry_validation), '%P')
entry = ttk.Entry(
  master = input_frame,
  textvariable = entry_int,
  validate='key',
  validatecommand=vcmd)
button = ttk.Button(
  master = input_frame,
  text = 'Convert',
  command = convert)
entry.pack(pady=10, padx=10, side='left')
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = ttk.StringVar()
outpuut_label = ttk.Label(
  master = window,
  text = "Output",
  font = ("Monospace", 24),
  textvariable = output_string)
outpuut_label.pack(pady = 5)

# run
window.mainloop()