import ttkbootstrap as ttk
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

        box = ttk.Frame(self.current_page, width=360, height=202, style="Card.TFrame")
        box.pack(pady=20)
        box.pack_propagate(False)

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

        self.last_card("ADD MORE")


    def create_card(self, title_text, command=None):
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

    def last_card(self, title_text):
        card = ttk.Frame(self.current_page, width=360, height=80, style="Arrow.TButton")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        btn = ttk.Button(
            card,
            text=title_text,
            style="Arrow.TButton",
            padding=(20, 15)
        )
        btn.pack(side="right", padx=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()