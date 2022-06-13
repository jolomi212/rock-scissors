# import random module
import random

game  = ''


print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")
print("Are you ready to play? (Y/N)")
ready = input()
if ready == "Y" or ready == "y":
    game = True



options = ["R","P","S"]
if game == True:
	print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
	
	# take the input from user
	choice = (input("User turn: ")).upper()

	
	#loop till valid input
	while choice not in options:
		print("Invalid input, pick again")
		choice = (input("User turn: ")).upper()
		

	# initialize value of choice_name variable
	
	if choice == "R":
		choice_name = 'Rock'
	elif choice == "P":
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	# print user choice
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	# Computer chooses randomly 
	#  Using choice method of random module
	comp_choice = random.choice(options)
	
	
	
	if comp_choice == "R":
		comp_choice_name = 'Rock'
	elif comp_choice == "P":
		comp_choice_name = 'Paper'
	else:
		comp_choice_name = 'Scissor'


	#loop if it's a tie
	while comp_choice == choice:
		
		print("It's a tie, choose again.")
		print("Player(" + choice_name + ") : " + "CPU("+comp_choice_name +")")
		print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
	
	# take the input from user
		choice = (input("User turn: ")).upper()

		
		
		while choice not in options:
			print("Invalid input, pick again")
			choice = (input("User turn: ")).upper()
			

		# initialize value of choice_name variable
		
		if choice == "R":
			choice_name = 'Rock'
		elif choice == "P":
			choice_name = 'paper'
		else:
			choice_name = 'scissor'
			
		# print user choice
		print("user choice is: " + choice_name)
		print("\nNow its computer turn.......")

		
		comp_choice = random.choice(options)
		if choice == "R":
			choice_name = 'Rock'
		elif choice == "P":
			choice_name = 'paper'
		else:
			choice_name = 'scissor'
	

		
	print("Computer choice is: " + comp_choice_name)

	print("Player(" + choice_name + ") : " + "CPU("+comp_choice_name +")")
    

	# condition for winning
	if((choice == "R" and comp_choice == "P") or
	(choice == "P" and comp_choice =="R" )):
		
		result = "paper"
		
	elif((choice == "R" and comp_choice == "S") or
		(choice == "S" and comp_choice == "R")):
		
		result = "Rock"
	else:
		
		result = "scissor"

	# Printing either user or computer wins
	if result == choice_name:
		print("<== You Win!!! ==>")
	else:
		print("<== CPU wins ==>")
	
	

	print("\nThanks for playing")


else:
    print("Come back when you're ready. Haha")
	

print("Goodbye")