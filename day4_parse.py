"""
In this Bite you will work with a list of names.

1. Write a function that accepts a list of names and title cases them and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

You can assume that the names in the list are single strings composed of two words: one given name and one surname.
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    title_cased_names = []
    seen_names = set() #keeps track of seen names

    for name in names:
        title_cased_name = name.title()
        if title_cased_name not in seen_names:
            seen_names.add(title_cased_name)
            title_cased_names.append(title_cased_name)
    return title_cased_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_names = sorted(names, key=lambda x: x.split()[-1], reverse=True)
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest_name = min(names, key=lambda x: len(x.split()[0]))
    return shortest_name


print(dedup_and_title_case_names(names=NAMES))
print(sort_by_surname_desc(names=NAMES))
print(shortest_first_name(names=NAMES))