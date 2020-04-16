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
    player_account = 0

    def __init__(self, player_name):
        self.player_name = player_name
        self.round_end = False
        
        self.new_game_setup()        
        bet = self.new_round_setup()
        while not self.round_end:
            self.payout(bet, self.check_cards(self.score(self.player_cards)))
            decision = input()
            if decision == "hit":
                score = self.player([self.deck[self.draw()]])
                self.print_result("p", self.player_cards, score)
                self.payout(bet, self.check_cards(self.score(self.player_cards)))
            elif decision == "stand":
                dealer_score = self.score(self.dealer_cards)
                self.dealer_hit(dealer_score)
                self.payout(bet, self.check_cards(self.score(self.player_cards),self.score(self.dealer_cards),stand_flag=True))
            elif decision == "stop":
                break
    
    # Checks the cards for wins or busts
    def check_cards(self, player_score, dealer_score=0, stand_flag=False):
        self.player_score = player_score
        self.dealer_score = dealer_score
        self.stand_flag = stand_flag
        
        if self.player_score == 21:
            print("Blackjack")
            return "b"
        elif self.player_score > 21:
            print("Bust!!!")
            return "l"
        elif self.stand_flag == True:
            if self.dealer_score > 21:
                print("Player Wins!")
                return "w"
            elif self.player_score > self.dealer_score:
                print("Player Wins!")
                return "w"
            else:
                print("Dealer wins")
                return "l"


    # Set up new game
    def new_game_setup(self):
        self.player_account = int(input("Enter int amount of player money: "))

    # recursive method that makes dealer hit until he is at 17 or more
    def dealer_hit(self, dealer_score):
        self.dealer_score = dealer_score

        self.print_result("d", self.dealer_cards, dealer_score, True)

        if dealer_score >=17:
            return dealer_score
        else:
            return self.dealer_hit(self.dealer([self.deck[self.draw()]]))

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
    def new_round_setup(self):
        bet = self.place_bet(self.player_account)

        p_score = self.player([self.deck[self.draw()],self.deck[self.draw()]])
        d_score = self.dealer([self.deck[self.draw()],self.deck[self.draw()]])
        
        self.print_result("p", self.player_cards, p_score)
        self.print_result("d", self.dealer_cards, d_score)

        return bet

    # Method that displays what cards the player currently has
    # Adds the total score of the cards
    def player(self, new_cards):
        self.player_cards += new_cards
        
        score = self.score(self.player_cards)

        return score

    # Method that will print the cards that the dealer has
    # Adds the total score of the cards
    def dealer(self, new_cards):
        self.dealer_cards += new_cards
        
        score = self.score(self.dealer_cards)
        
        return score

    def score(self, cards):
        self.cards = cards
        score = 0
        
        for card_points in self.cards:
            score += card_points[1]
                
        return score
    
    # Print the current cards depending on the dealer 
    def print_result(self, who, cards, print_score, show_dealer_cards=False):
        self.who = who
        self.cards = cards
        self.print_score = print_score
        self.show_dealer_cards = show_dealer_cards
        
        if self.who == "p":
            print("Player Cards:")
            for card in self.cards:
                print(card[0])
            print(f"Player Score: {self.print_score}")
            print("\n")
        elif self.who == "d" and show_dealer_cards == False:
            print(f"Dealer Card:\n{self.cards[0][0]}")
            print(f"Dealer Score: {self.cards[0][1]}")
            print("\n")
        elif self.who == "d" and show_dealer_cards == True:
            print("Dealer Cards:")
            for card in self.cards:
                print(card[0])
            print(f"Dealer Score: {self.print_score}")
            print("\n")
    
    # Place a bet taking the money from the players account
    def place_bet(self, account):
        self.account = account
        self.bet = 0

        if self.account - self.bet >= 0:
            self.account -= self.bet
            return self.bet
        else:
            return "Not enough money in the account"

    # Handle payouts of bets and money lost
    def payout(self, bet, action):
        self.bet = bet
        self.action = action

        if action == "b":
            self.player_account += (self.bet * 2.5)
            self.round_end = True
        elif action == "w":
            self.player_account += (self.bet * 2)
            self.round_end = True
        elif action == "l":
            self.player_account -= self.bet
            self.round_end = True
        print(self.player_account)
    def __str__(self):
        return self.deck[0][0]

b = Blackjack("Bob")
