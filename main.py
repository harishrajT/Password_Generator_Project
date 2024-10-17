#Password Generator Project
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os


#-----------------password generator-------------------------#
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)

  password = "".join(password_list)
  password_Entry.insert(0, password)

  pyperclip.copy(password)


#------------------------------save password------------------------#
def save_password():

  website = website_Entry.get()
  email = email_username_Entry.get()
  password = password_Entry.get()

  if len(website)==0 or len(email)==0 or len(password) == 0:
    messagebox.showinfo(title="Error", message="input can not be empty")

  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the the details entered: \nEmail :{email}" 
                           f"\nPassword : {password} \nIs it ok to save? ")

    if is_ok:
      with open("data.txt", mode="a") as data:
        data.write(f"{website} | {email} | {password}\n")
        website_Entry.delete(0, END)
        password_Entry.delete(0, END)



#---------------------Get Last Used Email----------------------------#
previous_email = "" # Temporary mail
def last_mail():
  if os.path.exists("data.txt"):
    with open("data.txt", mode="rb") as data:
      data.seek(-2, 2)  # Move to the second last byte of the data
      while data.read(1) != b'\n':  # Move backwards until you find a newline character
        data.seek(-2, 1)
      last_line = data.readline().decode()
      start = last_line.find('|') + 1  # Find the index of the first | and move one step forward
      end = last_line.find('|', start)  # Find the index of the next | after start
      previous_email = last_line[start:end].strip()
      if previous_email == "":
        return ""

  else:
    return ""


# ------------------------------UI Setup-----------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_png)
canvas.grid(row=0, column=1)


website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)

email_username_label = Label(text = "Email/Username : ")
email_username_label.grid(row = 2, column=0)

password_label = Label(text="Password : ")
password_label.grid(row = 3, column=0, )

website_Entry = Entry(width=52)
website_Entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_Entry.focus()

email_username_Entry = Entry(width=52)
email_username_Entry.grid(row=2,column=1, columnspan=2, sticky='w')
email_username_Entry.insert(0, f"{last_mail()}")

password_Entry = Entry(width=32)
password_Entry.grid(row=3, column=1, sticky='w')

generate_button= Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_password_button = Button(text="Add", width=44, command=save_password)
add_password_button.grid(row=4, column =1, columnspan=2, sticky='w')



window.mainloop()