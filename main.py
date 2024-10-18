#Password Generator Project
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import os
import json


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

  website = website_Entry.get().title()
  email = email_username_Entry.get().lower()
  password = password_Entry.get()
  new_data = {
    website : {
      "email": email,
      "password": password
    }
  }

  if len(website)==0 or len(email)==0 or len(password) == 0:
    messagebox.showinfo(title="Error", message="input can not be empty")

  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the the details entered: \nEmail :{email}" 
                           f"\nPassword : {password} \nIs it ok to save? ")

    if is_ok:
      try:
        with open("data.json", mode="r") as data:
          data_file = json.load(data)

      except FileNotFoundError:
        with open("data.json", "w") as data:
          json.dump(new_data, data, indent=4)

      else:
        data_file.update(new_data)

        with open("data.json", "w") as data:
          json.dump(data_file, data, indent=4)

      finally:
        website_Entry.delete(0, END)
        password_Entry.delete(0, END)



# --------------------Find Password---------------------------------#
def find_password():
  website = website_Entry.get().title()

  try:
    with open("data.json") as data:
      data_file = json.load(data)

  except FileNotFoundError:
      messagebox.showinfo(title="Error", message="No data file found")

  else:
      if website in data_file:
        email = data_file[website]["email"]
        password = data_file[website]["password"]
        messagebox.showinfo(title=website, message=f"Email:{email} \nPassword:{password}")
      else:
        messagebox.showinfo(title="Error", message=f"There is no website found named \"{website}\" ")



#---------------------Get Last Used Email----------------------------#
previous_email = ""  # Temporary email variable

def last_mail():
  if os.path.exists("data.json"):
    with open("data.json", mode="r") as file:
      data = json.load(file)

      if data:  # Check if the dictionary is not empty
        last_Entry = list(data.keys())[-1]
        last_entry_details = data[last_Entry]

        # Assuming 'email' is the key storing the email address in the service dictionary
        previous_email = last_entry_details.get('email', "").strip()

        return previous_email if previous_email else ""  # Return the email or empty string if not found

  return ""  # Return an empty string if file doesn't exist or no email is found


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

website_Entry = Entry(width=32)
website_Entry.grid(row=1, column=1, sticky='w')
website_Entry.focus()

email_username_Entry = Entry(width=52)
email_username_Entry.grid(row=2,column=1, columnspan=2, sticky='w')
email_username_Entry.insert(0, f"{last_mail()}")

password_Entry = Entry(width=32)
password_Entry.grid(row=3, column=1, sticky='w')

search_button = Button(text= "Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

generate_button= Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_password_button = Button(text="Add", width=44, command=save_password)
add_password_button.grid(row=4, column =1, columnspan=2, sticky='w')



window.mainloop()