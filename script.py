# Copyright 2024 Aarsh Patel
from restaurantData import *
from welcome import *

print_welcome()

type_of_food: str = input("What type of food would you like to eat?\n" + 
                        "Type the beginning of that food type and press 'Enter' to search for restaurants.\n")


for type in types:
    if type_of_food is type[:len(type_of_food)]:
        print("Here are the restaurants we found for " + type + " food:")
        for restaurant in restaurant_data:
            if type in restaurant:
                print(restaurant[1] + " is rated " + restaurant[2] + " with a price rating of " + restaurant[3] + ".")
        print("Would you like to see another type of food?")