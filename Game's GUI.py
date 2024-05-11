import tkinter

def get_name(event=None):
    global user_name
    user_name = user_box.get()
    user_box.delete(0, 'end')
    instruction_text.config(text=f"Your name is {user_name}. Do you want to keep it?")
    user_box.pack_forget()
    submit_button.pack_forget()
    yes_button.pack()
    no_button.pack()

def ask_name_again():
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
    window.after(1700, lambda: greeting_text.pack_forget())
    window.after(2000, lambda: ask_start())

def ask_start(event=None):
    ask_start_text.config(text="Do you want do begin ?")
    ask_start_text.pack()
    start_button.pack()
    leave_button.pack()

def game(event=None):
    ask_start_text.pack_forget()
    start_button.pack_forget()
    leave_button.pack_forget()
    game_placeholder_text.config(text="The game will be here soon 🔮")
    game_placeholder_text.pack()

def leaving():
    ask_start_text.forget()
    start_button.forget()
    leave_button.forget()
    leave_text.config(text="Bye felicia 🍄")
    leave_text.pack()
    window.after(2000, lambda: window.destroy())


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
start_button = tkinter.Button(window, text="Start", command=game)
leave_button = tkinter.Button(window, text="Leave", command=leaving)

greeting_text = tkinter.Label(window)
ask_start_text = tkinter.Label(window)

leave_text = tkinter.Label(window)

game_placeholder_text = tkinter.Label(window)

window.mainloop()
