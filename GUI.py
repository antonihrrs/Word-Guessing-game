import tkinter

def get_name():
    global user_name
    user_name = user_box.get()
    user_box.delete(0, 'end')
    instruction_text.config(text=f"Your name is {user_name}. Do you want to keep it?")
    user_box.pack_forget()
    submit_button.pack_forget()
    yes_button.pack()
    no_button.pack()

def continue_code():
    instruction_text.forget()
    yes_button.pack_forget()
    no_button.pack_forget()
    greeting_text.config(text=f"Great :) Welcome, {user_name}!")
    greeting_text.pack()

def ask_name_again():
    instruction_text.config(text="Enter your name : ")
    user_box.pack()
    submit_button.pack()
    yes_button.pack_forget()
    no_button.pack_forget()
    greeting_text.pack_forget()

window = tkinter.Tk()
window.title("🔮 Guess it all ")
window.geometry("500x450")

instruction_text = tkinter.Label(window, text="Enter your name : ")
instruction_text.pack()

user_box = tkinter.Entry(window)
user_box.pack()

submit_button = tkinter.Button(window, text="Submit", command=get_name)
submit_button.pack()

yes_button = tkinter.Button(window, text="Yes", command=continue_code)
no_button = tkinter.Button(window, text="No", command=ask_name_again)

greeting_text = tkinter.Label(window)

window.mainloop()
