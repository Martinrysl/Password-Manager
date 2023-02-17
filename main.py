from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)
    #Copy Password to paperclip
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    data = open('data.txt', 'a')
    web = input_web.get()
    email = input_user.get()
    password = input_pass.get()
    new_data = {
            web: {
                "email": email,
                "password": password,
            }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Don't leave any field empty mtf")
    else:
        try:
            with open('data.json', 'r') as data:
                load = json.load(data)

        except FileNotFoundError:
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            load.update(new_data)

            with open('data.json', 'w') as data:
                json.dump(load, data, indent=4)

        finally:
            input_web.delete(0, END)
            input_pass.delete(0, END)
            input_web.focus()


def find_password():
    web = input_web.get()
    try:
        with open('data.json') as data_file:
            load = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message='No data file found')
    else:
        if web in load:
            emaill = load[web]['email']
            passw = load[web]['password']
            messagebox.showinfo(title=web, message=f'Email: {emaill}\nPassword: {passw}')
        else:
            messagebox.showinfo(title="Error", message=f'No details for {web} exists.')



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_web = Label(text='Website:')
label_user = Label(text='Email/Username:')
label_pass = Label(text='Password:')

label_web.grid(row=1, column=0)
label_user.grid(row=2, column=0)
label_pass.grid(row=3, column=0)

input_web = Entry(width=21)
input_web.focus()
input_user = Entry(width=21)
input_user.insert(0, 'martinrysl@gmail.com')
input_pass = Entry(width=21)

input_web.grid(row=1, column=1)
input_user.grid(row=2, column=1)
input_pass.grid(row=3, column=1)

button_pass = Button(text='Generate Password', command=generate_pass)
button_add = Button(text='Add', width=36, command=save)
button_search = Button(text='Search', command=find_password)
button_pass.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2)
button_search.grid(row=1, column=2)

window.mainloop()
