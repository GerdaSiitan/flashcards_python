import ctypes
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

# Load font
ctypes.windll.gdi32.AddFontResourceExW("assets/PixelOperator.ttf", 0x10, 0)

# Fonts
PIXEL_FONT = ("PixelOperator", 24)
PIXEL_FONT_SMALL = ("PixelOperator", 19)
PIXEL_FONT_MINITURE = ("PixelOperator", 10)
PIXEL_FONT_CARD = ("PixelOperator", 16)


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
        font=PIXEL_FONT_CARD,
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
        font=PIXEL_FONT_CARD,
        borderwidth=0,
        padding=(20, 15)
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