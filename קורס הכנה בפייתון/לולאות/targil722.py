def numbers_letters_count(my_str):
	'''Returns all members in the list which are greater than n.
	   :param my_list: The string we check.
	   :type my_list: str.
	   :return: List containg the amount of numbers in the string([0]) 
	   and the amount of other characters in the string([1]).
	   :rtype: list.
	   '''
	info_list=[0,0]
	for c in my_str:
		if c.isdecimal():
			info_list[0] += 1
		else:
			info_list[1] += 1
	return info_list


def main():
	help(numbers_letters_count)
	print(numbers_letters_count("Python 3.6.3"))
	
if __name__ == "__main__":
	main()