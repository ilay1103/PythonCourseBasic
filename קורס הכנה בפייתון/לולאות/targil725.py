def sequence_del(my_str):
	'''Returns a new string removing all the apearances of same letters apearing together.
	   :param my_str: The string we want to change.
	   :type my_str: str.
	   :return: A new string which removes the characters apearing more than once together.
	   :rtype: str.
	   '''
	new_str = my_str[0]
	for i in range(1, len(my_str)):
		if my_str[i] != my_str[i - 1]:
			new_str += my_str[i]
	return new_str


def main():
	help(sequence_del)
	print(sequence_del("ppyyyyythhhhhooonnnnn"))
	print(sequence_del("SSSSsssshhhh"))
	print(sequence_del("Heeyyy   yyouuuu!!!"))
	
if __name__ == "__main__":
	main()