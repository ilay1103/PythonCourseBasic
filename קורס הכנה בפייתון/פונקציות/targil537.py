def chocolate_maker(small, big, x):
	SMALL_SIZE = 1
	BIG_SIZE = 5
	return (small + (big * BIG_SIZE)) >= x
	
print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))