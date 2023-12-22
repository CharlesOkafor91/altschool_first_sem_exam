"""
This is AltSchool of Data / Data Engineering Object Oriented Examination
The goal of this assignment is to assess our understanding of object-oriented programming
(OOP) concepts in Python

The assignment will test our proficiency in defining classes, utilizing class attributes and
methods,and handling time-related functionalities.
"""
from datetime import datetime
import uuid

# Creating an Expense class

class Expense():
    '''
    Represents an individual financial expense.
    '''

    def __init__(self, title: str, amount: float):
        
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.updated_at = None

    def update(self, new_title=None, new_amount=None):
        # updating title if provideed
        if new_title is not None:
            self.title = new_title
        
        # updating amount if provided
        if new_amount is not None:
            self.amount = new_amount
        
        self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def to_dict(self):
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['title'] = self.title
        new_dict['amount'] = self.amount
        new_dict['created_at'] = self.created_at
        new_dict['updated_at'] = self.updated_at

        return new_dict
    

# Creating a neew ExpenseDB class

class ExpenseDB():
    '''
    Manages a collection of Expense objects.
    '''

    def __init__(self):
        self.expense = []

    def add_expense(self, expense):
        temp_data = [expense]
        temp_expense = [[item['id'], item['title'], item['amount'], item['created_at'], item['updated_at']] for item in temp_data]
        self.expense.append(temp_expense)

    def remove_expense(self, expense_id):
        self.expense = [sublist for sublist in self.expense if sublist[0] != expense_id]

    def get_expense_by_id(self, expense_id):
        result = None
        for row in self.expense:
            if row[0] == expense_id:
                result = row

        return result

    def get_expense_by_title(self, expense_title):
        result = None
        for row in self.expense:
            if row[1] == expense_title:
                result = row

        return result

    def to_dict(self):
        keys = ['id', 'title', 'amount', 'created_at', 'updated_at']
        expense_dicts = [dict(zip(keys, sublist)) for sublist in self.expense]

        return expense_dicts

# Defining neew expense and testing the nethods
my_expense = Expense(title='transport',amount=2500)
my_expense2 = Expense('TV', 300.25)
my_expense3 = Expense('Food', 10250)
my_expense4 = Expense('Furniture', 2525)
my_expense5 = Expense('Electricity', 5000)

print(my_expense)

print(my_expense.to_dict())

my_expense.update('transportation', 4000)

print(my_expense.to_dict())


my_db = ExpenseDB()

print(my_db.to_dict())

my_db.add_expense(my_expense.to_dict())
my_db.add_expense(my_expense2.to_dict())
my_db.add_expense(my_expense3.to_dict())
my_db.add_expense(my_expense4.to_dict())
my_db.add_expense(my_expense5.to_dict())

print(my_db.to_dict())

print(my_db.get_expense_by_title('TV'))