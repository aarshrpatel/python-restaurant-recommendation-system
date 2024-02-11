# Copyright 2024 Aarsh Patel
from restaurantData import *
from welcome import *

print_welcome()

print("What type of food would you like to eat?")
print("Type the beginning of that food type and press 'Enter' to search for restaurants.")
type_of_food = input()

for type in types:
    if type_of_food is type[:len(type_of_food)]:
        print("Here are the restaurants we found for " + type + " food:")
        for restaurant in restaurant_data:
            if type in restaurant:
                print(restaurant[1] + " is rated " + restaurant[2] + " with a price rating of " + restaurant[3] + ".")
        print("Would you like to see another type of food?")