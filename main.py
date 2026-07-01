cells=[1, 2, 3, 4, 5, 6, 7, 8, 9]


print(f" {cells[0]} | {cells[1]}  | {cells[2]} ")
print("___|____|___")
print(f" {cells[3]} | {cells[4]}  | {cells[5]} ")
print("___|____|___")
print(f" {cells[6]} | {cells[7]}  | {cells[8]} ")
print("   |    |   ")
player="X"
turn=0

combinations=[
    [0,1,2],
    [3,4,5],
    [6,7,8],

    [0,3,6],
    [1,4,7],
    [2,5,8],

    [0,4,8],
    [2,4,6],

]

running=True
while running:

    user_input = int(input("Enter a number 1-9: "))

    i=0
    while i<len(cells):

        if user_input==cells[i]:
            cells[i]=player
            # turn += 1
            if player=="X":
                player="O"
            else:
                player="X"

            

        i = i + 1


    print(f" {cells[0]} | {cells[1]}  | {cells[2]} ")
    print("___|____|___")
    print(f" {cells[3]} | {cells[4]}  | {cells[5]} ")
    print("___|____|___")
    print(f" {cells[6]} | {cells[7]}  | {cells[8]} ")
    print("   |    |   ")

    

    for combo in combinations:
        if cells[combo[0]]==cells[combo[1]]==cells[combo[2]]:
            print("we have a winner")
            restart=input("Would you like to play again(y/n)")
            if restart=="y":
                cells=[1, 2, 3, 4, 5, 6, 7, 8, 9]
                player="X"
                turn=0
            else:
                running=False
            break

