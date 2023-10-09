# Import necessary modules
import tkinter as tk

# Define the application class
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add widgets here
        pass

# Create the application
root = tk.Tk()
app = Application(master=root)
app.mainloop()