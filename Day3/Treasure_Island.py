print("Welcome to teh Treasure Island!")
print("Your mission is to find the treasure")
cross_road = input("You are at crossroad, you wanna go Left(L) or Right(R)? ")
game_over = "Game Over!"
if cross_road == "L":
    lake = input("You reached a Lake, you wanna wait(W) or swim(S)? ")
    if lake == "W":
        print("You reached a cave and found 3 different colored doors,Red(R), Blue(B), Yellow(Y).\n")
        door = input("which door will you choose? ")
        if door == "Y":
            print("Congrats!!! you won it all")
        else:
            print(game_over)
    else:
        print(game_over)
else:
    print(game_over)