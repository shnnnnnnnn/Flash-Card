from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
word_translation = {}

try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
    word_translation = original_file.to_dict(orient="records")
else:
    word_translation = words.to_dict(orient="records")


def get_random_french_word():

    global current_card, delay
    window.after_cancel(delay)
    current_card = random.choice(word_translation)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    delay = window.after(3000, flip_the_card)


def flip_the_card():

    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")


def save_progress():

    word_translation.remove(current_card)
    words = pandas.DataFrame(word_translation)
    words.to_csv("./data/words_to_learn.csv", index=False)

    get_random_french_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

delay = window.after(3000, flip_the_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_back_img = PhotoImage(file="./images/card_back.png")

card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))

card_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bd=0, command=save_progress)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=get_random_french_word)
wrong_button.grid(column=0, row=1)

get_random_french_word()

window.mainloop()
