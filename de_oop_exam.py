"""
This is AltSchool of Data / Data Engineering Object Oriented Examination
The goal of this assignment is to assess our understanding of object-oriented programming
(OOP) concepts in Python

The assignment will test our proficiency in defining classes, utilizing class attributes and
methods,and handling time-related functionalities.
"""
from datetime import datetime

class Expense():
    '''
    Represents an individual financial expense.
    '''

    def __init__(self, id, title, amount, created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        
        self.id = id
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.updated_at = None

    def update(self, new_title, new_amount):
        self.title = new_title
        self.amount = new_amount
        self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def to_dict(self):
        new_dict = {}
        new_dict[self.id] = [self.title, self.amount,
                           self.created_at, self.updated_at]
        return new_dict
    


# Defining neew expense
my_expense = Expense(id=1,title='transport',amount=2500)

print(my_expense.to_dict())

my_expense.update('Electricity', 4000)

print(my_expense.to_dict())