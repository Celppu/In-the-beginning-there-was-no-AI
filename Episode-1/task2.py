#Find python file in the episode folder. Run the file and see what happens. Try to change the code and see what happens.
#Read the code and try to understand what it does.
#Comments in the code are marked with #. Comments are ignored by the computer when it runs the code.


# Function for addition
def add(x, y):
    """
    Adds two numbers x and y.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The sum of x and y
    """
    return x + y

# Function for subtraction
def subtract(x, y):
    """
    Subtracts y from x.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The difference of x and y
    """
    return x - y

# TODO: Function for multiplication - to be completed by the student
def multiply(x, y):
    """
    Multiplies two numbers x and y.
    
    TODO: Implement this function to return the product of x and y.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The product of x and y
    """
    # Your code here
    pass

# Function for division
def divide(x, y):
    """
    Divides x by y.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float or str: The quotient of x and y, or 'undefined' if y is 0
    """
    if y == 0:
        return "undefined"
    else:
        return x / y

# Main loop to ask for user input
while True:
    # Ask for the operation to be performed
    operation = input("Enter operation (add, subtract, multiply, divide) or 'quit' to exit: ").lower()

    # Exit condition
    if operation == 'quit':
        print("Calculator exiting. Goodbye!")
        break

    # Ask for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation
    if operation == 'add':
        print("Result:", add(num1, num2))
    elif operation == 'subtract':
        print("Result:", subtract(num1, num2))
    elif operation == 'multiply':
        print("Result:", multiply(num1, num2)) # This will not work until the function is implemented
    elif operation == 'divide':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation.")
