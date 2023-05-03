def seven_boom(end_number):
	'''Returns a list of all the numbers between 0 and the given number.
	All the numbers which contain 7 in them or divided by 7 are replaced with 'BOOM'.
	   :param end_number: The int we stop at.
	   :type end_number: int.
	   :return: List of the numbers between 0 and the given number.
	   all the numbers which contain 7 in them or divided by 7 are replaced with 'BOOM'.
	   :rtype: list.
	   '''
	boom_list = []
	for i in range(end_number + 1):
		if ("7" in str(i)) or (i % 7 == 0):
			boom_list.append("BOOM")
		else:
			boom_list.append(i)
	return boom_list


def main():
	help(seven_boom)
	print(seven_boom(17))
	
if __name__ == "__main__":
	main()