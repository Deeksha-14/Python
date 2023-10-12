print('Hi there! Welcome to the Guessing Game')
SecretNum = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input(f'Guess {guessCount+1}: '))
    guessCount = guessCount + 1
    if guess == SecretNum:
        print('Congratulations you won')
        break
else:
    print('Sorry, you lose!')

