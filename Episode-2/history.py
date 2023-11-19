# Author Emil Lintunen 2023
# Version: 1.0

# In this task, we will learn to use llama cpp python
# bindings to create a simple LLM interfence demo.
# You will learn the effects of stop words, history, and
# other LLM parameters.

# In the code there is 2 tasks for you to complete.

import argparse
from llama_cpp import Llama

# Initialize argument parser and define default model path
parser = argparse.ArgumentParser()
wsllocation = "/home/celp/models/airoboros-m-7b-3.0.Q4_K_S.gguf"
parser.add_argument("-m", "--model", type=str, default=wsllocation)
args = parser.parse_args()

# Load the model with a specified context window size
llm = Llama(model_path=args.model, n_ctx=1000)

### Task 2: Initialize chat history tokens ###
# Function to manage prompt and history
def manage_prompt(tokenized_history, new_user_input):
    """
    Exercise: This function manages the conversation history and the latest user input.
    - Tokenize the new user input and extend the tokenized history.
    - Slice the tokenized history to include only the last 400 tokens.
    - Detokenize this slice to create the prompt string for the Llama model. Note also add .decode() to the end of the detokenize function.
    - Return the prompt string and the updated tokenized history.
    """
    # Tokenize the new user input
    # ? Hint: use llm.tokenize()

    # Extend the tokenized history with the new input tokens
    # ? Hint: use the extend() function

    # Slice the history to get the last 400 tokens
    # ? Hint: use the slicing operator [:]

    # Detokenize the prompt tokens to create a string
    # ? Hint: use llm.detokenize() and add .decode() to the end

    # Return the prompt string and the updated tokenized history

    return prompt_string, tokenized_history


# Initialize chat history tokens
history_tokens = []

# System message that is always added to the beginning of the prompt
SystemMessage = "System: \n This is a transcript of two people chatting. \n"

# Chat loop to interact with the user
while True:
    user_input = input("You: ")
    prompt, history_tokens = manage_prompt(history_tokens, "Joe: \n" + user_input + "\nSamantha: \n")

    ### TASK 1 Add system message to the beginning of the prompt ###

    # Generate a response using the model
    stream = llm(prompt, max_tokens=400, temperature=0.2, stream=True, stop=["Joe:"])
    
    # Print model output with random colors for each token
    colors = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m",
              "\033[0;35m", "\033[0;36m", "\033[0;37m"]
    color_index = 0

    for output in stream:
        token_str = output["choices"][0]["text"]
        print(colors[color_index % len(colors)] + token_str + "\033[0m", end="")
        color_index += 1
        history_tokens.extend(llm.tokenize(token_str.encode()))
    print("\n")
