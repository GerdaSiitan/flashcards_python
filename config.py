import ctypes
import ttkbootstrap as ttk

# Colors
PRIMARY_COLOR = "#F8B9C2"
SECONDARY_COLOR = "#AAB8DB"
BACKGROUND_COLOR = "#FFF9FA"
TEXT_COLOR1 = "#FDFDFD"
TEXT_COLOR2 = "#1E1E1E"

# Load font
ctypes.windll.gdi32.AddFontResourceExW("assets/PixelOperator.ttf", 0x10, 0)

# Fonts
PIXEL_FONT = ("PixelOperator", 24)
PIXEL_FONT_SMALL = ("PixelOperator", 19)
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
        "Arrow.TButton",
        bordercolor=PRIMARY_COLOR,
        background=BACKGROUND_COLOR,
        font=PIXEL_FONT_CARD,
        borderwidth=2,
        foreground=PRIMARY_COLOR,
        relief="solid"
    )

    style.configure(
        "Page.TFrame",
        background=BACKGROUND_COLOR
    )

    return style