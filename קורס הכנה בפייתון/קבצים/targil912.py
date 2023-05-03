def print_file_reversed(file_name):
	'''Read the lines in the file backwards.
	   :param file_name: The file we want to read.
	   :type file_name: str.
	   :return: None.
	   :rtype: None.
	   '''
	open_file = open(file_name, 'r')
	for line in open_file:
		print(line[-1::-1])
	open_file.close()
	
def sort_file_to_list(file_name):
	'''Sorts the words into a list by alphabetical order.
	   :param file_name: The file we want to read.
	   :type file_name: str.
	   :return: None.
	   :rtype: None.
	   '''
	open_file = open(file_name, 'r')
	sorted_list = []
	for line in open_file:
		list_line = line.replace('\n','').split(" ")
		for word in list_line:
			if word not in sorted_list:
				sorted_list.append(word)
	sorted_list.sort()
	print(sorted_list)
	open_file.close()
	
def print_lines(file_name, lines):
	'''Read the amount of lines in the secont parameter.
	   :param file_name: The file we want to read.
	   :type file_name: str.
	   :param lines: The amount of lines we want to read.
	   :type lines: int.
	   :return: None.
	   :rtype: None.
	   '''
	open_file = open(file_name, 'r')
	for i in range(lines):
		line = open_file.readline()
		print(line)
	open_file.close()

def main():
	file_name = input("Enter a file path: ")
	task = input("Enter a task(rev, sort, last): ")
	if task == "rev":
		print_file_reversed(file_name)
	elif task == "sort":
		sort_file_to_list(file_name)
	elif task == "last":
		lines = int(input("Enter a number: "))
		print_lines(file_name, lines)
	else:
		print("Wrong task input.")
	
	
if __name__ == "__main__":
	main()