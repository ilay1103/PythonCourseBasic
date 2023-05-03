def who_is_missing(file_name):
	'''Check the number missing in the series of the file.
	Writes the missing number to a new file called 'found.txt'.
	   :param file_name: The file we want to check.
	   :type file_name: str.
	   :return: The missing number.
	   :rtype: int.
	   '''
	open_file = open(file_name, 'r')
	open_found = open("found.txt", 'w')
	series = open_file.read()
	sorted_series_list = series.split(',')
	sorted_series_list.sort()
	missing = 1
	while (sorted_series_list is not None) and (str(missing) in sorted_series_list):
		missing += 1
	open_found.write(str(missing))
	open_file.close()
	open_found.close()
	return missing
	

def main():
	print(who_is_missing(r"findMe.txt"))
	
if __name__ == "__main__":
	main()