# write your code here
from datetime import datetime


class Bot:
    birth_year = datetime.now().year

    def __init__(self, name):
        self.name = name

    def i_am(self):
        print(f'Hello! My name is {self.name}.'
              f'\nI was created in {self.birth_year}.')


my_bot = Bot('FAR14')
my_bot.i_am()
