def mult_tuple(tuple1, tuple2):
	'''Creates all the combinations possible between each 2 members in the tuples.
	   :param tuple1: First tuple.
	   :type tuple1: tuple.
	   :param tuple2: Second tuple.
	   :type tuple2: tuple.
	   :return: A tuple of all the possibilities.
	   :rtype: tuple.
	   '''
	all_possibilities = []
	for item1 in tuple1:
		for item2 in tuple2:
			all_possibilities.append((item1, item2))
			all_possibilities.append((item2, item1))
	new_tuple= tuple(all_possibilities)
	return new_tuple


def main():
	first_tuple = (1, 2)
	second_tuple = (4, 5)
	print(mult_tuple(first_tuple, second_tuple))
	
if __name__ == "__main__":
	main()