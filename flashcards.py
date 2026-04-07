import ttkbootstrap as ttk
from config import *

class flashcardsApp(ttk.Window):
    def __init__(self):
        super().__init__()

        self.title("Flashcards App")
        self.geometry("420x780")
        self.resizable(False, False)
        self.configure(bg=BACKGROUND_COLOR)

        setup_styles()

        self.current_page = ttk.Frame(self)
        self.current_page.pack(fill="both")

        self.header()
        self.text_card()
        self.center_card()
        self.button_answer()
    
    def header(self):
        card = ttk.Frame(self.current_page, style="Card2.TFrame")
        card.pack(fill="both", expand=True, padx=20, pady=10)

        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=2)
        card.columnconfigure(2, weight=1)

        btn = ttk.Button(
            card,
            text="⬅",
            style="Arrow.TButton",
            padding=(20, 15),
        )
        btn.grid(row=0, column=0, sticky="w")

        title_label = ttk.Label(
            card,
            text="PYTHON",
            font=PIXEL_FONT,
            foreground=PRIMARY_COLOR,
        )
        title_label.grid(row=0, column=1, padx=30, sticky="nsew")

    def text_card(self):
        card = ttk.Frame(self.current_page, style="Card2.TFrame")
        card.pack(fill="both", expand=True, padx=20, pady=10)

        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=1)
        card.columnconfigure(2, weight=1)

        title_label = ttk.Label(
            card,
            text="Question",
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2,
            anchor="center"
        )
        title_label.grid(row=0, column=1, padx=60, sticky="nsew")

    def center_card(self):
        card = ttk.Frame(self.current_page, width=360, height=370, style="Card.TFrame")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)
        
        title_label = ttk.Label(
            card,
            text="SOMETHING SOMETHING SOMETHING SOMETHING SOMETHING SOMETHING",
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR,
            anchor="center",
            wraplength=400
        )
        title_label.pack(expand=True)

    def button_answer(self):
        card = ttk.Frame(self.current_page, width=360, height=60)
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        btn = ttk.Button(
            card,
            text="ANSWER",
            style="Filled.TButton",
            padding=(20, 15),
        )
        btn.pack(expand=True, fill="both")




if __name__ == "__main__":
    app = flashcardsApp()
    app.mainloop()