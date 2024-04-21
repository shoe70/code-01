#!/usr/bin/env python3

from time import sleep
import random
import sys

i = 1
end = False
conversation = []

# Cosmetics...
def scrollTxt(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		sleep(0.03)

# Generate Shakespearean response and return a string.
def generate_response():
	# Generate sentence starters...
	with open("Data/sentence_starters.txt", "r") as file:
		lines = [line.strip().replace("\"", "").replace("...", "") for line in file.readlines()]
		random_start = random.choice(lines)
	# Generate sentence enders...
	with open("Data/sentence_enders.txt", "r") as file:
		lines = [line.strip().replace("...", "") for line in file.readlines()]
		random_end = random.choice(lines)
		
	return random_start + " " + random_end

# Talk with Shakespeare!
while not end:
	value = input(f"[{i}]: ")
	if value.lower() == "end":
		end = True
	else:
		if len(value) >= 100:
			scrollTxt("Shakespeare is thinking...\n")
			sleep(2)
		# Append the User's input and Shakespeare's response to a list for later use.
		response = generate_response()
		conversation.append(f"User: {value}")
		conversation.append(f"Shakespeare: {response}")
		scrollTxt(f"[{i + 1}]: {response}\n")
	i += 2

# Save the conversation (list) to a .txt file
save_conversation = input("Would you like your conversation saved? Y/n : ")
if save_conversation.lower() == "y" or save_conversation.lower() == "yes":
	with open("conversation.txt", "w") as file:
		for item in conversation:
			file.write(item + "\n")
	print("Your conversation has been saved in /conversation.txt")