"""
***Blackjack***
Project Report:
    The first thing that I had to do was create lists for the cards and include all of their info.
    I could not figure out a way to implement color on time because it would create way too many cards.
    Next I created the card class and included their suit and rank and then also having a function
    that will return the card information to the user. Next was a deck to hold all the cards. I created
    4 individual decks and then appended them all into one shoe and then shuffled the shoe using random
    I then created a deal function to deal out the cards. I used pop to remove that card from the deck.
    I did not use private variables I was having too many issues and just had to switch them to public so
    the program would actually run.  I then created the hand class to hold the cards created in the card class.
    I used an array to hold the cards and act as the dealer and players hand and
    then made the addCard functio that would append them to the array and calculate the
    value of the combined cards. I also kept track of the number of aces but ran out
    of time before actually being able to apply that number anywhere. The money class holds all of the information regarding the bank accounts of the player
    and dealer. I used a random int from 500-5000 to get the players number. The betLost
    and betWon function will give or take away funds from the bet depending on if the user won or lost.
    I also displayed the total and bet in the class. After I was done making the classes I moved on to the functions and created a betFunction
    that would use user input to make the bet. A hit function to append a card to the players hand.
    A showInfo function that displays the dealer and player hands and their bank values. The showdealer
    function does the same thing but does not hide the dealers first card. I then initialized everything including the deck and playerfunds. I shuffled the deck
    and then asked the user if they wanted to play and introduced the game to them. I deal out
    the cards and keep track of the round numbers. Next I display all the info to the user and ask them if they want to hit double or stand.
    After this I use a lot of if statements to track whether the dealer or player busted, lost,
    or got a blackjack. The while loop I use means the player can play indefinitely and choose how
    long they want to spend money for.

    The code did not end up exactly how I wanted but the end result is a working game thankfully.
    I put it off for too long and the problems that were a lot bigger than I thought they would be
    took up a lot of time and some of them did not even get implemented.
"""
import random

#Creating the lists to hold the suits ranks and values of each card
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
#Creating the card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self): #Returning the information to the user
        return ' Symbol: ' + self.suit + ' Value: ' + self.rank + '\n'

#Creating the deck class
class Deck:
    def __init__(self):
        self.deck = []  #The main shoe deck
        self.d1 = [] #The 4 decks that will be shuffled together
        self.d2 = []
        self.d3 = []
        self.d4 = []
        for i in suits: #Using 2 for loops to append each rank to their suit
            for j in ranks:
                self.d1.append(Card(i, j)) #Creating 4 decks
                self.d2.append(Card(i, j))
                self.d3.append(Card(i, j))
                self.d4.append(Card(i, j))
        self.deck = [*self.d1, *self.d2, *self.d3, *self.d4] #Appending them all to one shoe

    def shuffle(self): #Shuffling function
        random.shuffle(self.deck) #Shuffle them all together

    def deal(self): #Function to deal out cards
        playingCard = self.deck.pop() #Popping the card to remove it from the deck
        return playingCard #Returning the card
]
#Creating the hand class
class Hand:
    def __init__(self):
        self.cards = [] #Creating the array to hold the cards
        self.value = 0 #Adding the values of the cards together
        self.aces = 0 #Counting the number of aces just in case there are 2

    def addCard(self, card):
        self.cards.append(card) #Appending to the hand
        self.value = self.value + values[card.rank] #Adding up the values
        if card.rank == 'Ace':
            self.aces = self.aces + 1

#Creating the money class
class Money:
    def __init__(self):
        self.total = self.total = random.randint(500,5000) #initializing the total to a number between 500 and 5000
        self.bet = 0 #Setting bet to 0

    def betLost(self): #Subtracting from the total if the bet is lost
        self.total -= self.bet

    def betWon(self): #Adding to the total if the bet is won
        self.total += self.bet

    def __str__(self): #Displaying info to the user
        return ' TotalBet: $' + self.bet + ' InBank: $' + self.rank

def betFunction(money): #Function for the user to choose their betting amount
            print("You current total is $", money.total)
            money.bet = int(input("How much money would you like to bet? "))

def hit(deck, hand): #Hit function to get card
    hand.addCard(deck.deal())

def showInfo(player, dealer): #Displaying all the info to the user
    print("Dealer info: ") #Hiding the first dealers card
    print(dealer.cards[1])
    print("Player info: ") #Showing the users cards
    print(*player.cards)
    print(" Total value:", player.value) #Displaying their bank information
    print("TotalBet: $", playerFunds.bet, "InBank: $", playerFunds.total)

def showDealer(player, dealer): #Same function as above but it shows the dealers cards
    print("Dealer info: ")
    print(*dealer.cards)
    print(" Total value: ", dealer.value, '\n')
    print(" Total value: ", dealer.value)
    print("Player info: ")
    print(*player.cards)
    print(" Total value:", player.value)
    print("TotalBet: $", playerFunds.bet, "InBank: $", playerFunds.total)


deck = Deck() #creating the deck
deck.shuffle() #Shuffling the deck
playerFunds = Money() #Creating the players funds

#Asking the user if they want to play
status = int(input("Would you play a game of BlackJack? Enter 1 for yes or 0 for no "))
if(status==1):
#Introducing the player to the game
    print("Welcome to BlackJack! Each game will consist of 10 rounds and the player will be dealt a random amount of money")
while(status != 0):
    playerHand = Hand() #Creating the player hand and giving them 2 cards
    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())

    dealerHand = Hand() #Creating the dealer hand and giving them 2 cards
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    betFunction(playerFunds) #Asking the player for their bet
    i=1 #Keeping track of the rounds
    print("-------------------Round", i, "-------------------")
    i=i+1
    showInfo(playerHand, dealerHand) #Displaying the info
    choice = input("\nOptions available: 1 Hit 2 Double 3 Stand: ")
    if choice == '1': #Player adds another card to their deck
        playerHand.addCard(deck.deal())
    if choice == '2': #Player doubles their bet and addes another card
        playerFunds.bet = playerFunds.bet*2
        playerHand.addCard(deck.deal())
    elif choice == '3': #Player does not draw another card
        print("Player stands, Dealer is playing.")
    print("-------------------Round", i, "-------------------")
    i=i+1
    showInfo(playerHand, dealerHand)

    #If statements to track who wins or loses or busts
    if playerHand.value > 21:
        print("PLAYER BUSTS!")
        playerFunds.betLost()

    if playerHand.value <= 21:

        while dealerHand.value < 17:
            dealerHand.addCard(deck.deal())
        print("-------------------Round", i, "-------------------")
        i=i+1
        showDealer(playerHand, dealerHand)

        if dealerHand.value > 21:
            print("The dealer busted")
            playerFunds.betWon()

        elif dealerHand.value > playerHand.value:
            print("The dealer won")
            playerFunds.betLost()

        elif dealerHand.value < playerHand.value:
            print("The player won")
            money.betWon()

        if playerHand.value > 21:
            print("The platyer busted")
            playerFunds.betLost()

        if playerFunds.total > 50:
            status = 0

    #New round starts
    playerHand = Hand()
    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())

    dealerHand = Hand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    print("The player now  has$", playerFunds.total)
    status = int(input("Enter 1 to continue playing or 0 to stop "))
