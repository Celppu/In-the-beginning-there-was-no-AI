# Author Emil Lintunen 2023
# Version: 1.0

# In this task we will learn to use llama cpp python
# bindings to create a simple llm interfence demo.
# You will learn the efects of stop words, history and
# other llm parameters.

# First we will import the llm python bindings

import argparse
from llama_cpp import Llama

# Initialize argument parser and define default model path
parser = argparse.ArgumentParser()
# Change model path to your own model
wsllocation = "C:/Users/valtionrautatiet/Downloads/airoboros-m-7b-3.0.Q4_K_M.gguf"
parser.add_argument("-m", "--model", type=str, default=wsllocation)
args = parser.parse_args()

# Load the model with a specified context window size
llm = Llama(model_path=args.model, n_ctx=1000)

# Initialize chat history
history = "System: \n This is a chat between curious people \n"

# Example prompt to the model would look like : 
# "System: 
#  This is a chat between curious people 
#  Joe: {Your prompt here}
#  Samantha: " And llm will continue the conversation from there
# untill the max_tokens is reached or the model outputs a stop token


# Chat loop to interact with the user
while True:
    userin = input("You: ")
    history += "Joe: \n" + userin + "\nSamantha: \n"
    print(history)

    # Generate a response using the model
    stream = llm(history,
                max_tokens=400,  # Max tokens to generate
                temperature=0.2, # add randomness to the model output
                stream=True,     # Stream output as it is generated
                #stop=["Joe:", "Samantha:"] # Stop tokens. 
                # If you want to stop generation uncomment that line
                )
    
    # Print model output with random colors for each token
    colors = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m",
              "\033[0;35m", "\033[0;36m", "\033[0;37m"]
    color_index = 0

    for output in stream:
        token_str = output["choices"][0]["text"]
        print(colors[color_index % len(colors)] + token_str + "\033[0m", end="")
        color_index += 1
        # Add token to history string
        history += token_str
    print("\n")
