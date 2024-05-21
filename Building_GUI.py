import tkinter
import random
import string

window = tkinter.Tk()
window.title("🔮 Guess them all 🔮") 
window.geometry("525x300+460+230")
left_side_bg = tkinter.Label(fg="white", bg="#A7BCD9", width=8)
left_side_bg.pack(side="left", fill="y")
right_side_bg = tkinter.Label(fg="white", bg="#A7BCD9", width=8)
right_side_bg.pack(side="right", fill="y")

words_list = ["infrastructure","compactness", "topology", "transcendence", "divination", "omniscient", "effervescent", 
             "echolocation", "vicissitudes", "homeomorphism", "multifariousness", "acupuncture", "malevolent", "quintessential", "promiscuous",
              "ephemeral", "luminious", "cacophony", "rehabilitation", "testimony", "encryption", "jurisdiction", "prescription", "thermodynamic",
               "accreditation", "biodegradable", "sustainability", "segmentation", "psychopathology", "aesthetic", "correspondent", "cultivation",
                "irrigation","rainbow", "butterfly","ecosystem", "symphony", "victory", "triumphant", "courage", "satisfaction", "motivation", "expectation",
                  "melody", "persuasion", "competition", "quest", "elephant", "precious", "beautiful", "horticulture", "contradiction", "tornado", "fiction",
                   "playfulness", "component", "honorific", "electronic", "intelligence", "authoritarianism", "fluctuation", ]

instruction_text = tkinter.Label(window, text="Enter your name : ", font=("",16))
instruction_text.pack()

def get_name(event=None):
    global user_name
    user_name = user_box.get()
    user_box.delete(0, 'end')
    user_box.pack_forget()
    submit_button.pack_forget()
    instruction_text.config(text=f"Your name is {user_name}.\nDo you want to keep it?")
    yes_button.pack()
    no_button.pack()
    user_box.unbind("<Return>", get_name)

def ask_name_again(event=None):
    instruction_text.config(text="Enter your name : ")
    user_box.bind("<Return>", get_name)
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
    window.after(1600, lambda: greeting_text.pack_forget())
    window.after(1600, lambda: corner_name())
    window.after(1700, lambda: ask_start())

def ask_start():
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
    ask_start_text.forget()
    start_button.forget()
    leave_button.forget()
    random_letters_gen()
    window.after(2200, lambda: letters_gen_showing_up.forget())
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

tries = 0
def tries_nb():
    global tries
    number_of_tries_display.config(text= f"Tries: {tries}")

def check(event=None):
    global tries
    global guessed_word
    global display_guessed_word

    user_letter = user_box_guess.get()
    
    if "_" in guessed_word:

        if user_letter.isalpha()and len(user_letter) == 1 :
            tries += 1
            tries_nb()
            if user_letter in word :
                for i in range(len(word)):
                    if word[i] == user_letter:
                        guessed_word[i] = user_letter
                display_guessed_word = " ".join(guessed_word)
                letters_by_letters.config(text=display_guessed_word)
                user_box_guess.delete(0, 'end')
                
            else:
                letter_not_in_word.config(text=f"' {user_letter} ' is not in the word")
                letter_not_in_word.pack()
                user_box_guess.delete(0, 'end')
                window.after(1000, lambda: letter_not_in_word.forget())
        
        else:
            nope_message.config(text="🪄 Nope")
            nope_message.pack()
            user_box_guess.delete(0, 'end')
            window.after(1000, lambda: nope_message.forget())
    
    else:
        word_lengh_text.forget()
        check_button.forget()
        user_box_guess.forget()
        letters_by_letters.forget()
        leave_corner.forget()
        end_message.config(text=f"Congrats {user_name} ✨ \nYou've guessed the word '{word}' correctly !")
        end_message.pack()
        window.after(2000, lambda: happy_end_message())

def happy_end_message():

    if tries >= len(word) * 2.5:
        number_of_tries_message.config(text=f"Ouch... It took you {tries} tries to guess {word_length} letters !")
        number_of_tries_message.pack()
            
    elif tries <= len(word) * 2.5 and tries >= len(word) * 1.75:
        number_of_tries_message.config(text=f"It took you {tries} tries to find those {word_length} letters.")
        number_of_tries_message.pack()

    elif tries <= len(word) * 1.75 and tries >= len(word) * 1.1:
        number_of_tries_message.config(text=f"It only took you {tries} tries to guess all {word_length} letters ! Nice")
        number_of_tries_message.pack()
    else:
        number_of_tries_message.config(text=f"Woah it only took you {tries} tries to guess '{word}'\nand all it's {word_length} letters !\n🤯 Amazing !")
        number_of_tries_message.pack()
    
    window.after(2500, lambda:play_again_ask())
    
def play_again_ask():
    play_again_message.config(text="Play again ?")
    play_again_message.pack()
    window.after(1200, lambda: play_again_button.pack())
    window.after(1400, lambda:leave_button.pack())

def reset_game():
    global word, word_length, guessed_word, tries
    word = get_word()
    word_length = len(word)
    guessed_word = ["_"] * len(word)
    tries = 0 
    tries_nb()

def play_again_clicked():
    reset_game()
    play_again_button.forget()
    end_message.forget()
    number_of_tries_message.forget()
    play_again_button.forget()
    play_again_message.forget()
    letters_gen_showing_up.pack()
    begin()

def game():
    word_text.pack_forget()
    window.after(500, lambda: blank_spaces())
    window.after(500, lambda: user_box_guess.pack())
    check_button.pack()
    leave_corner.pack(side="bottom", anchor="se")

user_box = tkinter.Entry(window)
user_box.bind("<Return>", get_name)
user_box.pack(side="top")

user_box_guess = tkinter.Entry(window)
user_box_guess.bind("<Return>", check)

submit_button = tkinter.Button(window, text="Submit", command=get_name)
submit_button.pack()

yes_button = tkinter.Button(window, text="Yes", command=conclude_get_name)
no_button = tkinter.Button(window, text="No", command=ask_name_again)
start_button = tkinter.Button(window, text="Start", command=begin)
leave_button = tkinter.Button(window, text="Leave", command=leaving)
check_button = tkinter.Button(window, text="Check", anchor="s", command=check)
play_again_button = tkinter.Button(window, text="Pay again", command=play_again_clicked)
leave_corner = tkinter.Button(window, text="Leave", command=leaving, fg="Black", bg="white")

letters_gen = tkinter.StringVar()
letters_gen_showing_up = tkinter.Label(window, textvariable=letters_gen, font=("",16))
letters_gen_showing_up.pack()

wizard_emoji = tkinter.Label(window, font=("",49))
wizard_emoji.place(anchor="center")

name_of_user = tkinter.Label(window, bg="#A7BCD9", fg="black")
name_of_user.place(x=5, y=5, anchor="nw")

number_of_tries_display = tkinter.Label(window, bg="#A7BCD9", fg="black")
number_of_tries_display.place(x=5, y=25, anchor="nw")
number_of_tries_message = tkinter.Label(window)

greeting_text = tkinter.Label(window, font=("",16))
ask_start_text = tkinter.Label(window, font=("",16))
leave_text = tkinter.Label(window, font=("",16))
word_text = tkinter.Label(window, font=("",16))
character_number = tkinter.Label(window, font=("",16))
letters_by_letters = tkinter.Label(window, font=("",16))
word_lengh_text = tkinter.Label(window, font=("",16))
letter_not_in_word = tkinter.Label(window, font=("",16))
nope_message = tkinter.Label(window, font=("",16))
end_message =tkinter.Label(window, font=("",16))
play_again_message = tkinter.Label(window, font=("",16))

window.mainloop()