import ttkbootstrap as ttk

from config import *
from main import App
import python_questions
import thermo_questions
import brainrot_questions

CATEGORY_DATA = {
    "Python": python_questions.PYTHON_FLASHCARDS,
    "Thermodynamics": thermo_questions.THERMO_FLASHCARDS,
    "Brainrot": brainrot_questions.BRAINROT_FLASHCARDS
}
class FullApp(App):
    def clear_page(self):
        if self.current_page is not None:
            self.current_page.destroy()
            self.current_page = None

    def create_card(self, title_text):
        card = ttk.Frame(self.current_page, width=360, height=80, style="Card.TFrame")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        label = ttk.Label(
            card,
            text=title_text,
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR
        )
        label.pack(side="left", padx=20)

        btn = ttk.Button(
            card,
            text="➜",
            style="Arrow.TButton",
            padding=(20, 15),
            command=lambda t=title_text: self.show_study_page(t)
        )
        btn.pack(side="right", padx=20)

    def show_study_page(self, category):
        self.clear_page()

        self.current_category = category
        self.flashcards = CATEGORY_DATA[category]

        self.index = 0
        self.showing_answer = False

        self.current_page = ttk.Frame(self, style="Page.TFrame")
        self.current_page.pack(fill="both", expand=True)

        self.study_header()
        self.study_label()
        self.study_card()
        self.study_buttons()

    def study_header(self):
        card = ttk.Frame(self.current_page, style="Card2.TFrame")
        card.pack(fill="x", padx=20, pady=10)

        btn = ttk.Button(
            card,
            text="⬅",
            style="Arrow.TButton",
            padding=(20, 15),
            command=self.show_main_page_again
        )
        btn.pack(side="left")

        title = ttk.Label(
            card,
            text=self.current_category.upper(),
            font=PIXEL_FONT,
            foreground=PRIMARY_COLOR
        )
        title.pack(side="left", padx=45)

    def study_label(self):
        card = ttk.Frame(self.current_page, style="Card2.TFrame")
        card.pack(fill="x", padx=20, pady=10)

        self.mode_label = ttk.Label(
            card,
            text="Question",
            font=PIXEL_FONT_SMALL,
            foreground=TEXT_COLOR2
        )
        self.mode_label.pack()

    def study_card(self):
        card = ttk.Frame(self.current_page, width=360, height=370, style="Card.TFrame")
        card.pack(pady=10, padx=20)
        card.pack_propagate(False)

        self.card_text = ttk.Label(
            card,
            text=self.flashcards[self.index]["question"],
            font=PIXEL_FONT,
            foreground=TEXT_COLOR2,
            background=BACKGROUND_COLOR,
            anchor="center",
            wraplength=320
        )
        self.card_text.pack(expand=True)

    def study_buttons(self):
        self.flip_btn = ttk.Button(
            self.current_page,
            text="ANSWER",
            style="Filled.TButton",
            command=self.flip_card
        )
        self.flip_btn.pack(fill="x", padx=20, pady=10)

        self.next_btn = ttk.Button(
            self.current_page,
            text="NEXT ➜",
            style="Arrow.TButton",
            command=self.next_card
        )
        self.next_btn.pack(fill="x", padx=20, pady=10)

    def flip_card(self):
        self.showing_answer = not self.showing_answer

        if self.showing_answer:
            self.mode_label.config(text="Answer")
            self.card_text.config(text=self.flashcards[self.index]["answer"])
            self.flip_btn.config(text="FLIP BACK TO QUESTION")
        else:
            self.mode_label.config(text="Question")
            self.card_text.config(text=self.flashcards[self.index]["question"])
            self.flip_btn.config(text="ANSWER")

    def next_card(self):
        self.index = (self.index + 1) % len(self.flashcards)
        self.showing_answer = False

        self.mode_label.config(text="Question")
        self.card_text.config(text=self.flashcards[self.index]["question"])
        self.flip_btn.config(text="ANSWER")

    def show_main_page_again(self):
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
        title_label.pack(pady=25)

        self.profile_card()
        self.things_to_learn()
        self.last_card()


if __name__ == "__main__":
    app = FullApp()
    app.mainloop()