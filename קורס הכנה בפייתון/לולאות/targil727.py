def arrow(my_char, max_length):
	'''
	Returns a tring of an arrow.
		:param my_char: The character we will use for the arrow.
		:type my_char: str.
		:param max_length: The kength of the head of the arrow.
		:type max_length: int.
		:return: The string with the arrow shape.
		:rtype: str.
	   '''
	my_arrow = ''
	for i in range(1, max_length):
		my_arrow += (my_char * i) + '\n'
	for i in range(max_length, 0, -1):
		my_arrow += (my_char * i) + '\n'
	return my_arrow



def main():
	print(arrow('*',1))
	print(arrow('*',4))
	print(arrow('8',7))
	print(arrow('*',9))
	
if __name__ == "__main__":
	main()