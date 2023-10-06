"""
Write a function that receives one or more sequences. The sequences are already defined for you.

The function should return a table (list of strings) where the columns are the sequences (example below).

To keep it simple we work with equally sized sequences so you don't have to worry about handling a missing value 
(you should end up with a grid of 6 rows x n columns).

There are some Pythonic idioms you can use here, hint: think of pants ;)

Example call (look at the tests for more detail):

>>> generate_table(names, aliases)
['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder', 
 'Dante | Pythonista', 'Martin | Nerd', 'Rodolfo | Coder']
Bonus: use a generator to build up the table rows.
"""

from itertools import zip_longest

NAMES = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
ALIASES = ['Pythonista', 'Nerd', 'Coder', 'Pythonista', 'Nerd', 'Coder']

def generate_table(*sequences):
    # table = []
    # for row in zip_longest(*sequences, fillvalue=''):
    #     table.append(' | '.join(row))
    # return table

    """ Generator expression"""
    return (
        ' | '.join(row)
        for row in zip_longest(*sequences, fillvalue='')
    )


if __name__ == '__main__':
    table = generate_table(NAMES, ALIASES)
    print(list(table))

