def format_list(my_list):
	'''This function gets an evem list of strings and
	returns a string of the even members split by a comma.
	The last member needs to have the word 'and' before it.
	   :param my_list: The list we would like use.
	   :type my_list: list.
	   :return: The string with the even members.
	   :rtype: str.
	   '''
	even_my_list = my_list[::2]
	even_my_list.append("and " + my_list[-1]) 
	return ", ".join(even_my_list)


def main():
	help(format_list)
	my_list = ["hydrogen", "helium", "lithium", "beryllium", \
	"boron", "magnesium"]
	print(format_list(my_list))
	
if __name__ == "__main__":
	main()