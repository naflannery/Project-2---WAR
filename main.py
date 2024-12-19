#Python Card Game : WAR
import random

suits = ('Clubs','Hearts','Spades','Diamonds')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,
        'Three':3,
        'Four':4,
        'Five':5,
        'Six':6,
        'Seven':7,
        'Eight':8,
        'Nine':9,
        'Ten':10,
        'Jack':11,
        'Queen':12,
         'King':13,
        'Ace':14}


class Card():
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit 
    
class Deck():
      
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        print('\n\nShuffeling the deck...')
        random.shuffle(self.all_cards)
        print('Deck is shuffled \n\n')

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    #pop(0) is used to deal a card, append can be used to add one card, extend can be used to add multiple cards
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        #multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        #single card
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

def main():
    new_deck = Deck()
    new_deck.shuffle()

    player_1 = Player('One')
    player_2 = Player('Two')

    for x in range(26):
        player_1.add_cards(new_deck.deal_one())
        player_2.add_cards(new_deck.deal_one())
    
    game_on = True
    round_number = 0

    #BEGINING OF GAME LOOP
    while game_on:
        round_number += 1
        print(f'Currently on round: {round_number}')

        if len(player_1.all_cards) == 0:
            print('Player One is out of catrds. Player Two has won the game!')
            game_on = False
            break

        if len(player_2.all_cards) == 0:
            print('Player Two is out of catrds. Player One has won the game!')
            game_on = False
            break

        #BEGIN NEW ROUND
        player_1_cards_on_table =[]
        player_1_cards_on_table.append(player_1.remove_one())

        player_2_cards_on_table =[]
        player_2_cards_on_table.append(player_2.remove_one())

        #BEGINING OF WAR LOOP  the war loop decides win or loss logic
        war_card_number = 5 #Change this number to set the losing hand size and the amount of cards drawn during war

        at_war = True
        while at_war:
            if player_1_cards_on_table[-1].value > player_2_cards_on_table[-1].value:
                player_1.add_cards(player_1_cards_on_table)
                player_1.add_cards(player_2_cards_on_table)
                at_war = False
            elif player_1_cards_on_table[-1].value < player_2_cards_on_table[-1].value:
                player_2.add_cards(player_1_cards_on_table)
                player_2.add_cards(player_2_cards_on_table)
                at_war = False
            else:
                print("At War!!!")
                if len(player_1.all_cards) < war_card_number:
                    print('Player One has insufficient cards for the war')
                    print('PLAYER TWO WINS!!!')
                    game_on =False
                    break
                elif len(player_2.all_cards) < war_card_number:
                    print('Player Two has insufficient cards for the war')
                    print('PLAYER ONE WINS!!!')
                    game_on =False
                    break
                else:
                    for num in range(war_card_number):
                        player_1_cards_on_table.append(player_1.remove_one())
                        player_2_cards_on_table.append(player_2.remove_one())
            

    

if __name__ == '__main__':
    main()
