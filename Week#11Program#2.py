#UNWSP Programming PythonCos2005DEsp25
#Program_2_Name and Address Pop-up
#04.11.25
#Abraham. N. Andersen

import tkinter as tk
from tkinter import messagebox

def show_info():
    """Displays your name and address in a pop-up box."""
    name = "Abraham Andersen"
    address = "2601 13th Ave S\nMinneapolis, Minnesota, 55407"
    messagebox.showinfo("Info", f"Name: {name}\nAddress:\n{address}")

def quit_program():
    """Closes the main window."""
    window.destroy()


window = tk.Tk()
window.title("Info Window")


show_button = tk.Button(window, text="Show Info", command=show_info)
show_button.pack(pady=10)


quit_button = tk.Button(window, text="Quit", command=quit_program)
quit_button.pack(pady=5)


window.mainloop()