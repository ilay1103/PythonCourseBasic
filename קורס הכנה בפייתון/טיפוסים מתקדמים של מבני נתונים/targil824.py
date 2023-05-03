def sort_anagrams(list_of_strings):
	'''Divides the list into sub-lists sorted by anagrams.
	   :param list_of_strings: First tuple.
	   :type list_of_strings: list.
	   :return: A list of all the anagrams.
	   :rtype: list.
	   '''
	list_of_anagram_types=[]
	list_of_anagrams=[]
	for word in list_of_strings:
		sorted_word = sorted(word)
		sorted_word = ''.join(sorted_word)
		if sorted_word in list_of_anagram_types:
			list_of_anagrams[list_of_anagram_types.index(sorted_word)].append(word)
		else:
			list_of_anagram_types.append(sorted_word)
			list_of_anagrams.append([word])
	return list_of_anagrams
	

def main():
	list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
	print(sort_anagrams(list_of_words))
	
if __name__ == "__main__":
	main()