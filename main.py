from random import randint


def ask_user():
    """
    Ask user to enter a number. That number will then be compared to the
    computer's answer
    """
    ans = 0

    while True:
        # Run loop

        ans = input('Enter a number between 0-20: ')

        if ans.isdigit():
            ans = int(ans)
        else:
            print('\nEnter a valid number!')

        if ans > 20:
            print('Enter a number within the desired range\n')
        else:
            break

    return ans


def compare(number, answer):
    """
    Find the difference of the random number and player answer. From
    there give the player a hint
    """
    if abs(number - answer) <= 5:
        print('Warm')
    else:
        print('Cold')


if __name__ == '__main__':

    # Find a random number
    random_num = randint(0, 21)

    # Player will keep on guessing until he/she answers correctly
    while True:
        # Ask user for an number
        user_ans = ask_user()

        # Compare numbers
        if user_ans == random_num:
            print('You guessed the right answer!\n')

            # Ask the player if he/she wants to play again
            play_again = input('Do you want to play again? y/n\n')
            if play_again == 'y':

                # Generate a new random number for the new game
                random_num = randint(0, 21)
                continue

            else:
                print('Thanks for playing!')
                break

        else:
            # Give the player a hint
            compare(random_num, user_ans)

            print('Wrong answer! Try again.\n')
            continue
