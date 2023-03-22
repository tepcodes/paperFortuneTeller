import random
import tkinter as tk


print("some text")
print("name")

def check_number(number):
    # Fibonacci sequence check
    a, b = 0, 1
    while b < int(number):
        a, b = b, a + b
    if b == int(number):
        return "it will be PERFECT!"

    # Prime number check
    for i in range(2, int(number)):
        if int(number) % i == 0:
            break
    else:
        return "it will be BOUNTIFUL!"

    # Divisible by 7 check
    if int(number) % 7 == 0:
        return "it will be AWESOME!"

    # Divisible by 3 check
    if int(number) % 3 == 0:
        return "it will be GREAT!"

    # Divisible by 2 check
    if int(number) % 2 == 0:
        return "it will be COOL!"

    # Contains 0 check
    if "0" in str(number):
        return "it will be LUCKY!"

    # Default case
    return "it will be SUFFERING!"


def button_click():
    color = color_var.get()
    number = number_entry.get()

    while color not in ['green', 'blue', 'yellow', 'red']:
        result_label.config(text='Invalid input. Please choose from the four colors.')
        return

    if color == 'green':
        result = "In CAREER"
    elif color == 'blue':
        result = "In LOVE"
    elif color == 'yellow':
        result = "In HEALTH"
    elif color == 'red':
        result = "In HAPPINESS"

    if not number.isdigit() or int(number) not in range(0, 101):
        result_label.config(text='Invalid input. Please choose a number from 0 to 100.')
        return

    result += '\n' + check_number(number)
    result_label.config(text=result)


# Create the GUI
root = tk.Tk()
root.title('Fortune Teller')

# Create the color selection dropdown
color_label = tk.Label(root, text='Choose a COLOR:')
color_label.pack()

color_var = tk.StringVar(root)
color_var.set('green')

color_option = tk.OptionMenu(root, color_var, 'green', 'blue', 'yellow', 'red')
color_option.pack()

# Create the number input field and submit button
number_label = tk.Label(root, text='Choose a NUMBER:')
number_label.pack()

number_entry = tk.Entry(root)
number_entry.pack()

submit_button = tk.Button(root, text='Submit', command=button_click)
submit_button.pack()

# Create the result label
result_label = tk.Label(root, text='Welcome to the Fortune Teller!\nI will tell you what the future holds for you!')
result_label.pack()

root.mainloop()
