# write your code here
from datetime import datetime


class Bot:
    birth_year = datetime.now().year

    def __init__(self, name):
        self.name = name

    def i_am(self):
        print(f'Hello! My name is {self.name}.'
              f'\nI was created in {self.birth_year}.')

    def ask_for_name(self):
        name = input('Please, remind me your name.\n')
        print(f'What a great name you have, {name}!')

    def guess_age(self):
        print('Let me guess your age.\nSay me remainders of dividing your age by 3, 5 and 7.')
        remainder3 = int(input())
        remainder5 = int(input())
        remainder7 = int(input())
        age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
        print(f"Your age is {age}; that's a good time to start programming!")


my_bot = Bot('FAR14')
my_bot.i_am()
my_bot.ask_for_name()
my_bot.guess_age()
