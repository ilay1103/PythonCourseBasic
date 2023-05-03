def is_product_in_list(product, list_of_products):
	'''
	Returns if the product is in the list.
		:param product: The string we want to change.
		:type product: str.
		:param list_of_products: The list we want to check in.
		:type list_of_products: list.
		:return: If the product is in the list.
		:rtype: bool.
	   '''
	return product in list_of_products
	
def remove_duplicates_from_list(list_of_products):
	'''
	Returns the list without all the duplicates.
		:param list_of_products: The list we want to modify.
		:type list_of_products: list.
		:return: The new list without the duplicates.
		:rtype: list.
	   '''
	new_list_of_products = []
	for product in list_of_products:
		if product not in new_list_of_products:
			new_list_of_products.append(product)
	return new_list_of_products
	
def print_invalid_products(list_of_products):
	'''
	Prints all the invalid products.
	Product is invalid if he is smaller than 3 or contains characters other than the alphabetic letters.
		:param list_of_products: The list we want to check in.
		:type list_of_products: list.
		:return: None.
		:rtype: None.
	   '''
	invalid_product_list = []
	for product in list_of_products:
		if len(product)<3 or not product.isalpha():
			invalid_product_list.append(product)
	print(invalid_product_list)
	

def print_options():
	print('''
	1. Print the list of products.
	2. Print the number of products in the list.
	3. "Is the product on the list?"
	4. "How many times does a certain product appear?"
	5. Delete a product from the list.
	6. Add a product to the list
	7. Print all invalid products (a product is invalid if its length is less than 3 or it contains characters other than letters)
	8. Remove all existing duplicates in the list
	9. Exit
	   ''')


def main():
	option=0
	shoping_list= input("Enter your shopping list(for example 'Milk,Cottage,Tomatoes'): ")
	list_of_products = shoping_list.split(',')
	while option != 9:
		print_options()
		option = int(input("Enter the option you'd like to use: "))
		if option == 1:
			print(list_of_products)
		elif option == 2:
			print(len(list_of_products))
		elif option == 3:
			product = input("Which product? ")
			print(is_product_in_list(product, list_of_products))
		elif option == 4:
			product = input("Which product? ")
			if is_product_in_list(product, list_of_products):
				print(list_of_products.count(product))
			else:
				print("Product is'nt in the list.")
		elif option == 5:
			product = input("Which product? ")
			if is_product_in_list(product, list_of_products):
				list_of_products.remove(product)
			else:
				print("Product is'nt in the list.")
		elif option == 6:
			product = input("Which product? ")
			list_of_products.append(product)
		elif option == 7:
			print_invalid_products(list_of_products)
		elif option == 8:
			list_of_products = remove_duplicates_from_list(list_of_products)
		elif option == 9:
			print("Exit")
	
if __name__ == "__main__":
	main()