# This program simulates a magic 8 ball

"""
There will be 20 responses.
There will be 10 positive answers, 5 negative answers and 5 vague responses.
"""
from random import choice
from time import sleep

print("Hi, this program will help you make decisions depending on what you ask. \n")
print("Type your question or just think about the question in your head or speak it loud.")

input("Enter your question or press enter if you thought or spoke it out loud. \n>>")
print("Please wait...")
sleep(1)

answers = ["It is certain", "It is decidedly so.", "With a doubt.", "Yes definitely.", "You may rely on it.",
           "As I see it, yes", "Most likely.", "Outlook good.", "Yes", "Signs point to yes.", "Reply hazy, try again.",
           "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."
           "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print(choice(answers))