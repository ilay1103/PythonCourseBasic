
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
		|      / \\
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
	

def main():
	num_of_tries = 4
	print_hangman(num_of_tries)
	num_of_tries = 5
	print_hangman(num_of_tries)
	num_of_tries = 6
	print_hangman(num_of_tries)
	
if __name__ == "__main__":
	main()
