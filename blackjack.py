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
        #self.deck = [(suit, value) for suit in SUITS for value in VALUES]
        # map_values_sense = {"Two": 0, "Three":1, "Four":2, "Five":3, "Six":4, "Seven":5, "Eight":6, "Nine":7, "Ten":8, \ 
        #                     "Jack":9, "Queen":10, "King":11, "Ace":12}
        #self.shuffle(self.deck) # in place; uses python built-in `shuffle` from `random` `import`ed above 
        self.reset() 

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

class Blackjack:
    # Creates a Blackjack game with a new Deck.
    def __init__(self):
        self.hand = None 
        self.deck = Deck() 
        self.deal_new_hand() # create a `self.hand` holding the hand of cards for duration of one game  
    
    # Computes the score of a hand. 
    # For examples of hands and scores as a number. 
    # 2,5 -> 7
    # 3, 10 -> 13
    # 5, King -> 15
    # 10, Ace -> 21
    # 10, 8, 4 -> Bust so return -1
    # 9, Jack, Ace -> 20 
    # If the Hand is a bust return -1 (because it always loses)
    def _get_score(self, hand: List[Card]) -> int:
        total = 0 
        count_aces = 0 
        for card in hand: 
            if card.value != 'Ace': 
                total += self.score_card(card) 
                
            else: 
                count_aces += 1 
        if count_aces: 
            if count_aces == 1: 
                if total + 11 <= 21: 
                    total += 11 
                else:
                    total += 1 
            else: # 2, 3, or 4 aces. Only possibly can score max 1 of them as an 11, the rest have to be 1s. 
                if count_aces == 2: 
                    if total + 12 <= 21:
                        total += 12 
                    else: 
                        total += 2 
                else: # count_aces is either 3 or 4 
                    total += (count_aces - 1) # only possibly max 1 ace will be scored as an 11 hence the minus 1 
                    if total + 11 <= 21:
                        total += 11
                    else: 
                        total += 1 
        return total  

    # return score of any card other than an Ace which is handled with a crap ton of ugly logic separately "aces sold separately"
    # "we don't deal with aces" 
    def score_card(self, card: Card) -> int: 

        scores_of_cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, \
                            'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King':10}

        suit = card.suit()
        return scores_of_cards[suit] 
  
    # Prints the current hand and score.
    # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
    # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
    def _print_current_hand(self) -> None:


    # The previous hand is discarded and shuffled back into the deck.
    # Should remove the top 2 cards from the current deck and 
    # Set those 2 cards as the "current hand". 
    # It should also print the current hand and score of that hand.
    # If less than 2 cards are in the deck, 
    # then print an error instructing the client to shuffle the deck.
    def deal_new_hand(self) -> None:
        if len(self.deck) < 2: 
            print ("Error: deck to skinny--reshuffle first!") 
        else: 
            if self.hand: 
                for each_card in self.hand: 
                    self.hand.remove(each_card) 
                    self.deck.append(each_card) 
                self.reshuffle() 
            else: 
                new_hand = self.deck[-2:] 
                self.deck = self.deck[:-2]
                self.hand = new_hand 
            print ("Current hand:")
            print (self.hand) 
            print (self._get_score(self.hand)) 


    
    # Deals one more card to the current hand and prints the hand and score.
    # If no cards remain in the deck, print an error.
    def hit(self) -> None: 
        if len(self.deck) < 1:
            print ("Error")
        else: 
            self.hand.append(self.deck[-1])
            self.deck = self.deck[:-1] 

    # Reshuffles all cards in the "current hand" and "discard pile"
    # and shuffles everything back into the Deck.
    def reshuffle(self) -> None:
