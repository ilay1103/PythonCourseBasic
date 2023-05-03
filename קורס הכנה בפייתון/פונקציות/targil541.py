
def func(num1, num2):
	'''This function gets 2 parameters
	   and return the sum of them.
	   :param num1: The first number we get.
	   :type num1: int.
	   :param num2: The second number we get.
	   :type num2: int.
	   :return: The sum of both numbers.
	   :rtype: int
	   '''
	return num1 + num2
	
def main():
	help(func)
	print(func(1, 3))
	
if __name__ == "__main__":
	main()