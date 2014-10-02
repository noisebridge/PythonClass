import random as r 
import copy

poss_colors = ['r','g','p','y','b','o','c','w'] #for user as well
ran_colors = copy.deepcopy(poss_colors)
r.shuffle(ran_colors)
code = ran_colors[:4]

#print code

print("You get 10 turns to guess the code")

guess = ''

def validate_guess(guess=''):
	valid_guess = False #sentinel value
	valid_ltrs = [ltr for ltr in guess if ltr in ran_colors]
	if len(guess) == 4 and len(valid_ltrs) == 4 and len(set(guess)) == 4:
		valid_guess = True
	return valid_guess










for turn in range(10): 
	while validate_guess(guess) == False:
		guess = raw_input("State four ordered unique colors out of these possible colors {}\n".format(poss_colors))
		print "validated"

	white_pegs = 0
	black_pegs = 0


	for index in range(len(code)):
		if guess[index] in code:
			white_pegs += 1
		if guess[index] == code[index]:
			white_pegs -= 1
			black_pegs += 1
	if black_pegs == 4:
		print "you win!!!!!!!"
		quit() #quti() or exit()

	guess = ''
	print("turn #{}".format(turn))

	print("you have {} black pegs and {} white pegs".format(black_pegs, white_pegs))
		
print("put down your fucking cell phone and play the game you loser, is it too hard, dumass?")

	


