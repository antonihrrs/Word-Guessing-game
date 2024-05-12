import tkinter
import random
import string

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

def conclude_get_name(event=None):
    instruction_text.forget()
    yes_button.pack_forget()
    no_button.pack_forget()
    greeting_text.config(text=f"Great :) Welcome, {user_name}!")
    greeting_text.pack()
    window.after(1500, lambda: greeting_text.pack_forget())
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
    random_letters_gen()
    window.after(2000, lambda: letters_gen_showing_up.pack_forget())
    window.after(2450, lambda: begin_word_message())

def begin_word_message():
    word_text.config(text="🔮 A word has been picked out 🔮")
    word_text.pack()


window = tkinter.Tk()
window.title("🔮 Guess them all 🔮")
window.geometry("500x300")

instruction_text = tkinter.Label(window, text="Enter your name : ")
instruction_text.pack()

user_box = tkinter.Entry(window)
user_box.pack()

user_box.bind("<Return>", get_name)

submit_button = tkinter.Button(window, text="Submit", command=get_name)
submit_button.pack()

yes_button = tkinter.Button(window, text="Yes", command=conclude_get_name)
no_button = tkinter.Button(window, text="No", command=ask_name_again)
start_button = tkinter.Button(window, text="Start", command=begin)
leave_button = tkinter.Button(window, text="Leave", command=leaving)

greeting_text = tkinter.Label(window)
ask_start_text = tkinter.Label(window)

leave_text = tkinter.Label(window)

letters_gen = tkinter.StringVar()
letters_gen_showing_up = tkinter.Label(window, textvariable=letters_gen)
letters_gen_showing_up.pack()

window.mainloop()
