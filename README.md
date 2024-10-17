
# Password Manager

## Project Overview
This is a simple **Password Manager** built using Python and Tkinter. It allows users to securely generate and store passwords for different websites or accounts. The app also provides a feature to automatically generate strong passwords for better security.

## Features
- User-friendly graphical interface using **Tkinter**.
- Secure password generation with a combination of letters, numbers, and symbols.
- Option to save website, email/username, and password entries.
- Password generation at the click of a button.
  
## Screenshots
![App Screenshot](screenshot.png)  <!-- Add your screenshot here if you have one -->

## Installation
### Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
  
### Steps
1. Clone the repository or download the project files.
2. Install the necessary dependencies (Tkinter is included by default with Python).
3. Run the `main.py` file using Python.

```bash
python main.py
```

## How It Works
1. Enter the website, email/username, and password (or use the "Generate Password" button to generate a secure password).
2. Click the "Add" button to save the information.
3. The generated password will include a mix of random letters, numbers, and special characters for enhanced security.

## Code Explanation

- The password generation logic uses the `random` module to select random characters from predefined lists of letters, numbers, and symbols.
- The graphical interface is built using **Tkinter**, with buttons, labels, and entry widgets arranged in a grid layout.

### Password Generation Code Snippet:
```python
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    return f"Your password is: {password}"
```

## Future Improvements
- Save passwords to a local file for persistence.
- Add a feature to retrieve and display saved passwords.
- Option to encrypt stored passwords for added security.
- Integrate search functionality to easily find credentials for a specific website.

## Contributing
Feel free to contribute by submitting a pull request or opening an issue.

