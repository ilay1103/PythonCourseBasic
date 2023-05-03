def longest(my_list):
	'''This function gets a list of strings returns the longest value in it.
	   :param my_list: The list we would like check.
	   :type my_list: list.
	   :return: The longest string in the list.
	   :rtype: str.
	   '''
	my_list = sorted(my_list, key = len)
	return my_list[-1]


def main():
	help(longest)
	list1 = ["111", "234", "2000", "goru", "birthday", "09"]
	print(longest(list1))
	
if __name__ == "__main__":
	main()