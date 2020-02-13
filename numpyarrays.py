import numpy as np


# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: Wacky Packages
# Mike Gotta, Sam Allen
# Last Modified: Nov 15, 2019
# ---------------------------------------------
# A brief overview of the program.
# ---------------------------------------------

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)


# Place the missing methods here.  Do not modify the code below or above.
    # ---------------------------------------------

    def read_series_information(self, filename):
        self.filename = filename
        self.wackypack = []

        file = open(filename, "r")
        for cards in file:
            cardlist = cards.strip().split(",")
            number = int(cardlist[0])
            description = cardlist[1]
            value = int(cardlist[2])
            self.wackypack += [WackyPackageCard(number, description, value)]
        file.close()

    # ---------------------------------------------

    def read_collection_information(self, file):
        self.file = file
        file = open(file, "r")
        for lines in file:
            cardlist = lines.split(",")
            description = cardlist[0].strip().split()
            new_description = []
            for item in description:
                new_description.append(item.strip())
            description = " ".join(new_description)
            for card in self.wackypack:
                if card.get_description().lower() == description.lower():
                    card.cards_owned += 1
        file.close()

    # ---------------------------------------------
    def collection_value(self):
        value = 0
        for card in self.wackypack:
            if card.get_cards_owned() > 0:
                value += card.get_cards_owned() * card.get_value()
        return value

    def determine_missing_information(self):
        value = 0
        missing_cards = 0
        for card in self.wackypack:
            if card.get_cards_owned() == 0:
                value += card.get_value()
                missing_cards += 1

        return missing_cards, value

    # ---------------------------------------------

    def __str__(self):
        answer = "My " + str(self.year) + " collection of " + self.manufacturer + " Wacky Packages\n"
        answer += "Number    Description                   Value     Owned\n"
        answer += "------    -----------                   -----     -----\n"
        for cards in self.wackypack:
            answer += str(cards) + "\n"
        return answer


# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number


# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    print("Number of missing cards =", number_of_missing_cards)
    print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))


# ---------------------------------------------

main()

