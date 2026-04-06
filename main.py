import tkinter as tk
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Flashcards App")
        self.geometry("1080x720")


        self.button = ttk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        print("Button clicked!")

root = App()
root.mainloop()