import ctypes
import os
from matplotlib import style
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# Colors
PRIMARY_COLOR = "#F8B9C2"
PRESSED_COLOR = "#AA5764"
SECONDARY_COLOR = "#AAB8DB"
BACKGROUND_COLOR = "#FFF9FA"
TEXT_COLOR1 = "#FDFDFD"
TEXT_COLOR2 = "#1E1E1E"

def load_fonts():
    font_paths = [
        "assets/PixelOperator.ttf",
        "assets/PixelOperator-Bold.ttf",
    ]

    for path in font_paths:
        full_path = os.path.abspath(path)
        ctypes.windll.gdi32.AddFontResourceExW(full_path, 0x10, 0)
load_fonts()

# Fonts
PIXEL_FONT = ("Pixel Operator", 24)
PIXEL_FONT_SMALL = ("Pixel Operator", 19)
PIXEL_FONT_MINITURE = ("Pixel Operator", 10)
PIXEL_FONT_CARD = ("Pixel Operator", 16)
PIXEL_FONT_BOLD = ("Pixel Operator Bold", 24)
PIXEL_FONT_BOLD_SMALL = ("Pixel Operator Bold", 19)


def setup_styles():
    style = ttk.Style()

    style.configure(
        "Card.TFrame",
        background=BACKGROUND_COLOR,
        bordercolor=PRIMARY_COLOR,
        relief="solid",
        borderwidth=2
    )

    style.configure(
        "Card3.TFrame",
        background="gray",
        bordercolor=PRIMARY_COLOR,
        relief="solid",
        borderwidth=2
    )

    style.configure(
        "Card.TLabel",
        background=BACKGROUND_COLOR
    )

    style.configure(
        "Card2.TFrame",
    )

    style.configure(
        "Arrow.TButton",
        bordercolor=PRIMARY_COLOR,
        background=BACKGROUND_COLOR,
        foreground=PRIMARY_COLOR,
        font=PIXEL_FONT_CARD,
        borderwidth=2,
        relief="solid",
        padding=(20, 15)
    )

    style.map(
        "Arrow.TButton",
        background=[
            ("active", BACKGROUND_COLOR),
            ("pressed", PRIMARY_COLOR)
        ],
        foreground=[
            ("active", PRIMARY_COLOR),
            ("pressed", "white")
        ]
    )

    style.configure(
        "Outlined.TButton",
        foreground=PRIMARY_COLOR,
        font=PIXEL_FONT_SMALL,
        borderwidth=2,
        bordercolor=PRIMARY_COLOR,
        background=BACKGROUND_COLOR,
        relief="solid",
        padding=(20, 15)
    )

    style.map(
        "Outlined.TButton",
        foreground=[
            ("pressed", PRIMARY_COLOR),
            ("active", "white")
        ],
        background=[
            ("pressed", "white"),
            ("active", PRIMARY_COLOR)
        ],
        bordercolor=[
        ("pressed", PRIMARY_COLOR),
        ("active", PRIMARY_COLOR)
        ]
    )

    style.configure(
        "Filled.TButton",
        background=PRIMARY_COLOR,
        foreground="white", 
        font=PIXEL_FONT_SMALL,
        borderwidth=0,
        padding=(30, 15)
    )

    style.configure(
        "Page.TLabel",
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR2,
        font=PIXEL_FONT
    )

    style.map(
        "Filled.TButton",
        background=[("active", PRIMARY_COLOR), ("pressed", PRESSED_COLOR)],
        foreground=[("active", "white"), ("pressed", "white")]
    )

    style.configure(
            "Page.TFrame",
            background=BACKGROUND_COLOR
    )
    return style