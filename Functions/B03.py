def tictactoe():
    board = [["#", "#", "#"],
         ["#", "#", "#"],
         ["#", "#", "#"]]
    count = 0
    print("Tic Tac Toe!!")
    print('''Player 1 : "O" ; Player 2 : "X" ''')
    print("Format pengisian input baris lalu kolom")

    while count <= 9:
        print("Player 1 silahkan memasukkan baris dan kolom yang ingin dimainkan : ")
        horizon1 = int(input())
        vertikal1 = int(input())

        while (horizon1 > 3 or vertikal1 > 3):
            print("Inputan baris dan kolom salah")
            horizon1 = int(input())
            vertikal1 = int(input())
        
        while board[horizon1-1][vertikal1-1] != "#":
            print("Inputan yang diberikan sudah berisi")
            horizon1 = int(input())
            vertikal1 = int(input())
            if horizon1 > 3 or vertikal1 > 3:
                while (horizon1 > 3 or vertikal1 > 3):
                    print("Inputan baris dan kolom salah")
                    horizon1 = int(input())
                    vertikal1 = int(input())

        board[horizon1-1][vertikal1-1] = "O"
        count += 1

        for i in range(3):
            for j in range(3):
                print(board[i][j], end='')
            print()


        if count >= 5:
            if board[0][0] == "O" and board[0][1] == "O" and board[0][1] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                print("Player 1 Menang!!!")
                break
            elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                print("Player 2 Menang!!!")
                break
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                print("Player 2 Menang!!!")
                break
        if count == 9:
            print("------Hasil Seri------")
            break

        
        print("Player 2 silahkan memasukkan baris dan kolom yang ingin dimainkan : ")
        horizon2 = int(input())
        vertikal2 = int(input())

        while horizon2 > 3 or vertikal2 > 3:
            print("Inputan baris dan kolom salah")
            horizon2 = int(input())
            vertikal2 = int(input())
        
        while board[horizon2-1][vertikal2-1] != "#":
            print("Inputan yang diberikan sudah berisi")
            horizon2 = int(input())
            vertikal2 = int(input())
            if horizon2 > 3 or vertikal2 > 3:
                while (horizon2 > 3 or vertikal2 > 3):
                    print("Inputan baris dan kolom salah")
                    horizon2 = int(input())
                    vertikal2 = int(input())

        board[horizon2-1][vertikal2-1] = "X"
        count += 1

        for i in range(3):
            for j in range(3):
                print(board[i][j], end='')
            print()

tictactoe()