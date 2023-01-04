def can_win(s):
    # base case: if there is only one player left, they can win
    if len(s) == 1:
        return True
    # split the players into two teams
    half = len(s) // 2
    team1 = s[:half]
    team2 = s[half:]
    # check the sum of the strengths of the two teams
    if sum(team1) == sum(team2):
        # if the sums are equal, any player on the stronger team can win
        return any(can_win(team1), can_win(team2))
    elif sum(team1) > sum(team2):
        # if team1 is stronger, all the players on team2 cannot win
        return can_win(team1)
    else:
        # if team2 is stronger, all the players on team1 cannot win
        return can_win(team2)

# read in the input
n = int(input())
s = list(map(int, input().split()))

# create a list of 0s and 1s, where 1s represent players who can win


winners = [1 if can_win([s[i]]) else 0 for i in range(n)]

# print the binary string
print("".join(map(str, winners)))
