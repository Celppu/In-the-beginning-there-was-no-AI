# Author: Emil Lintunen
# Date: 26-11-2023
# This Python function is designed to check if a specific user is mentioned in a comment.
# A 'mention' is identified as a word in the comment that starts with '@' followed by the user's name.
# Students are tasked to complete the function by following the instructions in the comments.

def is_user_mentioned(comment, user):
    """
    Checks if a user is mentioned in a comment.
    
    Parameters:
    comment (str): The comment text to search through.
    user (str): The username to look for in the comment.

    Returns:
    bool: True if the user is mentioned in the comment, False otherwise.
    """
    
    # TODO: Split the comment into words using the split() method and store it in a variable named 'words'
    # Hint: Use the .split() method on the comment string

    # TODO: Write a loop to iterate through each word in the 'words' list
    # Hint: Use a 'for' loop, for example, 'for word in words:'

    # Inside the loop:
        # TODO: Check if the word starts with '@'
        # Hint: Use the .startswith() method on the word

        # TODO: If the word starts with '@', check if the rest of the word matches the 'user' parameter
        # Hint: Use slicing [1:] to get the part of the word after '@'

        # TODO: If a match is found, return True

    # TODO: If no match is found in the entire loop, return False
    # Hint: This return statement should be outside of the loop

# Example comments for testing
comment1 = "Hey @Alice, did you finish your homework?"
comment2 = "Good job on the project, @Bob!"
comment3 = "I think @Charlie will know the answer to this question."
comment4 = "Does anyone want to join my study group?"

# Example test cases - students can uncomment and run these once they complete the function
# print(is_user_mentioned(comment1, "Alice"))  # Expected output: True
# print(is_user_mentioned(comment2, "Alice"))  # Expected output: False
# print(is_user_mentioned(comment3, "Charlie")) # Expected output: True
# print(is_user_mentioned(comment4, "David"))   # Expected output: False
