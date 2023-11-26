[← Back to Main README](../README.md)

# Episode 1: Introduction to the course

Welcome to the first episode of the course. In this episode, we will introduce the course and the instructor. We will also discuss the course structure and the tools we will use throughout the course.

(In classroom. Introduction. Favorite AI in game or movie etc.)

## Structure of the lesson

Lessons try to follow the following structure:

1. Boring talk
2. Individual work
3. Discussion
4. Break (moving outside of the classroom or video)
5. repeat

Idea is to keep the lessons interactive and interesting. Also human brain can only concentrate for 20 minutes at a time. We will try to make short bursts of focusing on the coding and then some brakes where you can relax and discuss with your peers. Or watch a video. Or stretch your legs.

Pomodoro technique is something you can look up if you want to know more about this kind of learning.

## Today's lesson

1. Material
2. Learning goals
3. Installing python
(Independent work. Video on screen)
4. Coding python examples
5. Debugging
(Independent work. Video on screen)
6. LLM tools
7. Prompt engineering and manipulating AI
(Prompting)


Also we will start with

1. Python
2. Debugging
3. Going through different AI tools
4. Form study groups

## Structure of the course

Course is divided into episodes. Episodes can be one lesson or two lessons depending on the pace of the class. Each episode has a README file that contains the material for the episode. Each episode also has a homework that you should do before the next episode. Homework is not mandatory, but you will not get the most out of the course if you do not do the homework. Homework is also not graded.

I will test your knowledge in the class with small quizzes. These quizzes are not graded and you can not fail them. They are just to test your knowledge and to help you to understand the material. Also I will check you groups homework checklist to see the actual pace of the class. This will be used to adjust the pace of the course.

Topics we will cover in order:

1. Introduction to the course and Python
2. Debugging
3. Coding python examples
4. Neural networks in theory
5. Available llm tools
6. Prompt engineering and manipulating AI
7. Installing and using LLama AI
8. Using LLama AI examples
9. Building on top of LLama AI. Also learning to read documentation.
10. Filler episodes: Linux. Learning to use wsl and bash. Learning to use gpu on you own computer to accelerate inference.
11. API and web services. Learning to use discord API
12. Building simple discord bot



# Installing Python

Python
https://www.youtube.com/watch?v=6i3e-j3wSf0

Python is a programming language. It is used in many different fields. It is easy to learn and it is very popular. It is also very easy to install and use. Python is also very popular in AI and machine learning.

Example of python code for a simple hello world program:

```python
print("Hello world")
```
Hello world is a simple program that just prints out the text "Hello world" to the console. This is the first program that many people write when they learn a new programming language. It is a tradition in the programming world.

Next example prints out christmas tree out of asterisks.

```python
print("   *")
print("  ***")
print(" *****")
print("*******")
print("   *")
```

And next one uses loops to print out the same christmas tree.

```python
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))
print("   *")
```

Use debugger to go through the code line by line. Also try to change the code and see what happens.

# Code exercises

## Exercise 1
Find python file in the episode folder. Run the file and see what happens. Try to change the code and see what happens.
Read the code and try to understand what it does.
Comments in the code are marked with #. Try to understand what the comments mean.

## Exercise 2
Write a program that prints out a square of asterisks. Size of the square should be given as a parameter to the program.
Read comments

## Exercise 3
In this exercise will learn to finde keywords from text. Example use case would be a bot that only answers if it is mentioned in the message. This is a very simple example, but it is a good starting point for more complex bots.

[mentionfinder.py](./mentionfinder.py)

## Exercise 4
Check next section andtest all listed tools. Try to understand where they excel and where they fail. Test them all with same prompt and see what happens.


# LLM tools
In this course we will learn to use all LLM tools available. Prompting questions is most important skill after the googling.

Different tools use different models. Models are trained with different datasets. Models are also trained with different parameters. This means that different models have different strengths and weaknesses. You should try different models and see which one works best for you.

- Chat GPT Most advanced at the moment. Free version is older GPT 3.5
- Bing ai Note that this is very light and dumb ai
- Bard ai Not as dumb
- Copilot - Must have. Recommended extension to vscode. Student license available. Example of use in class.

Debugger
https://www.youtube.com/watch?v=oCcTiRGPogQ

Neural
https://www.youtube.com/watch?v=aircAruvnKk
