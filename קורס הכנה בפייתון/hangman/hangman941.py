def choose_word(file_path, index):
	'''Takes a word at the index from the file.
	   :param file_path: The file with 
	   :type file_path: str.
	   :param index: The index of the word we want to get. Starts from 1. Goes in cycle.
	   :type index: str.
	   :return: A tuple of the amount of different words and the chosen word.
	   :rtype: tuple.
	   '''
	open_file = open(file_path, 'r')
	words = open_file.read()
	words_list = words.split(' ')
	different_words = []
	for word in words_list:
		if word not in different_words:
			different_words.append(word)
	open_file.close()
	return len(different_words), words_list[(index - 1) % len(words_list)]
	

def main():
	print(choose_word("words.txt", 3))
	print(choose_word("words.txt", 15))
	
if __name__ == "__main__":
	main()