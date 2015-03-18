




if __name__ == "__main__":

    from lib.deck import StandardDeck

    mydeck = StandardDeck()

    print mydeck.deck

    mydeck.cut(5)

    print mydeck.deck

    mydeck.shuffle()

    print mydeck.deck
