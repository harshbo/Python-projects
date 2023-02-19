import random
import colorama
colorama.init()
name = input("Enter your name: ")
print("let's GO!!"+name)
l=["laptop","plumber","electricity","instagram","facebook","transistor","computer","multiplication"]
word=random.choice(l)
print(colorama.Fore.WHITE+"length of the word is : ",len(word))
tries=len(word)-1
display = '_'*len(word)
game_over=False
print(colorama.Fore.YELLOW+"*********************WORD GUESSING GAME ***************************")
while not game_over:
	print("You have " +str(tries)+ " reamining chances to guess the word")
	print(colorama.Fore.BLUE+display)
	print(colorama.Fore.CYAN+"-----------------------------------------")
	guess =input(colorama.Fore.WHITE+"Please guess a letter: ")
	i=0
	if guess in word:
		while word.find(guess,i)!= -1:
			i = word.find(guess,i)
			display = display[:i]+guess+display[i+1:]
			i+=1
		print(colorama.Fore.LIGHTGREEN_EX+"Correct guess!")
	else:
		print(colorama.Fore.LIGHTRED_EX+"sorry,wrong guess")
		tries -= 1
	if word == display:
		print("Word is : "+word.upper())
		print(colorama.Fore.MAGENTA+"Congratulations "+name)
		print(colorama.Fore.WHITE+"No of chances ",tries,"remained")
		print(colorama.Fore.LIGHTGREEN_EX+"You win!!")
		game_over = True
	if tries == 0:
		print(colorama.Fore.LIGHTRED_EX+"Sorry, you are out of attempts! \nTry next time! "+name)
		game_over=True