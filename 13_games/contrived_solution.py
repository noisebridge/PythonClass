#ugh, this is kinda ugly, i did not write

import random

def return_matches(guess,code):
    '''return_matches(guess,code) -> (int,int)
    returns matches of guess to code
    first int is "black" (exact matches)
    second int is "white" (right color, wrong position)'''
    black, white = 0, 0  # initialize match variables
    # use these lists to keep track of matches
    guessMatched = [False]*len(guess)
    codeMatched = [False]*len(guess)
    # determine exact matches
    for n in range(len(guess)):
        if guess[n] == code[n]:
            guessMatched[n] = True
            codeMatched[n] = True
            black += 1
    # determine position matches
    for n in range(len(guess)):
        if not guessMatched[n]: # not a black match, check for white match
            for char in range(len(guess)):  # loop through the code
                if not codeMatched[char] and guess[n]==code[char]:
                    # found a match -- update and break
                    codeMatched[char] = True
                    white += 1
                    break
    return (black,white)

def play_mastermind(codeLength,numGuesses,difficulty):
    '''play_mastermind(codeLength,numGuesses) -> None
    play a game of mastermind
    codeLength is the length of the code
    numGuesses is the number of guesses allowed
    difficulty is 'easy' or 'hard' '''
    colors = 'rybgop'
    code = ''
    winner = False
    # create a code
    for i in range(codeLength):
        color = colors[random.randrange(len(colors))]
        while difficulty == 'easy' and color in code:
            # duplicate color, pick another
            color = colors[random.randrange(len(colors))]
        code += color
    # play the game
    print("I've got a code of length "+str(codeLength))
    print("It uses colors in "+colors)
    for turn in range(1,numGuesses+1):
        legalGuess = False
        while not legalGuess:
            guess = raw_input("Guess # "+str(turn)+" -- enter your guess: ")
            legalGuess = True
            # check for legal guess
            if len(guess) == codeLength:
                # check for legal colors
                for index in range(codeLength):
                    if guess[index] not in colors:
                        legalGuess = False
            else:
                legalGuess = False
            if not legalGuess:
                print("That's not a legal guess!")
        (black,white) = return_matches(guess,code)
        if black==4:
            print("You cracked the code!")
            winner = True
            break
        print(str(black)+" black "+str(white)+ " white")
    if not winner:
        print("Sorry, you ran out of guesses!")
        print("The code was: "+str(code))

play_mastermind(4,10,'hard')