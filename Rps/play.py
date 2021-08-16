import Interactions, Moves, Outcomes, Player, MoveList

# Ask for how many players
print("Welcome to Rock Paper Scissors!")
continueGame = True

while continueGame:
    
    choice = int(input("Please choose a game mode: \n 1) Player vs Bot \n 2) Bot vs Bot \n 3) Quit"))
    
    if choice == 3:
        continueGame = False
        break
    
    interactions = Interactions.Interactions()
    outcomes = Outcomes.Outcomes()
    allMoves = MoveList.MoveList().getAllMoves()

    players = interactions.generatePlayers(bots=choice, n=2)
    print(players[0].name)
    interactions.askForNames(players)
    interactions.askForMoves(players, allMoves)

    # compute outcome and display result
    result = outcomes.getResultString(players[0], players[1])
    print(result)