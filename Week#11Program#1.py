#UNWSP Programming PythonCos2005DEsp25
#Program_1_Phrase Window
#04.11.25
#Abraham. N. Andersen

import tkinter as tk

window = tk.Tk()
window.title("Favorite Phrase Window")

message_label = tk.Label(window, text="But God being rich in mercy...")
message_label.pack(padx=20, pady=20)

window.mainloop()