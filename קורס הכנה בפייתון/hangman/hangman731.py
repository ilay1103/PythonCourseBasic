def show_hidden_word(secret_word, old_letters_guessed):
    '''Shows the correct letters guessed in the right spots of the secret string.
       :param secret_word: The number we start from.
       :type secret_word: int.
       :param old_letters_guessed: List of the letters guessed.
       :type old_letters_guessed: list.
       :return: The string with the correct letters guessed.
       :rtype: str.
       '''
    current_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            current_word += letter
        else:
            current_word += '_'
    current_word = ' '.join(current_word)
    return current_word


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()