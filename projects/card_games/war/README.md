


1. Lets settle on a ruleset for the WAR cardgame.
- 2 Player Game
- The entire deck is dealt at the beginning


Jokers removed from the deck before dealing.


player deck addition/subtraction:
- Cards are thrown from the top of the player's deck
- Cards are recovered to the bottom of the player's deck.
- There is no discard pile and cards are never shuffled in the player deck (we chose this)


game flow:
- the game consists of consecutive rounds of play
- a round of play begins with each player throwing a card.
- the cards are then compared. The player with the higher ranked card wins (suits are ignored)
- if the card ranks are equal, a 'war' begins.


war events:
- each player puts 3 cards face down
- each player puts 1 card face up
- the face up cards are compared, the highest card wins.
- if the cards are even, another war is initiated (double war)... this can until exhausted.


We only have to test for losing - Losing:
- If you run out of cards, you lose.
- This can happen any time a card is drawn from your deck.
OUR TEST - IF A DRAW EVENT FAILS FOR YOU, YOU LOSE
- Both players must be tested at the same time in case they both lose.


2. Categorize deck and card interactions and tests during a game of war.




3. Write some behavior for 2 computer players to go head-to-head in war.



How will we define our game?

1. Start by defining objects:
Original Deck, Decks, Active Set, Players, Cards, Table

Each card is an object that has two data attributes rank and suit..
Original Deck is a class.
Original Deck is instantiated with one of each Card
Player has a Deck
Player has an Active Card?
Table has an Active Set for each Player?
Cards that have been played are stored in the Table (Community Object).

2. 







