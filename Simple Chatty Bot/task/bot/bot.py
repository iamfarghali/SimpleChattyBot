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


my_bot = Bot('FAR14')
my_bot.i_am()
my_bot.ask_for_name()
