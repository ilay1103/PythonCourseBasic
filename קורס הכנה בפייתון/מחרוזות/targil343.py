sentence = input("Please enter a string: ")
print(sentence[:int(len(sentence)/2)].lower() + sentence[int(len(sentence)/2):].upper())