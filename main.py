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
    for card_object in new_deck.all_cards:
        print(card_object)
    new_deck.shuffle()
    for card_object in new_deck.all_cards:
        print(card_object)
    my_card = new_deck.deal_one()
    print(f'my card is: {my_card}')
    
    player1 = Player('Niall')
    print(player1)
    player1.add_cards(my_card)
    print(player1)

if __name__ == '__main__':
    main()
