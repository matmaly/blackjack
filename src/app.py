#!/usr/bin/env python3
'''
Author: Mateusz Maly
Description: Blackjack game against computer
'''

import random 

class Blackjack:
    deck = [("2 Spades",2),("3 Spades",3),("4 Spades",4),("5 Spades",5),("6 Spades",6),("7 Spades",7),("8 Spades",8),("9 Spades",9),("10 Spades",10),("Jack Spades",10),("Queen Spades",10),("King Spades",10),("Ace Spades",11,1),("2 Clubs",2),("3 Clubs",3),("4 Clubs",4),("5 Clubs",5),("6 Clubs",6),("7 Clubs",7),("8 Clubs",8),("9 Clubs",9),("10 Clubs",10),("Jack Clubs",10),("Queen Clubs",10),("King Clubs",10),("Ace Clubs",11,1),("2 Diamonds",2),("3 Diamonds",3),("4 Diamonds",4),("5 Diamonds",5),("6 Diamonds",6),("7 Diamonds",7),("8 Diamonds",8),("9 Diamonds",9),("10 Diamonds",10),("Jack Diamonds",10),("Queen Diamonds",10),("King Diamonds",10),("Ace Diamonds",11,1),("2 Hearts",2),("3 Hearts",3),("4 Hearts",4),("5 Hearts",5),("6 Hearts",6),("7 Hearts",7),("8 Hearts",8),("9 Hearts",9),("10 Hearts",10),("Jack Hearts",10),("Queen Hearts",10),("King Hearts",10),("Ace Hearts",11,1)
            ]
    cards_left = 51
    player_cards = []
    dealer_cards = []

    def __init__(self, player_name):
        self.player_name = player_name
        
        self.new_game_setup()
        while True:
            decision = input()
            if decision == "hit":
                score = self.player([self.deck[self.draw()]])
                if score == 21:
                    print("Blackjack")
                    break
                elif score > 21:
                    print("Bust!!!")
                    break
            elif decision == "stand":
                dealer_score = self.score(self.dealer_cards)
                if dealer_score < 17:
                    dealer_score = self.dealer([self.deck[self.draw()]])
            elif decision == "stop":
                break
    
    # Method that takes the card out of the deck so it can't be used again
    def take_card_out_of_deck(self, card):
        self.card = card
        
        del self.deck[card]
        self.cards_left -= 1

    # Method to draw a card and call a method to take that card out of the deck
    def draw(self):
        draw = random.randint(0,self.cards_left -1)        
        self.take_card_out_of_deck(draw)
        return draw
    
    # Method that sets up the game by giving the player 2 cards and 1 card to the computer
    # First it calls the player method and passes the deck as parameter, calling the draw method to return a random integer
    def new_game_setup(self):
        self.player([self.deck[self.draw()],self.deck[self.draw()]])
        self.dealer([self.deck[self.draw()]])

    # Method that displays what cards the player currently has
    # Adds the total score of the cards
    def player(self, new_cards):
        self.player_cards += new_cards
        
        score = self.score(self.player_cards)

        print(f"Player Cards: {self.player_cards}")
        print(f"Player Score: {score}")
        
        return score

    # Method that will print the cards that the dealer has
    # Adds the total score of the cards
    def dealer(self, new_cards):
        self.dealer_cards += new_cards
        
        score = self.score(self.dealer_cards)

        print(f"Dealer Cards: {self.dealer_cards}")
        print(f"Dealer Score: {score}")
    
        return score

    def score(self, cards):
        self.cards = cards
        score = 0
        
        for card_points in self.cards:
            score += card_points[1]
                
        return score

    def __str__(self):
        return self.deck[0][0]

b = Blackjack("Bob")
