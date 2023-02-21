import random
import colorama
colorama.init()
l=["rock","paper","scissors"]
user_wins=0
computer_wins=0
matches,total = 0,0
while True:
	r_number = random.randint(0,2)
	com_pick = l[r_number]
	print(colorama.Fore.WHITE+"Computer have already picked the choice")
	user_input = input(colorama.Fore.CYAN+"Enter your choice rock or paper or scissors or quit : ").lower()
	print(colorama.Fore.WHITE+"")

	if user_input == "quit" :
		print(colorama.Fore.YELLOW+"Game ended")
		break
	if user_input not in l:
		print(colorama.Fore.LIGHTRED_EX+"Check your input")
		continue

	print(colorama.Fore.YELLOW+"Computer Picked : "+com_pick)

	if user_input in l:
		if user_input == "rock" and com_pick =="scissors" :
			print(colorama.Fore.GREEN+"You won!!")
			user_wins +=1
			total+=1
		elif user_input == "paper" and com_pick =="rock" :
			print(colorama.Fore.GREEN+"You won!!")
			user_wins +=1
			total+=1 
		elif user_input == "scissors" and com_pick =="paper" :
			print(colorama.Fore.GREEN+"You won!!")
			user_wins +=1
			total+=1
		elif ((user_input == "scissors" and com_pick =="scissors" ) or (user_input == "paper" and com_pick =="paper" ) or (user_input == "rock" and com_pick =="rock" )):
			print(colorama.Fore.CYAN+"Tied up!!")
			matches +=1
			total+=1
		else:
			print(colorama.Fore.GREEN+"Computer won!!")
			computer_wins +=1
			total+=1


print( "Total matches: ",total)
print("-------------------------")
print(colorama.Fore.YELLOW+"Computer wins count: ",computer_wins,"\nYour wins count ",user_wins,"\nMatches tied up ",matches ) 
print( colorama.Fore.MAGENTA+"Good Bye!")
