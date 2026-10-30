###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

#
# 1.2)
# Create a method called "add_test"
# which takes two parameters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return 0.99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and increases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

# Patient class
class Patient:
    # Initialize class
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self.test_storage = {}
    
    # Stored in a dictionary
    def add_test(self, name: str, result: bool):
        self.test_storage[name] = result

    # Probability that the user has covid: 0.99 otherwise 0.05 + 0.1 * num for num the number of matchings from list match_list
    def has_covid(self) -> float:
        if "covid" in self.test_storage:
            return 0.99 if self.test_storage["covid"] else 0.01
        else:
            match_list = ['fever', 'cough', 'anosmia']
            leftover = 0.1 * sum(symptom in match_list for symptom in set(self.symptoms))
            return 0.05 + leftover


######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them



# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" of the card.
# The class should store both as attributes.

class Card:
    def __init__(self, suit,value):
        self.suit = suit
        self.value = value

card = Card("Spades","King")
    

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

import random

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]
        
        self.cards = [
            Card(suit, value)
            for suit in suits
            for value in values
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            print("the deck is empty.")
            return
        card = self.cards.pop()
        print(card.suit, card.value)
#manual test
#deck = Deck()

#for card in deck.cards:
   # print(card.value, "of", card.suit)
    
#deck.shuffle()
#deck.draw()

###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimeter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

import math
from abc import ABCMeta, abstractmethod


class PlaneFigure(metaclass=ABCMeta):

    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError

    @abstractmethod
    def compute_surface(self):
        return NotImplementedError


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        return self.base * self.h / 2


# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        return 2 * (self.a + self.b)

    def compute_surface(self):
        return self.a * self.b


# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

    def compute_surface(self):
        return math.pi * self.radius ** 2

