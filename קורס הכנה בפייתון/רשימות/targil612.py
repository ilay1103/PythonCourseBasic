def shift_left(my_list):
	'''This function gets a list with three members in it.
	The function shifts every member one place right in rotation.
	   :param my_list: The list we would like to shift.
	   :type my_list: list.
	   :return: The new list.
	   :rtype: list.
	   '''
	my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2], my_list[0]
	return my_list


def main():
	help(shift_left)
	print(shift_left([0, 1, 2]))
	print(shift_left(['monkey', 2.0, 1]))
	
if __name__ == "__main__":
	main()