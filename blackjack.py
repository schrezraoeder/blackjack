# super basic review of OOP in Python 

from random import shuffle 

class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit: str, value: str):
        self.suit = suit # should be one of ["Diamonds", "Spades", "Hearts", "Clubs"] 
        self.value = value # should be one of ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    
    # Returns the suit of the card.
    def suit(self) -> str:
        return self.suit 
    
    # Returns the value of the card.
    def value(self) -> str:
        return self.value 
      
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
      

class Deck:
    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
        SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
        VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.deck = [(suit, value) for suit in SUITS for value in VALUES]
        map_values_sense = {"Two": 0, "Three":1, "Four":2, "Five":3, "Six":4, "Seven":5, "Eight":6, "Nine":7, "Ten":8, \ 
                            "Jack":9, "Queen":10, "King":11, "Ace":12}
        self.shuffle(self.deck) # in place; uses python built-in `shuffle` from `random` `import`ed above 
    
    # Returns the number of Cards in the Deck
    def size(self) -> int:
        return len(self.deck) 
    
    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None: # to me it seems like horrible 'form' to use the same name as a built-in, absolutely atrocious, i never do this!
        shuffle(self.deck)  # in place; uses python built-in `shuffle` from `random` `import`ed above  
    
    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card: 
        return self.deck[-1] 
    
    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        card = self.deck.pop() 
        return card 
    
    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        if len(self.deck) >= 52: # presumably the above comment means *inclusively* when it says "more than" 
            raise Exception('deck already full') 
        else:
            self.deck.append(card) # let's see is a deck of cards a stack? idk, i don't play cards...  
    
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        for card in self.cards:
            print (card) 
      
    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        self.deck = [(suit, value) for suit in SUITS for value in VALUES]
        self.shuffle(self.deck) 




