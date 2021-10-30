# MS Code Oympics 21 example files

## Challenge 1 - Credit card checker
We want you to write a script to make sure a 16-digit credit card number is correct.
The program will need to be able to take in a file where every line is a separate credit card
number
And output a CSV file in the format
CC Number, validity, Check digit, Issuer, testcard
16-digit number, Y/N, 1 digit number, string, Y/N

Example input and output files in this github 
 - input: credit_cards
 - output cc_out.csv 

Marking
* 50% of marks for working validity check and check digit calculation
* 25% for being able to work out issuer
* 25% if it’s a test card or not

## challange 2 - SQL Challange 
 https://github.com/iain-mc/sqlchallenge

## Challenge 3 - poker hand checker

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:
• High Card: Highest value card.
• One Pair: Two cards of the same value.
• Two Pairs: Two different pairs.
• Three of a Kind: Three cards of the same value.
• Straight: All cards are consecutive values.
• Flush: All cards of the same suit.
• Full House: Three of a kind and a pair.
• Four of a Kind: Four cards of the same value.
• Straight Flush: All cards are consecutive values of same suit.
• Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens, then
highest cards in each hand are compared (see example 4 below); if the highest
cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand Player 1 Player 2 Winner

1
5H 5C 6S 7S KD
Pair of Fives

2C 3S 8S 8D TD

Pair of Eights Player 2

2
5D 8C 9S JS AC

Highest card Ace

2C 5C 7D 8S QH

Highest card Queen Player 1

3
2D 9C AS AH AC

Three Aces

3D 6D 7D TD QD

Flush with Diamonds Player 2

4
4D 6S 9H QH QC

Pair of Queens
Highest card Nine

3D 6D 7H QD QS

Pair of Queens
Highest card Seven Player 1

5
2H 2D 4C 4D 4S

Full House
With Three Fours

3C 3D 3S 9S 9D

Full House
with Three Threes Player 1

The program should take an input file of which each line contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five
are Player 2's cards. You can assume that all hands are valid (no invalid
characters or repeated cards), each player's hand is in no specific order, and in
each hand, there is a clear winner.

The output should be the number of hands player 1 wins, example input is poker_input.txt. Full marks for correct answer

## Challenge 4 - procedural pumpkin asci art generator
We want you to write a script that procedurally generates random pumpkins in the
terminal.
Rules are it can only be 80*24 char (standard terminal size)
Can only use ascii symbols and ANSI codes in your output

Making is 80% for working and believable pumpkins and 20% remains for subjective
marking of the uniqueness or innovativeness of the output

## Challenge 5 – Make the news Happy
We want you to scrape a website (website will be provided on Saturday) for all its
headlines and modify them to be positive, bonus points if they read well in context
and top marks if you are able to re-host the website while replacing the headlines

### makring 
* 50% for working basic implementation
* 25% for the headlines reading well
* The last 25% for hosting a copy of the webpage with your new headlines
