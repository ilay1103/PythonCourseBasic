def copy_file_content(source, destination):
	'''Copy the contents from source file to the destination file.
	   :param source: The source file we want to copy from.
	   :type source: str.
	   :param destination: The destination file we want to paste into.
	   :type destination: str.
	   :return: None.
	   :rtype: None.
	   '''
	open_source = open(source, 'r')
	open_destination = open(destination, 'w')
	data = open_source.read()
	open_destination.write(data)
	open_source.close()
	open_destination.close()
	

def main():
	copy_file_content(r"copy.txt", r"paste.txt")
	
if __name__ == "__main__":
	main()