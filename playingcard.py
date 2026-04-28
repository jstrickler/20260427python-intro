class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # replaced with PROPERTY, no longer METHOD
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a str")

    def __str__(self):  # str(obj)
        return f"{self.rank}-{self.suit}"


    def __repr__(self): # repr(obj)
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    pc1 = PlayingCard('8', 'Diamonds')
    print(pc1)  # str()
    print(f"{pc1 = }")  # repr
    print(f"{pc1.rank = }")
    print(f"{pc1.suit = }")
    pc1.rank = '10'
    print(f"{pc1.rank = }")
    

