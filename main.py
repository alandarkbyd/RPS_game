import random
Choices = ["rock", "papper", "scissor"]
compChoice = random.choice(Choices)
print("Welcome to the rps game!")
print("Enter your choice as (rock or papper or scissor)")
user_inp = input("Enter your choice: ").lower()

def letsCheck():
	global user_inp
	run = True

	while run:
		if user_inp == compChoice:
			print('It\'s a tie')
			run = False
	
		elif user_inp == "papper" and compChoice == "rock":
			print('The user wins')
			run = False
		
		elif user_inp == "papper" and compChoice == "scissor":
			print("You lose")
			run = False
	
		elif user_inp == "scissor" and compChoice == "rock":
			print("You lose")
			run = False

		elif user_inp == "scissor" and compChoice == "papper":
			print("The user wins")
			run = False
		
		elif user_inp == "rock" and compChoice == "scissor":
			print("The user wins")
			run = False

		elif user_inp == "rock" and compChoice == "papper":
			print("You lose")
			run = False
		
		else:
			print("Invalid choice!")
			user_inp = input("Enter your choice: ").lower()
		
	print(f"The computer took \"{compChoice}\"")

letsCheck()
