import random

def create_code():
    """create_code() -> str, returns the 4 colors""" 
    code='' #initialize our code object to an empty string in order to fill it with the string values which will represent each color value
    colorList = ['r','y','b','g','o','p'] # these represent the colors: red, yellow, blue, green, orange, purple
    for color in range(4): #since there are only four colors total in our color code we use range(4) to pick only 4 colors
        randColor = random.randrange(len(colorList)) # select an integer that will represent the index of a color in our colorList 
        #print(randColor)
        code += colorList[randColor] # convert our random integer to a color representation and add it to the code object
        #print(code)
        colorList.pop(randColor) # so the computer can't choose the color again
        #print(colorList)
    return code

def play_mm():
    """play_mm() -> str, which will return the display of either a winning or losing statement to standard out"""
    #currentGuessNumber = 1 #we will need to keep track of which guess out of 10 the user is making and display it
    colorCode = create_code() #generate a new set of four colors
    for currentGuessNumber in range(1, 11): #each user will get ten turns, we will exit this loop if the 'win condition' is satisfied with a return statement
        #below we give the user a thorough explanation of the rules to make an accurate guess on each turn
        guess = raw_input("I've got a code of length 4 \nEach color is represented by a letter r-y-b-g-o-p \nGuess #{} -- enter four of these letters as your guess: ".format(currentGuessNumber)) 
        listCode = list(colorCode) #we will use a list data structure to compare our guesses and code
        listGuess = list(guess) #using lists allows us to easily keep order and access each element
        blackPegs = 0 #initializing blackPegs as int value for the win! Note we need to do this for each turn!
        whitePegs = 0 #initializing whitePegs as int value, both these Peg values will need to be displayed
        for color in [0, 1, 2, 3]: # enter a loop that will check all four possibilities for matches
            #print("code of length 4 \nIt uses colors in rybgop")
            if listCode[color] == listGuess[color]: #check exact matches
                blackPegs += 1 #if condition is met than we add a black peg and display which color out of four was correct
                #totally could print the place of black peg if that was part of the rules though
                #print("You nailed a black peg on the number {0} color, {1}".format(color+1, listCode[color])) 
                #above, we'll add one for the user on the color number who is probably not thinking in computer terms!
            elif listCode[color] in listGuess: #we can simply see if there are any other colors that are in the listCode without worrying about position
                whitePegs += 1
            else:
                pass
        #now we need to make a thorough report of how that turn went so that the user can make an educated guess of what the next guess should be
        print('\nAlright! You got {0} black pegs {1} white pegs on guess #{2}\n'.format(blackPegs, whitePegs, currentGuessNumber))

        if blackPegs == 4: #we need to take care of the win condition and check it on each turn if the player wins!
            return 'You cracked the code!' #exit from out for loop

        return "You didn't guess my code in ten turns. Sorry--YOU LOST! \nThe code was: {}".format(colorCode)
play_mm()