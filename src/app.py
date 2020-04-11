#!/usr/bin/env python3
'''
Author: Mateusz Maly
Description: Blackjack game against computer
'''
class Blackjack:

    def __init__(self, player_name):
        self.player_name = player_name
    
    def __str__(self):
        return self.player_name

b = Blackjack("Bob")
print(b)
