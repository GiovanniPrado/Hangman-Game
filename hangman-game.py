from random import randint
from termcolor import colored

def print_hangman(errors):
	if errors == 0:
		print(''' ______
 |     |
 |     
 |    
 |     
 |    
_|_   ''')
	if errors == 1:
		print(''' ______
 |     |
 |     O
 |    
 |    
 |    
_|_   ''')
	if errors == 2:
		print(''' ______
 |     |
 |     O
 |     |
 |     |
 |    
_|_   ''')
	if errors == 3:
		print(''' ______
 |     |
 |     O
 |    /|
 |     |
 |    
_|_   ''')
	if errors == 4:
		print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    
_|_   ''')
	if errors == 5:
		print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    /
_|_   ''')
	if errors == 6:
		print(''' ______
 |     |
 |     O
 |    /|\\
 |     |
 |    / \\
_|_   ''')

def pick_word():
	words = ["Cereal","Classe","Submergir","Holanda","Aplauso","Transporte","Nuclear","Kilos","Homens","Eclipse"]
	chosen_word = words[randint(0, len(words)-1)]
	return chosen_word

def print_word(word):
	unknown_word = []

def print_tries(letters, word):
	print('Tries: ',end='')
	for letter in letters:
		if letter in word:
			print(colored(letter, 'green'), end = ' ')
		else:
			print(colored(letter, 'red'), end = ' ')
	print()

def handle_in_game_input(input, previous_attempts):
	if len(input) > 1:
		print(colored('Type only one letter', 'yellow'))
		return "error"
	if input in previous_attempts:
		print(colored('You already tried that! Try a different letter.', 'yellow'))
		return "error"
	if not input.isalpha():
		print(colored('Type letters only', 'yellow'))
		return "error" 

errors = 0
word = pick_word()
hidden_word = "_"*len(word)
letters_tried = []
letter = ""
choice = 0
while True:
	print('Welcome to the Hangman Game! What do you want to do?')
	print('1- Play')
	print('2- Quit')
	while choice not in [1,2]:
		try:
			choice = int(input('>>'))
			if choice not in [1,2]:
				print(colored('Type a valid option.', 'yellow'))
		except:
			print(colored('Type a valid option.', 'yellow'))
	if choice == 2:
		exit()
	print('-'*40)
	while errors <= 6:
		print_hangman(errors)
		for position in hidden_word:
			print(position + " ", end="")
		print("\n")
		print_tries(letters_tried, word)
		letter = input('Guess a letter: ')
		print('-'*40)
		if handle_in_game_input(letter, letters_tried) == "error":
			continue
		letters_tried.append(letter)
		
