# this is python debugger exercise.
# Here we print variable size asterisk christmas tree

# Python Exercise: Print a Variable Size Asterisk Christmas Tree

def print_christmas_tree(size):
    """
    Function to print a Christmas tree made of asterisks.
    :param size: Integer representing the size of the tree.
    """
    for i in range(size):
        # Print each level of the tree
        # The number of asterisks increases by 2 each level, starting from 1
        # Center align the asterisks with respect to the width of the tree's base
        print((' ' * (size - i - 1)) + ('*' * (2 * i + 1)))

    # Print the trunk of the tree
    trunk_width = size // 2
    trunk_height = size // 4
    for _ in range(trunk_height):
        # Center align the trunk with respect to the width of the tree's base
        print((' ' * (size - trunk_width - 1)) + ('*' * (2 * trunk_width + 1)))

# Ask user for the size
size = int(input("Enter the size of the tree: "))
# Print the tree
print_christmas_tree(size)