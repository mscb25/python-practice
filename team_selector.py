import random


players = ["Sabrina", "Maddie", "Teddy", "Tommy", "Chelsea", "Erin", "Mack",
           "Kassie", "Brandon", "Henry", "Dominic B", "Dominic K", "Anthony",
           "Kevin", "Teal", "Anna", "Miller", "Caspien", "Lindsey", "Gloria"]

print("Welcome to Team/Player Allocator!")

while True:
    random.shuffle(players)

    resp = input("Is it a team or individual sport? \ Type team or individual: ")
    if resp == "team":
        team1 = players[:len(players)//2]
        team2 = players[len(players)//2:]



        print("Team 1 captain: " + random.choice(team1))
    
        print("Team 1:")
        for player in team1:
            print(player)


    
        print("/n Team 2 captain: " + random.choice (team2))

        print("Team 2:")
        for player in team2:
            print(player)

    else:
        for i in range(0, 20, 2):
            print(players[i] + " vs " + players[i + 1])
            start = random.randrange(i, i + 2)
            print(players[start] + " starts")

    response = input("Pick again? Type y or n: ")
    if response == "n":
        break
