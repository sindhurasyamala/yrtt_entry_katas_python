# Scenario
# Several people are standing in a row divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)
# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

# rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
# Explanation:
# The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.

# rowWeights([80])  ==>  return (80, 0)
# Explanation:
# The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.

def row_weights(arr):
    team1 = []
    team2 = []
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            team1.append(arr[i])
        else:
            team2.append(arr[i])
    print("Team1 =", team1)
    print("Team2= ", team2)
    for x in team1:
        sum1 = sum1 + x
    print("1st team total= ", sum1)
    for y in team2:
        sum2 = sum2 + y
    print("2nd team total = ", sum2)

row_weights([10,20,30,40,50])