def inverse_dict(my_dict):
	'''Inverse the dictionary.
	   :param my_dict: The dictionary we want to inverse.
	   :type my_dict: dict.
	   :return: New dictionary with the values and keys inversed.
	   :rtype: dict.
	   '''
	inversed_dict = {}
	for pair in my_dict.items():
		if pair[1] in inversed_dict.keys():
			inversed_dict[pair[1]].append(pair[0])
			inversed_dict[pair[1]].sort()
		else:
			inversed_dict[pair[1]] = [pair[0]]
	return inversed_dict
	

def main():
	course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
	print(inverse_dict(course_dict))
	
if __name__ == "__main__":
	main()