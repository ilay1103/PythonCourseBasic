def check_win(secret_word, old_letters_guessed):
    '''Shows the correct letters guessed in the right spots of the secret string.
       :param secret_word: The number we start from.
       :type secret_word: int.
       :param old_letters_guessed: List of the letters guessed.
       :type old_letters_guessed: list.
       :return: The string with the correct letters guessed.
       :rtype: str.
       '''
    win = True
    for letter in secret_word:
        if letter not in old_letters_guessed:
            win = False
    return win


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(check_win(secret_word, old_letters_guessed))
    old_letters_guessed +=  ['a', 'l']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()
