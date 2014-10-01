import random

def create_code():
    """create_code() -> str, returns the 4 colors""" 
    code='' 
    #initialize our code object to an empty string in order to fill it with the
    # string values which will represent each color value
    colorList = ['r','y','b','g','o','p'] 
    #these represent the colors: red, yellow, blue, green, orange, purple
    for color in range(4): 
    #since there are only four colors total in our color code we use range(4) 
    #in order to pick only 4 colors
        randColor = random.randrange(len(colorList)) 
        #select an integer that will go on to represent the index
        #of a color in our colorList 
        #print(randColor)
        code += colorList[randColor] 
        #convert our random integer to a color representation
        #and add it to the code object
        #print(code)
        colorList.pop(randColor) #so we won't choose the color again, easy version
        #print(colorList)
    return code

def play_mm():
    """play_mm() -> str, 
    the string will return the display of either 
    a winning or losing statement to standard out"""

    colorCode = create_code() #generate a new set of four colors

    for currentGuessNumber in range(1, 11): 
    #each user will get ten turns, 
    #we will exit this loop only if the 'win condition' is satisfied 
    #with a return statement that prints a winning remark
        #below we give the user a thorough explanation of the rules to make an 
        #accurate guess on each turn
        guess = raw_input("""I've got a code of length 4 \n \
Each color is represented by a letter r-y-b-g-o-p \n \
Guess #{} -- enter four of these letters as your guess: """ \
                            .format(currentGuessNumber)) 
        listCode = list(colorCode) 
        #we will use a list data structure to compare our guesses and code
        listGuess = list(guess) 
        #using lists allows us to easily keep order and access each element
        blackPegs = 0 
        #initializing blackPegs as int value for the win! Do this for each turn!
        whitePegs = 0 
        #initializing whitePegs as int value, 
        #both these Peg values will need to be displayed
        for color in [0, 1, 2, 3]: 
        #enter a loop that will check all four possibilities for matches
            if listCode[color] == listGuess[color]: #check exact matches
                blackPegs += 1 #if condition is met than we add a black peg 
                #above, we'll add one for the user on the color number 
                #who is probably not thinking in pure computer terms!
            elif listCode[color] in listGuess: 
            #for each color we can simply check if there are any other colors that 
            #are in the listCode without worrying about position using 'in'
                whitePegs += 1
            else:
                pass
        #now we need to make a thorough report of how that turn went so that
        #the user can make an educated guess of what the next guess should be
        print('\nAlright! You got {0} black pegs {1} white pegs on guess #{2}\n' \
            .format(blackPegs, whitePegs, currentGuessNumber))
        print "================="

        if blackPegs == 4: 
        #we need to take care of the win condition and check it 
        #on each turn if the player wins!
            return 'You cracked the code!' #exit from out for loop

    return "You didn't guess my code in ten turns. Sorry--YOU LOST! \n \
        The code was: {}".format(colorCode)
play_mm()
