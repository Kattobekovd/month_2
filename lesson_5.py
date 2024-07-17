#import random
from random import randint as generate_number
import utilities.calculator as calc
from utilities.templates import Person
from termcolor import cprint
import emoji
from decouple import config

#print(random.randint(1,10))
print(generate_number(1, 10))
print(calc.multiplication(2,5))

my_friend = Person("Bob", "30")
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config("DATABASE_URL"))
commented = config("COMMENTED", default=0, cast=int)
print(commented * 2)