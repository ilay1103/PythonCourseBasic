def is_greater(my_list, n):
	'''Returns all members in the list which are greater than n.
	   :param my_list: The list we check.
	   :type my_list: list.
	   :param n: The number we compare with.
	   :type n: int.
	   :return: The list of all the numbers bigger than n.
	   :rtype: list.
	   '''
	bigger_list=[]
	for num in my_list:
		if num > n:
			bigger_list.append(num)
	return bigger_list


def main():
	help(is_greater)
	result = is_greater([1, 30, 25, 60, 27, 28], 28)
	print(result)
	
if __name__ == "__main__":
	main()