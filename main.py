from os import name
from turtle import left
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from config import *

class App(ttk.Window):
    def __init__(self):
        super().__init__()

        self.title("Flashcards App")
        self.geometry("420x780")
        self.resizable(False, False)
        self.configure(bg=BACKGROUND_COLOR)

        setup_styles()

        self.current_page = None
        self.show_main_page()
        self.profile_card()
        self.things_to_learn()
        self.last_card()

    def clear_page(self):
        if self.current_page is not None:
            self.current_page.destroy()

    def show_main_page(self):
        self.clear_page()

        self.current_page = ttk.Frame(self, style="Page.TFrame")
        self.current_page.pack(fill="both", expand=True)

        title_label = ttk.Label(
            self.current_page,
            text="Flashcards",
            font=PIXEL_FONT,
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR
        )
        title_label.pack(pady=20)

    def profile_card(self):
        box = ttk.Frame(self.current_page, width=360, height=202, style="Card.TFrame")
        box.pack(pady=20)
        box.pack_propagate(False)

        box.columnconfigure(0, weight=1)
        box.columnconfigure(1, weight=1)
        box.rowconfigure(0, weight=1)

        #nimi ja muud asjad
        right = tk.Frame(box, bg=BACKGROUND_COLOR)
        right.grid(row=0, column=1, padx=(20, 60), pady=24, sticky="nw")

        label_name = ttk.Label(
            right,
            text="Faya",
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR,
            style="Card.TLabel"
        )
        label_name.pack(anchor="w")

        streak_title = ttk.Label(
            right,
            text="Streak:",
            font=PIXEL_FONT_MINITURE,
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR
        )
        streak_title.pack(pady=(10, 0),anchor="w")

        streak_value = ttk.Label(
            right,
            text="2 DAYS",
            font=PIXEL_FONT_SMALL,
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR
        )
        streak_value.pack(anchor="w", pady=(0, 8))

        Learning_title = ttk.Label(
            right,
            text="Learning:",
            font=PIXEL_FONT_MINITURE,
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR
        )
        Learning_title.pack(pady=(0, 0),anchor="w")

        Learning_value = ttk.Label(
            right,
            text="PYTHON",
            font=PIXEL_FONT_SMALL,
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR
        )
        Learning_value.pack(anchor="w", pady=(0, 12))


        #profile pic ja edit prof
        left = ttk.Frame(box)
        left.grid(row=0, column=0, padx=(30, 10), pady=18, sticky="nw")

        profile_pic = ttk.Frame(left, width=140, height=150, style="Card3.TFrame")
        profile_pic.pack()
        profile_pic.pack_propagate(False)

        img = Image.open("assets/profile.png")
        img = img.resize((140, 150))
        photo = ImageTk.PhotoImage(img)

        pic_label = ttk.Label(profile_pic, image=photo)
        pic_label.image = photo
        pic_label.pack(expand=True, fill="both")

        edit_profile = ttk.Label(
            left,
            text="Edit Profile",
            font=PIXEL_FONT_MINITURE,
            foreground=SECONDARY_COLOR,
            background=BACKGROUND_COLOR
        )
        edit_profile.pack(pady=(5, 0))


    def things_to_learn(self):
        header = ttk.Label(
            self.current_page,
            text="Things to learn",
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR
        )
        header.pack(pady=10, anchor="w", padx=30)

        self.create_card("Python")
        self.create_card("Thermodynamics")
        self.create_card("Brainrot")


    def create_card(self, title_text):
        card = ttk.Frame(self.current_page, width=360, height=80, style="Card.TFrame")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        label = ttk.Label(
            card,
            text=title_text,
            font=PIXEL_FONT_CARD,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR
        )
        label.pack(side="left", padx=20)

        btn = ttk.Button(
            card,
            text="➜",
            style="Arrow.TButton",
            padding=(20, 15),
        )
        btn.pack(side="right", padx=20)

    def last_card(self):
        card = ttk.Frame(self.current_page, width=360, height=60)
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        btn = ttk.Button(
            card,
            text="ADD MORE",
            style="Outlined.TButton"
        )
        btn.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()