def squared_numbers(start, stop):
	'''Returns all the squared numbers between start and stop.
	   :param start: The number we start from.
	   :type start: int.
	   :param stop: The number we stop at.
	   :type stop: int.
	   :return: The list of all the squared values.
	   :rtype: list.
	   '''
	squared_list = []
	i = start
	while i <= stop:
		squared_list.append(i ** 2)
		i += 1
	return squared_list


def main():
	help(squared_numbers)
	print(squared_numbers(4, 8))
	print(squared_numbers(-3, 3))
	
if __name__ == "__main__":
	main()