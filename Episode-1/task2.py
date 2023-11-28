#Write a program that prints out a square of asterisks. Size of the square should be given as a parameter to the program.
#Read comments

# print_square.py

def print_square(size):
    """
    Prints a square of asterisks.

    This function takes an integer 'size' and prints a square of asterisks,
    where each side of the square has 'size' number of asterisks.

    Parameters:
    size (int): The size of the square.

    Example:
    If size is 3, the output should be:
    ***
    ***
    ***

    TODO: Complete this function to print the square.
    """

    # TODO: Use a loop to print each line of the square.
    # Hint: You'll need a loop inside another loop (nested loop).
    # The outer loop should iterate 'size' times, once for each line.
    # The inner loop should also iterate 'size' times to print the asterisks in a line.
    # Use 'print("*", end="")' to print asterisks on the same line.
    # Use a simple 'print()' to move to the next line after printing each line of asterisks.

    # Your code here

# Ask the user for the size of the square
try:
    square_size = int(input("Enter the size of the square: "))
    print_square(square_size)
except ValueError:
    print("Please enter a valid integer for the size.")
