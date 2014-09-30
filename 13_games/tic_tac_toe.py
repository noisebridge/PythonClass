

#board = range(10) #should we replace with string values? ya
board = [str(num) for num in range(10)]

def print_board():   
    print(board[:3]) 
    print(board[3:6]) 
    print(board[6:9]) 

def play():
    for turn in range(len(board) // 2): #we need 9 turns
        print_board()
        guess1 = int(raw_input("Player 1 enter your 'X' using corresponding integer\t"))
        if not str(board[guess1]).isdigit(): #extra validation check
            print("that spot is already taken tho!\n you lose your turn")
        else:
            board.pop(guess1)
            board.insert(guess1, 'X')
        print_board()
        guess2 = int(raw_input("Player 2 enter you 'O' using corresponding integer\t"))
        if not str(board[guess2]).isdigit(): #extra validation check
            print("that spot is already taken tho!\n you lose your turn")
        else:
            board.pop(guess2)
            board.insert(guess2, 'O')
    return board

def win():
    pass

play()