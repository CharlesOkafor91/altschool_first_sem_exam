# altschool_first_sem_exam

## Altschool Data Engineering First Semester Exams

In this project, I created 2 classes:
1. **Expense**
2. **ExpenseDB**

#### Expense:

This class helps to instanciate an expense item with attributes:
- id: this is initialised using the [uuid library](https://www.npmjs.com/package/uuidv4)
- title: this is the name of thee expense added
- amount: total cost of the expense
- creeated_at: date and time the expense item was creeated
- updated_at: date and time the expense item was modified. This is initialised as **None**

Methods on this class includes:
- update: Updates the expense title and/or amount, and also update the updated_at timestamp which was initally None
- to_dict: This is to return a dictionary represeentation of the expense


#### ExpenseDB:

This class manages the collections of Expense instances or onjects. It creates of collection of expense items. Its attributes are:
- expense: this is a list containing all expense objects.

Methods on this class includes:
- add_expense: Add an expense to the self.expense list
- remove_expense: Remove an expense iteem by the id
- get_expense_by_id: Select and return an expense item by the id
- get_expense_by_title: Select and reeturn an expense item by the title
- to_dict: Returns a list of dictionaries representing expenses

> NB// `ExpenseDB` is **NOT** an inheritance class of the `Expeense` class. These 2 classes aree stand alone independent classes, however an instance or object of the `Expense` class can be used as an input iteem to the `ExpenseDB` class.
