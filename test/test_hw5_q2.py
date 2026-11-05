import hw5
import random

# Testing Card Innit
def test_card_init():
    # Creating card an object of the class Card
    card = hw5.Card("Diamonds", "A")

    # Testing whether Card's initialized instatialized card's suit and value:
    assert card.suit == "Diamonds"
    assert card.value == "A"

# Testing Deck
def test_deck_init():
    # Creating deck object which contains card objects
    deck = hw5.Deck()

    # All suits and values
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Creating a set (order does not matter) of tuples with all possible cards in the deck
    expected = {(suit, value) for suit in suits for value in values}
    # Actual set of cards in the deck object
    actual = {(card.suit, card.value) for card in deck.cards}

    # We test that there are a total of 52 card objects in the deck object
    assert len(deck.cards) == 52
    # We test that all of the card objects in the deck object are in fact card objects
    assert all(isinstance(card, hw5.Card) for card in deck.cards)
    # And lastly we test that the deck object houses exactly all the possible cards with suits
    # and value combination (expected is coded to take all combinations of suits and values)
    assert actual == expected

def test_deck_shuffle():
    # Creating deck object:
    deck = hw5.Deck()
    # Making a copy of the deck prior to shuffling
    deck_prior_shuffle = deck.cards.copy()

    # Random state
    state = random.getstate()
    try:
        random.seed(5)
        deck.shuffle()
    finally:
        random.setstate(state)

    # Asserting that the shuffled deck is not the same as the unshuffled deck
    # Mathematically the chance that the random shuffle gave us the same deck
    # is 1/52!, so will almost never get the same ordering as is common knowledge
    assert deck.cards != deck_prior_shuffle
    # Asserting that the deck did not someone lose or gain any number of card objects
    assert len(deck.cards) == 52
    # Asserting that the deck preserves the same exact cards and the set of the deck prior
    # and post shuffling is the same
    assert set(deck.cards) == set(deck_prior_shuffle)

def test_draw_empty_deck(capsys):
    # Creating empty deck object:
    deck = hw5.Deck()
    deck.cards.clear()

    # Draw the last card in the deck
    result = deck.draw()

    # Asserting that the draw method returns None
    assert result is None
    # Asserting that there are no cards in the deck
    assert deck.cards == []
    # Asserting that the the deck is empty messages is empty
    assert capsys.readouterr().out == "the deck is empty.\n"

def test_draw(capsys):
    # Creating deck object:
    deck = hw5.Deck()

    # Last card in the deck:
    last_card = deck.cards[-1]

    # Draw the last card in the deck
    deck.draw()

    # We resort to physically extracting the print message
    output = capsys.readouterr().out

    # Asserting that the the last card in the deck's suit and value is printed
    assert output == f"{last_card.suit} {last_card.value}\n"
    # Asserting that that the deck now has 51 cards
    assert len(deck.cards) == 51
    # Asserting that the last card is no longer in the deck
    assert last_card not in deck.cards