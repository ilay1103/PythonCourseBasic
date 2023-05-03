def choose_word(file_path, index):
	'''Takes a word at the index from the file.
	   :param file_path: The file with all the words.
	   :type file_path: str.
	   :param index: The index of the word we want to get. Starts from 1. Goes in cycle.
	   :type index: str.
	   :return: The chosen word.
	   :rtype: str.
	   '''
	opened = False
	while not opened:
		try:
			open_file = open(file_path, 'r')
			opened = True
		except IOError:
			#If the file doesn't exist, write a different one.
			file_path = input("Wrong file was written.\nTry to write a new path: ")
	words = open_file.read()
	words_list = words.split(' ')
	different_words = []
	for word in words_list:
		if word not in different_words:
			different_words.append(word)
	open_file.close()
	return words_list[(index - 1) % len(words_list)]
	
def print_hangman(num_of_tries):
	'''Prints the photo of the hangman based on the num of tries.
	   :param num_of_tries: The amount of tries failed.
	   :type num_of_tries: int.
	   :return: None.
	   :rtype: None.
	   '''
	HANGMAN_PHOTOS = {}
	HANGMAN_PHOTOS[0] = """
	picture 1:
		x-------x
	"""
	HANGMAN_PHOTOS[1] = """
	picture 2:
		x-------x
		|
		|
		|
		|
		|
	"""
	HANGMAN_PHOTOS[2] = """
	picture 3:
		x-------x
		|       |
		|       0
		|
		|
		|
	"""
	HANGMAN_PHOTOS[3] = """
	picture 4:
		x-------x
		|       |
		|       0
		|       |
		|
		|
	"""
	HANGMAN_PHOTOS[4] = """
	picture 5:
		x-------x
		|       |
		|       0
		|      /|\\
		|
		|
	"""
	
	HANGMAN_PHOTOS[5] = """
	picture 6:
		x-------x
		|       |
		|       0
		|      /|\\
		|      / 
		|
	"""
	
	HANGMAN_PHOTOS[6] = """
	picture 7:
		x-------x
		|       |
		|       0
		|      /|\\
		|      / \\
		|
	"""
	print(HANGMAN_PHOTOS[num_of_tries])
	
def check_win(secret_word, old_letters_guessed):
    '''Check if all the letters in the secret word were guessed.
       :param secret_word: The word we must guess.
       :type secret_word: str.
       :param old_letters_guessed: List of the letters guessed.
       :type old_letters_guessed: list.
       :return: If the secret word has all the letters in the list.
       :rtype: bool.
       '''
    win = True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            win = False
    return win

def show_hidden_word(secret_word, old_letters_guessed):
    '''Shows the correct letters guessed in the right spots of the secret string.
       :param secret_word: The word we must guess.
       :type secret_word: str.
       :param old_letters_guessed: List of the letters guessed.
       :type old_letters_guessed: list.
       :return: The string with the correct letters guessed.
       :rtype: str.
       '''
    current_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            current_word += letter
        else:
            current_word += '_'
    current_word = ' '.join(current_word)
    return current_word

def check_valid_input(letter_guessed, old_letters_guessed):
	'''This function gets a letter and a list of the letters which were 
	already guessed before. 
	The function returns if the letter guessed is valid.
	Letter can be valid if he is a single letter in the english alphabet
	and if it was not guessed already. 
	   :param letter_guessed: The letter we would like to check.
	   :type letter_guessed: str.
	   :param old_letters_guessed: The letters which were already guessed.
	   :type old_letters_guessed: list.
	   :return: If he is valid or not.
	   :rtype: bool.
	   '''
	if len(letter_guessed) > 1 or not letter_guessed.isalpha() \
	or letter_guessed in old_letters_guessed:
		return False
	else:
		return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	'''This function gets a letter and a list of the letters which were 
	already guessed before. 
	The function returns if the letter guessed is valid.
	If the letter is valid it will also add the letter to the list of the letters gussed.
	Letter can be valid if he is a single letter in the english alphabet
	and if it was not guessed already. 
	If the letter is invalid, The function will print X and the letters which were guessed.
	   :param letter_guessed: The letter we would like to check.
	   :type letter_guessed: str.
	   :param old_letters_guessed: The letters which were already guessed.
	   :type old_letters_guessed: list.
	   :return: If he is valid or not.
	   :rtype: bool.
	   '''
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed)
		return True
	else:
		print("X\n" + " -> ".join(sorted(old_letters_guessed)))
		return False
	
def print_header(max_tries = 6):
	HANGMAN_ASCII_ART = """
	Welcome to the game Hangman
			_    _                                         
			| |  | |                                        
			| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
			|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
			| |  | | (_| | | | | (_| | | | | | | (_| | | | |
			|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
								__/ |                      
								|___/"""
	
	print(HANGMAN_ASCII_ART, '\nAmount of tries:', max_tries)

def main():
	MAX_TRIES = 6
	old_letters_guessed = []
	num_of_tries = 0
	
	#1
	print_header(MAX_TRIES)
	
	#2
	file_path = input("Enter file path to the words file: ")
	index = int(input("Enter index of the word you want to guess: "))
	secret_word = choose_word(file_path, index)
	
	#3
	print_hangman(num_of_tries)
	
	#4
	print(show_hidden_word(secret_word, old_letters_guessed))
	
	while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
		#5
		letter_guessed = input("Guess a letter: ")
		while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
			letter_guessed = input("Guess another letter: ")
		
		
		#6
		print(show_hidden_word(secret_word, old_letters_guessed))
		if letter_guessed not in secret_word:
			num_of_tries += 1
			print("):")
			print_hangman(num_of_tries)
	
	#7
	if check_win(secret_word, old_letters_guessed):
		print("WIN")
	else:
		print("LOSE")
	
if __name__ == "__main__":
	main()