# Importing required functions from the replit module
from replit import clear
# Importing the logo for the calculator
from art import logo

# Function definitions for basic arithmetic operations

def add(n1, n2):
  return n1 + n2  # Returns the sum of two numbers

def subtract(n1, n2):
  return n1 - n2  # Returns the difference between two numbers

def multiply(n1, n2):
  return n1 * n2  # Returns the product of two numbers

def divide(n1, n2):
  return n1 / n2  # Returns the division of two numbers

# A dictionary mapping operation symbols to their respective functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Calculator function to interact with the user
def calculator():
  print(logo)  # Print the calculator logo

  # Asking the user for the first number
  num1 = float(input("What's the first number?: "))

  # Display available operations to the user
  for symbol in operations:
    print(symbol)

  should_continue = True  # Variable to control the continuation of the calculation process

  # Loop to perform the calculation
  while should_continue:
    # Asking the user to pick an operation
    operation_symbol = input("Pick an operation: ")
    
    # Asking for the second number
    num2 = float(input("What's the next number?: "))
    
    # Calling the corresponding function based on the chosen operation
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    # Printing the result of the calculation
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Asking if the user wants to continue with the result of the current calculation
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer  # If 'y', continue calculating with the new result
    else:
      should_continue = False  # If 'n', stop the current calculation
      clear()  # Clear the screen for a fresh start
      calculator()  # Start a new calculation session

# Call the calculator function to start the program
calculator()
