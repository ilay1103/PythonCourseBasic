def sort_prices (list_of_tuples):
	'''sorts the tuples by their prices.
	   :param list_of_tuples: List of tuples. each tuple has a value of 'item' and 'price'.
	   :type list_of_tuples: list.
	   :return: the list sorted by the prices.
	   :rtype: list.
	   '''
	list_of_tuples=sorted(list_of_tuples, key = lambda x: x[1], reverse = True)
	return list_of_tuples


def main():
	products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
	print(sort_prices(products))
	
if __name__ == "__main__":
	main()