import tkinter
import random
import string

window = tkinter.Tk()
window.title("🔮 Guess them all 🔮")
window.geometry("500x300")

words_list = ["infrastructure","compactness", "topology", "transcendence", "divination", "mmniscient", "effervescent", 
             "echolocation", "vicissitudes", "homeomorphism", "multifariousness", "acupuncture", "malevolent", "quintessential", "promiscuous",
              "ephemeral", "luminious", "cacophony", "rehabilitation", "testimony", "encryption", "jurisdiction", "prescription", "thermodynamic",
               "accreditation", "biodegradable", "sustainability", "segmentation", "psychopathology", "aesthetic", "correspondent", "cultivation",
                "irrigation","rainbow", "butterfly","ecosystem", "symphony", "victory", "triumphant", "courage", "satisfaction", "motivation", "expectation",
                  "melody", "persuasion", "competition", "quest", "elephant", "precious", "beautiful", "horticulture", "contradiction", "tornado", "fiction",
                   "playfulness", "component", "honorific", "electronic", "intelligence", "authoritarianism", "fluctuation", ]

instruction_text = tkinter.Label(window, text="Enter your name : ")
instruction_text.place(anchor="center")
instruction_text.pack()

def get_name(event=None):
    global user_name
    user_name = user_box.get()
    user_box.delete(0, 'end')
    instruction_text.config(text=f"Your name is {user_name}. Do you want to keep it?")
    user_box.pack_forget()
    submit_button.pack_forget()
    yes_button.pack()
    no_button.pack()

def ask_name_again(event=None):
    instruction_text.config(text="Enter your name : ")
    user_box.pack()
    submit_button.pack()
    yes_button.pack_forget()
    no_button.pack_forget()
    greeting_text.pack_forget()

def wizard():
    wizard_emoji.config(text="🧙‍♂️")
    wizard_emoji.pack()

def corner_name():
    name_of_user.config(text=user_name)

def conclude_get_name(event=None):
    instruction_text.forget()
    yes_button.pack_forget()
    no_button.pack_forget()
    wizard()
    greeting_text.config(text=f"Hi {user_name} ! Nice to meet you !")
    greeting_text.pack()
    window.after(1500, lambda: greeting_text.pack_forget())
    window.after(1600, lambda: corner_name())
    window.after(1750, lambda: ask_start())

def ask_start(event=None):
    ask_start_text.config(text="Do you want do begin ?")
    ask_start_text.pack()
    start_button.pack()
    leave_button.pack()

def leaving():
    ask_start_text.forget()
    start_button.forget()
    leave_button.forget()
    leave_text.config(text="Bye felicia 🍄")
    leave_text.pack()
    window.after(2000, lambda: window.destroy())

def get_letters():
    letters = ""
    for _ in range(1):
        line = " ".join(random.choices(string.ascii_lowercase, k=14))
        letters += line + "\n"
    return letters

def random_letters_gen():
    random_letters = get_letters()
    letters_gen.set(random_letters)
    letters_gen_showing_up.config(text=random_letters)
    window.after(125, random_letters_gen)

def begin(event=None):
    ask_start_text.pack_forget()
    start_button.pack_forget()
    leave_button.pack_forget()
    wizard_emoji.pack_forget()
    random_letters_gen()
    window.after(2000, lambda: letters_gen_showing_up.pack_forget())
    window.after(2450, lambda: begin_word_message())

def begin_word_message():
    wizard_emoji.pack()
    word_text.config(text="🔮 A word has been picked out 🔮")
    word_text.pack()
    window.after(1000, lambda: word_lengh_show_up())
    window.after(2700, lambda: game())
    window.after(2700, lambda: tries_nb())

def get_word():
    word = random.choice(words_list)
    return word

word = get_word()
word_length = len(word)
guessed_word = ["_"] * len(word)

def word_lengh_show_up():
    word_lengh_text.config(text="The number of characters : " + str(word_length) + "\n")
    word_lengh_text.pack()

def blank_spaces():
    letters_by_letters.config(text="")
    for i in word:
        letters_by_letters.config(text=letters_by_letters.cget("text") + " _ ")
    letters_by_letters.pack()

def user_guess_box():
    user_box_guess = tkinter.Entry(window)
    user_box_guess.pack()

tries = 0
def tries_nb():
    global tries
    number_of_tries.config(text= f"Tries = {tries}")

def game():
    word_text.pack_forget()
    window.after(500, lambda: blank_spaces())
    window.after(500, lambda: user_guess_box())

user_box = tkinter.Entry(window)
user_box.place(anchor="center")
user_box.pack()

user_box.bind("<Return>", get_name)

submit_button = tkinter.Button(window, text="Submit", command=get_name)
submit_button.place(anchor="center")
submit_button.pack()

yes_button = tkinter.Button(window, text="Yes", command=conclude_get_name)
no_button = tkinter.Button(window, text="No", command=ask_name_again)
start_button = tkinter.Button(window, text="Start", command=begin)
leave_button = tkinter.Button(window, text="Leave", command=leaving)

letters_gen = tkinter.StringVar()
letters_gen_showing_up = tkinter.Label(window, textvariable=letters_gen)
letters_gen_showing_up.pack()

wizard_emoji = tkinter.Label(window)
wizard_emoji.place(anchor="center")

name_of_user = tkinter.Label()
name_of_user.place(x=15, y=5, anchor="nw")

number_of_tries = tkinter.Label()
number_of_tries.place(x=15, y=25, anchor="nw")

greeting_text = tkinter.Label(window)
ask_start_text = tkinter.Label(window)
leave_text = tkinter.Label(window)
word_text = tkinter.Label(window)
guessed_word = tkinter.Label(window)
character_number = tkinter.Label(window)
letters_by_letters = tkinter.Label(window)
word_lengh_text = tkinter.Label(window)


window.mainloop()
