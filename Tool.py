import pyfiglet

# Create ASCII art text
ascii_art = pyfiglet.figlet_format("first tool")
print(ascii_art)

class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"Tool Name: {self.name}")
        print(f"Description: {self.description}")

# Example usage of the Tool class
book = Tool("Calculator Tool", "Hey, my name is Touhid. This is my first project. I made a calculator, please try it!")
book.display()

# User interaction
nu = input('Please enter your name: ')
print(f'Hey, {nu}')

# Display introduction
b = '''I am a designer & engineer.
I created a calculator for you. Please try it now.'''
print(b)

# Simple calculator
x = input('Enter your first number: ')
y = input('Enter your second number: ')
print("This is your number result:")
print(int(x) + int(y))
