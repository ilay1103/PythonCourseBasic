
def print_options():
	print('''
	1. Print last name.
	2. Print the mounth of Maria was born.
	3. Amount of hobbies Maria has.
	4. Most recent hobby.
	5. Add 'Cooking' to her hobbies.
	6. Print birth date(as tuple).
	7. Add age.
	   ''')


def main():
	option = 0
	maria_dict = {"first_name": "Maria", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
	print_options()
	option = int(input("Enter the option you'd like to use: "))
	if option == 1:
		print(maria_dict["last_name"])
	elif option == 2:
		print(maria_dict["birth_date"].split('.')[1])
	elif option == 3:
		print(len(maria_dict["hobbies"]))
	elif option == 4:
		print(maria_dict["hobbies"][-1])
	elif option == 5:
		maria_dict["hobbies"].append("Cooking")
		print(maria_dict["hobbies"])
	elif option == 6:
		print(tuple(maria_dict["birth_date"].split('.')))
	elif option == 7:
		age = int(input("Enter Maria's age: "))
		maria_dict["age"] = age
		print(maria_dict)
	
if __name__ == "__main__":
	main()