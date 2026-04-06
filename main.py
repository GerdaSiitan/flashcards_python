import ctypes
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Flashcards App")
        self.geometry("420x780")
        self.resizable(False, False)

        self.primary_color = "#F8B9C2"
        self.secondary_color = "#AAB8DB"
        self.background_color = "#FFF9FA"
        self.text_color1 = "#FDFDFD"
        self.text_color2 = "#1E1E1E"

        self.configure(bg=self.background_color)

        ctypes.windll.gdi32.AddFontResourceExW("assets/PixelOperator.ttf", 0x10, 0)
        self.pixel_font = ("PixelOperator", 24)
        self.pixel_font_small = ("PixelOperator", 19)
        self.pixel_font_card = ("PixelOperator", 16)

        title_label = ttk.Label(
            self,
            text="Flashcards",
            font=self.pixel_font,
            foreground=self.primary_color,
            background=self.background_color
        )
        title_label.pack(pady=20)

        style = ttk.Style()
        style.configure(
            "Card.TFrame",
            background="#FFF9FA",
            bordercolor=self.primary_color,
            relief="solid",
            borderwidth=2
        )

        style.configure(
            "Arrow.TButton",
            bordercolor=self.primary_color,
            background=self.background_color,
            font=self.pixel_font_card,
            borderwidth=2,
            foreground=self.primary_color,
            relief="solid"
        )

        box = ttk.Frame(self, width=360, height=202, style="Card.TFrame")
        box.pack(pady=20)
        box.pack_propagate(False)

        header = ttk.Label(
            self,
            text="Things to learn",
            font=self.pixel_font_small,
            foreground=self.text_color2,
            background=self.background_color
        )
        header.pack(pady=10, anchor="w", padx=30)

        self.create_card("Python")
        self.create_card("Thermodynamics")
        self.create_card("Brainrot")

        self.last_card("Brainrot")

    def create_card(self, title_text):
        card = ttk.Frame(self, width=360, height=80, style="Card.TFrame")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        label = ttk.Label(
            card,
            text=title_text,
            font=("PixelOperator", 16),
            foreground=self.text_color2,
            background=self.background_color
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
        card = ttk.Frame(self, width=360, height=80, style="Arrow.TButton")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        btn = ttk.Button(
        card,
        text=title_text,
        style="Arrow.TButton",
        padding=(20, 15),
        )
        btn.pack(side="right", padx=20)

root = App()
root.mainloop()