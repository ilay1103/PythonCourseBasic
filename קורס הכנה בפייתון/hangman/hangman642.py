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

def main():
	help(check_valid_input)
	help(try_update_letter_guessed)
	old_letters = ['a', 'p', 'c', 'f']
	character_guessed=input("Guess a letter: ")
	print(try_update_letter_guessed(character_guessed, old_letters ))
	print(old_letters)
	
	
if __name__ == "__main__":
	main()