def are_lists_equal(list1, list2):
	'''This function gets 2 lists and chechs if ther match.
	   :param list1: The first list we would like check.
	   :type list1: list.
	   :param list2: The second list we would like check.
	   :type list2: list.
	   :return: If the lists match.
	   :rtype: bool.
	   '''
	list1.sort()
	list2.sort()
	return list1 == list2


def main():
	help(are_lists_equal)
	list1 = [0.6, 1, 2, 3]
	list2 = [3, 2, 0.6, 1]
	list3 = [9, 0, 5, 10.5]
	print(are_lists_equal(list1, list2))
	print(are_lists_equal(list1, list3))
	
if __name__ == "__main__":
	main()