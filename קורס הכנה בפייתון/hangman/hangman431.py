character_guessed=input("Guess a letter: ")

if len(character_guessed)>1 and not character_guessed.isalpha():
	print("E3")
elif len(character_guessed)>1:
	print("E1")
elif not character_guessed.isalpha():
	print("E2")
else:
	print(character_guessed.lower())