"""
Create a function that takes a username and checks for a valid user:

1. The username is in USERS

2. The user's account has not expired.

3. The user has the ADMIN role.

If those 3 conditions are met return SECRET.

If one of the conditions is not True, raise an appropriate exception:

- UserDoesNotExist

- UserAccessExpired

- UserNoPermission
"""
"""
This is not how I would do in the ideal world, but my response is based on the problem statement.
However, I'd love to incorporate few changes in this code to make it more efficient.
1. Instead of using list of dictionaries, I'd like to use a dictionary where keys are usernames. Username lookup is more efficient.
2. Once a user is found, the function could return immediately, instead of continuing to iterate over the remaining users.
3. I'd prefer to return some specific values rather than raising exceptions. Using exceptions for flow control can have some performance implications.

My 2 cents of suggestions/advice.
"""


def validate_users(USERS, username):
    for user_data in USERS:
        if user_data['username'] == username:
            if user_data['role'] == 'admin' and not user_data['expired']:
                return "SECRET"
            else:
                if user_data['role'] != 'admin':
                    raise ValueError("User does not have admin role")
                elif user_data['expired']:
                    raise ValueError("User access has expired")
                
    
    raise ValueError("User does not exist")

USERS = [{'username':'lamechef','expired':False, 'role': 'admin'},
         {'username': 'subbappa', 'expired': True, 'role': 'user'},
         {'username': 'chippendi', 'expired': True, 'role': 'user'}]

username = str(input("Enter the username: "))
try:
    result = validate_users(USERS, username)
    print(result)
except ValueError as e:
    print(f"Error: {e}")