word = input("Enter a word: ").replace(" ","").lower()
if word[::] == word[-1::-1]:
	print("OK")
else:
	print("NOT")