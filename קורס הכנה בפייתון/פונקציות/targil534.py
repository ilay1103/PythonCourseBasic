def last_early(my_str):
	return my_str.count(my_str[-1]) > 1
	
stam_str=input("Enter a senctence: ")
print(last_early(stam_str))