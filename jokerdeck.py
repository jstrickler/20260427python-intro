from carddeck import CardDeck
from playingcard import PlayingCard

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = PlayingCard(f'JOKER-{joker_number}', 'JOKER')
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    print(j)
    j.shuffle()
    print(f"{j.cards = }")
