def are_files_equal(file1, file2):
	'''Check if two files contain the same data in them.
	   :param file1: The firs file.
	   :type file1: str.
	   :param file2: The second file.
	   :type file2: str.
	   :return: if the file's contents is equal.
	   :rtype: bool.
	   '''
	open_file1 = open(file1, 'r')
	open_file2 = open(file2, 'r')
	content_file1 = open_file1.read()
	content_file2 = open_file2.read()
	open_file1.close()
	open_file2.close()
	return content_file1 == content_file2
	

def main():
	print(are_files_equal(r"G:\Documents\קורס הכנה בפייתון\קבצים\file1.txt", r"G:\Documents\קורס הכנה בפייתון\קבצים\file2.txt"))
	
if __name__ == "__main__":
	main()