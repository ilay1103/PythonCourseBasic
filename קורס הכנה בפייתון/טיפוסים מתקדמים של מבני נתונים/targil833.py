def count_chars(my_str):
	'''Count the apearances of each letter.
	   :param my_str: The string we check.
	   :type my_str: str.
	   :return: dictionary of the apearances of each letter.
	   :rtype: dict.
	   '''
	letter_dict = {}
	my_str = my_str.replace(' ','')
	for letter in my_str:
		if letter in letter_dict.keys():
			letter_dict[letter] += 1
		else:
			letter_dict[letter] = 1
	return letter_dict
	

def main():
	magic_str = "abra cadabra"	
	print(count_chars(magic_str))
	
if __name__ == "__main__":
	main()