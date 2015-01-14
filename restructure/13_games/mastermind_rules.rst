Mastermind is a game for 2 players. The commercial version of the game uses six colors, which vary from game to game; for our purposes we'll use red, yellow, blue, green, orange, and purple. One player (the codemaker) thinks of a secret code, which is any 4 colors in some order (in the easy version of the game, the 4 colors all have to be different; in the harder version, a color is allowed to repeat one or more times). The other player (the codebreaker) has 10 attempts to guess the code.

For each guess, the codemaker tells the codebreaker how many colors are correct and in the correct location, and how many colors are correct but in the wrong location. The guesser is not told exactly which colors are correct. In the commercial version of the game, black and white pegs are used for this: a black peg means a color correct and in the correct location, a white peg means a color correct but not in the correct location. You can use black and white as a shorthand for your responses.

Here's an example: suppose the code is red-blue-red-yellow.

If a guess is green-blue-purple-purple, the response would be 1 black 0 white (meaning that one peg---the blue one---is correct and in the correct location, and the rest are incorrect).

If a guess is red-yellow-green-purple, the response would be 1 black 1 white (the red is correct and in the correct location, the yellow is correct but in the wrong location).

If a guess is red-red-blue-orange, the response would be 1 black 2 white.

If a guess is blue-green-blue-red, the response would be 0 black 2 white (only one of the two blue guessed gets a white peg, since there is only one blue in the actual code).

Implement this game where the computer randomly generates a code, and the user plays as the codebreaker. The codebreaker wins if he or she gets the code in 10 guesses or less. You can decide whether to implement the easy or hard version of the game (or both)



Sample output on CLI:

I've got a code of length 4
It uses colors in rybgop
Guess #1 -- enter your guess: rybg
1 black 1 white
Guess #2 -- enter your guess: ryop
2 black 1 white
Guess #3 -- enter your guess: rpyo
1 black 2 white
Guess #4 -- enter your guess: ryog
1 black 2 white
Guess #5 -- enter your guess: ropy
2 black 1 white
Guess #6 -- enter your guess: ropg
2 black 2 white
Guess #7 -- enter your guess: rogp


https://www.youtube.com/watch?v=PeAO2jnegBc - 1 min video explanation