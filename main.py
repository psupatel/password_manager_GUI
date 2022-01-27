from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(symbols) for chat in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    record = f"{web} | {email} | {password}\n"

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Warning", message = "No fields can be left empty")
    else:
        is_okay = messagebox.askokcancel(message = f"These are the details entered:\n"
                                                  f"\n Website: {web}\n"
                                                  f"Email: {email} \n"
                                                  f"Password: {password} \n"
                                                  f"\nIs it okay to save?")
        if is_okay:
            with open("data.txt", mode="a") as my_file:
                my_file.write(record)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady= 50)

# Lock Image
canvas = Canvas(width = 200, height = 200)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column = 1, row = 0)

# Show labels in column 0
website_label = Label(text="Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text="Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text="Password:")
password_label.grid(column = 0, row = 3)

# Show entry boxes and buttons in column 1
website_entry = Entry()
website_entry.focus()
website_entry.grid(column = 1, row = 1, columnspan=2, sticky="EW")


email_entry = Entry()
email_entry.insert(0, "psupatel@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan=2, sticky="EW")


password_entry = Entry()
password_entry.grid(column = 1, row = 3, sticky="EW")


# Generate password button
password_button = Button(text = "Generate Password", command = generate_password)
password_button.grid(column = 2, row = 3, sticky="EW")


# Add button
add_button = Button(text = "Add", width=36, command = add_password)
add_button.grid(column = 1, row = 4, columnspan=2, sticky="EW")

window.mainloop()
