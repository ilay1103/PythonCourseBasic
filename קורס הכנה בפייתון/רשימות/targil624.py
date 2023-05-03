def extend_list_x(list_x, list_y):
	'''This function gets 2 lists and adds the second to the start of the first.
	   :param list_x: The list we would like use.
	   :type list_x: list.
	   :param list_y: The list we would like use.
	   :type list_y: list.
	   :return: list_x which contains list_y at the start of it.
	   :rtype: list.
	   '''
	list_x	= [*list_y, *list_x]
	return list_x


def main():
	help(extend_list_x)
	x = [4, 5, 6]
	y = [1, 2, 3]
	print(extend_list_x(x, y))
	
if __name__ == "__main__":
	main()