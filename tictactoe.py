cell = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

def board():
    print("---------")
    print(f"| {cell[0]} {cell[1]} {cell[2]} |")  # 1;3  2;3  3;3
    print(f"| {cell[3]} {cell[4]} {cell[5]} |")  # 1;2  2;2  3;2
    print(f"| {cell[6]} {cell[7]} {cell[8]} |")  # 1;1  2;1  3;1
    print("---------")

i = 0

while True:
    coordinates = input("Enter the coordinates: ")
    if coordinates.isalpha():
        print("You should enter numbers!")
        continue
    else:
        y, x = coordinates.split()
        column = int(y) - 1
        row = 3 - int(x)
        index = (row * 3) + column
        if index <= 8:
            if 1 <= int(y) <= 3 and 1 <= int(x) <= 3:
                if cell[index] != " ":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    cell = list(cell)
                    if i % 2 == 0:
                        cell[index] = "X"
                        board()
                        cell = "".join(cell)
                        wins = [cell[:3], cell[3:6], cell[6:],
                                cell[0:7:3], cell[1:8:3], cell[2:9:3],
                                cell[0:9:4], cell[2:7:2]]
                        if "XXX" in wins:
                            print("X wins")
                            break
                        elif "XXX" not in wins and "OOO" not in wins and " " not in cell:
                            print("Draw")
                            break
                        i += 1
                        continue
                    else:
                        cell[index] = "O"
                        board()
                        cell = "".join(cell)
                        wins = [cell[:3], cell[3:6], cell[6:],
                                cell[0:7:3], cell[1:8:3], cell[2:9:3],
                                cell[0:9:4], cell[2:7:2]]
                        if "OOO" in wins:
                            print("O wins")
                            break
                        elif "XXX" not in wins and "OOO" not in wins and " " not in cell:
                            print("Draw")
                            break
                        i += 1
                        continue
            else:
                print("Coordinates should be from 1 to 3")
                continue
        else:
            print("Coordinates should be from 1 to 3")
            continue