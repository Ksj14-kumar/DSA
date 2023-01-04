def dfs(players, eliminated, strengths):
    # base case: if there is only one player in the list who has not been eliminated, return a string with a single "1" character
    if len([p for p in players if p not in eliminated]) == 1:
        return "1"

    # split the players into two teams of equal size
    n = len(players)
    half = n // 2
    team1 = players[:half]
    team2 = players[half:]

    result = ""
    # for each possible combination of teams that Iron can choose
    for i in range(2):
        for j in range(2):
            # calculate the total strength of each team
            strength1 = sum([strengths[team1[k]] for k in range(half) if i & (1 << k)])
            strength2 = sum([strengths[team2[k]] for k in range(half) if j & (1 << k)])

            # determine the winning team
            if strength1 > strength2:
                winners = team1
                losers = team2
            elif strength2 > strength1:
                winners = team2
                losers = team1
            else:
                # if the teams have equal strength, choose the winning team based on Iron's preference
                winners = team1
                losers = team2

            # update the list of eliminated players and the strengths dictionary
            eliminated += losers
            for p in losers:
                strengths[p] = 0

            # recursively call dfs on the list of players in the winning team, excluding the eliminated players
            result += dfs([players[k] for k in range(n) if k in winners and k not in eliminated], eliminated, strengths)

            # remove the eliminated players from the list
            eliminated = eliminated[:-half]

    return result

# read in the input
n = int(input())
s = list(map(int, input().split()))

# initialize the strengths dictionary
strengths = {i: s[i] for i in range(n)}

# call dfs on the list of all player indices
result = dfs(list(range(n)), [], strengths)

# output the resulting string
print(result)
