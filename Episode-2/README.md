[← Back to Main README](../README.md)

# Episode 2: Installing Python Tools for Llama AI

Welcome to Episode 2! Here we'll install Python bindings for llama.cpp to begin our AI programming adventure, focusing on a CPU-based setup using WSL 2 for Windows users.

## Using WSL 2 (Recommended for Windows Users)

Setting up WSL 2 provides a Linux environment on Windows, facilitating development tasks. Follow these steps:

1. Ensure you have Windows 10, updated to version 2004, Build 19041, or higher.
2. Open PowerShell as Administrator and run: `wsl --install`
3. Set WSL 2 as your default version with: `wsl --set-default-version 2`
4. Install your preferred Linux distribution from the Microsoft Store.
5. Launch the Linux distribution and complete the initial setup including username and password.
6. Update the package list and install essential packages:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install python3 python3-pip build-essential cmake
   ```

For additional help with WSL 2, consult the [Microsoft WSL 2 Documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Installation from PyPI

With WSL 2 or native Linux:

```bash
pip install llama-cpp-python
```

Visit the [llama-cpp-python repository](https://github.com/abetlen/llama-cpp-python) for detailed instructions and troubleshooting.

## Additional Setup for Native Windows

If you're installing directly on Windows, you will need Visual Studio Build Tools and CMake:

1. [Download Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
2. [Get CMake](https://cmake.org/download/)

Then proceed with the `pip install llama-cpp-python` command.

## Working with the API

After installation, you can start using the llama API. Example usage can be found in the [High-level API section](https://github.com/abetlen/llama-cpp-python).

For further guidance and development details, the [llama-cpp-python documentation](https://abetlen.github.io/llama-cpp-python) is available.

# Projects and Exercises
## Task 0: Find the right model

Finding good model can be difficult task. There are many models available, but not all of them are good. Some of them are not trained well, some of them are trained on different data, some of them are trained on different language.

LLama does not understand finnish language. Also the prompt template can be different depending on training data and the version.

I can recommend this model for basic testing:
https://huggingface.co/TheBloke/airoboros-m-7B-3.0-GGUF
You need to select version that can fit into your RAM. Repository contains models with different bit depth. For example Q4_K_S . README.md contains information about the compression and bit depths + there is link to the original model. User TheBloke only converts the models to convienient format for us. LLama cpp uses GGUF format. Note ! GGUF has code in it, only use models from trusted sources.

## Task 1: Interactive Chat with Llama AI

[basicLLama.py](./basicLLama.py)

In Task 1 you'll dive into using the Llama AI through Python bindings. The objective is to create a simple interactive chat interface where you can send inputs to the AI and receive responses. You will learn about the effects of different parameters like 'max_tokens', 'temperature', and the use of 'stream' for generating responses.

The provided script sets up an interactive loop where you can converse with the model, and each response from Llama AI is printed in a random color to demonstrate the token-by-token generation of text. It's a fun way to visualize how the AI constructs its responses and how each token contributes to the overall message.

Be sure to read through the comments in the code to understand each part of the process, from initializing the model to generating and displaying the AI's responses.

Try these:
1. Change names of the agents
2. Brainwash new system message
3. Test infinite conversation without stop tokens
4. Download new model.
5. Read about the parameters loaded to the model (check comments)


## Task 2: Token history limit

### Creating an Interactive AI Chatbot

Creating chatbot that can handle long inputs and outputs is not easy task. In this task you will learn how to tokenize and limit history of the conversation. You will also learn how to use stop words to guide the AI's response generation.

If you input too long history to the model, error will be generated. This task is important step to make the chatbot more robust.

### Key Concepts:
1. **Managing Conversation History**: Understand how to maintain a rolling history of tokens to keep the conversation relevant and coherent.
2. **Using Stop Words**: Explore how stop words can guide the AI's response generation, marking natural ends of sentences or turns in conversation.

### Exercise:
- Complete the `manage_prompt` function:
  - **Tokenization**: Convert the new user input into tokens using `llm.tokenize()`.
  - **History Management**: Extend the tokenized history with the new input tokens, keeping only the last 400 tokens.
  - **Prompt Preparation**: Detokenize the last 400 tokens to create the string prompt for the Llama model, ensuring to decode the byte string.
- Modify the chat loop:
  - **System Message Integration**: Add a predefined system message at the beginning of each prompt to simulate a chat scenario.
  - **Dynamic Response Generation**: Use the Llama model to generate responses based on the prompt, and display them with random colors to indicate tokenization.

This task will deepen your understanding of how conversational AI models process and respond to text inputs. It's a hands-on way to explore the mechanics of AI-driven chatbots.

---

## Task 3: Multi Agent Conversation

To make the chatbot more interesting, we can add more agents to the conversation. In this task you will learn how to create multi agent conversation.

Copy the code from Task 2 and modify it to support multi agent conversation. You can use the code from Task 2 as a starting point.

### Key Concepts:
1. **Multi Agent Conversation**: Understand how to create multi agent conversation.
2. **Managing Conversation History**: Understand how to maintain a rolling history of tokens to keep the conversation relevant and coherent.
3. **Using Stop Words**: Explore how stop words can guide the AI's response generation, marking natural ends of sentences or turns in conversation.

### Exercise:
- Complete previous task
- Instead of using one agent, ask user to input who they are in this round of conversation and who ai will be answering for.
- Read about prompt format for the model you are using. You can find the information from the model repository. For example: https://huggingface.co/TheBloke/airoboros-m-7B-3.0-GGUF

### Testing
- Test the conversation with different agents. For example: You, AI, Bob, Alice, John, Jane, etc.
- Test if llm can remember who said what. Prompting is enough

## Task 4: Brainwash

Brainwashing is a technique that can be used to make the AI to say what you want. In this task you will learn how to use brainwashing to make the AI to say what you want.

### Key Concepts:
- System message
   - System message is a message that is added to the beginning of the prompt. It can be used to guide the AI's response generation. Test different system messages and see how they affect the AI's response generation.
- Prompt template
   - Think if you can guide the conversation by desiciding what the AI will say before you give it to llm. For example
      ```
      - User: Hello
      - AI: Arr! I am a pirate! -> and generation starts here.
      ```
 

## Task 5: TODO to do

TODO do todo

## License

The materials provided in this workshop are shared under the [MIT license](https://github.com/abetlen/llama-cpp-python).
```
Copy and paste the above content into your README file as needed.