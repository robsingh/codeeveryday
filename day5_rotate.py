"""
Write a function that rotates characters in a string in either direction:

- If n is positive, move n characters from beginning to end, e.g.: rotate('hello', 2) would return "llohe".

- If n is negative, move the last n characters to the start of the string, e.g.: rotate('hello', -2) would return "lohel".

"""

def rotate(names,n):
    if n > 0:
        n = n % len(names)
        final_string = names[n:] + names[:n]
        print(final_string)
    elif n < 0:
        n = abs(n) % len(names)
        final_string = names[-n:] + names[:-n]
        print(final_string)
    else:
        print(names)

names = 'hello'
n = -2

(rotate(names, n))