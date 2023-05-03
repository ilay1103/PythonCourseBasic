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
	if len(letter_guessed)>1 or not letter_guessed.isalpha() \
	or letter_guessed in old_letters_guessed:
		return False
	else:
		return True


def main():
	help(check_valid_input)
	old_letters  = []
	character_guessed=input("Guess a letter: ")
	print(check_valid_input(character_guessed, old_letters ))
	old_letters .append(character_guessed)
	
if __name__ == "__main__":
	main()