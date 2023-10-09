"""
Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True), the number of teams would be greater.

Enjoy :)
"""
from typing import List
from itertools import permutations, combinations

def friends_teams_helper(friends, team_size, current_team, all_teams, order_does_matter):
    if len(current_team) == team_size:
        if order_does_matter:
            all_teams.append(tuple(current_team))
        else:
            all_teams.append(sorted(current_team))
        return 
    
    for friend in friends:
        remaining_friends = friends.copy()
        remaining_friends.remove(friend)
        friends_teams_helper(remaining_friends, team_size, current_team + [friend], all_teams, order_does_matter)


def friends_teams(friends:List, team_size=2, order_does_matter=False):
    """using built-in methods"""
    """if order_does_matter:
        all_teams = list(permutations(friends, team_size))
    else:
        all_teams = list(combinations(friends, team_size))
    
    return all_teams"""
    all_teams = []
    friends_teams_helper(friends, team_size, [], all_teams, order_does_matter)
    return all_teams


friends = ['rob', 'bob']
print(friends_teams(friends, team_size=2, order_does_matter=True))