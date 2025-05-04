import random

words_list = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
             'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
             'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
             'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
             'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spide',
             'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf',
             'wombat', 'zebra']

def asciiart(count):
    match count:
        case 1:
            print(r'''
                +---+
                |   |
                    |
                    |
                    |
                    |
                == == == == ==''')
        case 2:
            print(r'''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
        case 3:
            print(r'''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
        case 4:
            print(r'''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''')
        case 5:
            print(r'''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========''')
        case 6:
            print(r'''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''')
        case 7:
            print(r'''GAME OVER!
                         +---+
                         |   |
                         O   |
                        /|\  |
                        / \  |
                             |
                       =========''')

ch = input("Enter 'y' if you want to start playing\n")

while ch.lower() == "y":
    # RESET game state here
    c_word = random.choice(words_list)
    length = len(c_word)
    display = ['_'] * length
    count = 0
    gmover = False

    print("\nGuess the word:")
    print(' '.join(display))

    while not gmover:
        inp = input("Enter a letter: ").lower()

        if inp in c_word:
            for i in range(length):
                if c_word[i] == inp:
                    display[i] = inp
            print(' '.join(display))
        else:
            count += 1
            asciiart(count)

        if "_" not in display:
            print("🎉 Congratulations! You guessed the word correctly:", c_word)
            gmover = True

        if count >= 7:
            print("😢 The word was:", c_word)
            gmover = True

    ch = input("\nEnter 'y' if you want to play again\n")
