import random
from playingcard import PlayingCard

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamond Hearts Spades'.split()


    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return [str(c) for c in self._cards]

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}/{len(self.cards)}"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"
    
    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1 = }")
    print(f"{d2 = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        print(d1.draw())
    print(d1)
    print(d2)
    print(f"{d1.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
    
    


