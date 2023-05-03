def is_valid_input(letter_guessed):
	'''This function gets a letter and returns if he is valid.
	letter can be valid if he is a single letter and a letter of
	the english alphabet.
	   :param letter_guessed: The letter we would like to check.
	   :type letter_guessed: str.
	   :return: If he is valid or not.
	   :rtype: bool.
	   '''
	if len(letter_guessed)>1 or not letter_guessed.isalpha():
		return False
	else:
		return True


def main():
	help(is_valid_input)
	character_guessed=input("Guess a letter: ")
	print(is_valid_input(character_guessed))
	
if __name__ == "__main__":
	main()