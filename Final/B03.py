
def tictactoe():
    print('''
     :+                                           
*%                                           
 %%                                          
 *%%                                         
  %%%        .%                              
   %%%%%%:   :%             %  .             
    %%%%%    :%:=%          % %%       :     
    %%%% %   :%=:%%  .%%%   % :%%    %%%     
   .%%%%%%=  .%# %%%%%%%    %  %%=  %%%.     
   :%+ %%%%   %%  %%%%.     %   %% %%%       
   .%#  %%%   %%  %%%#      %   .%%%%        
    %%%%%%%%. %% %  +%=     %   :%%%         
    .%%%%##%%:%%      #     %  %%#.%*        
     ....::#%%%%:.... .    .% :.    %        
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%- 
  .:=+########%%%##**++=*-:=%..              
           *  %%%%  %%%%%  -%                
   %%    %%%: %%%%%%%%%# % +%     +%%%       
   @%* %%%%-  %% #%%+    % #%    %%%%%.      
    %%%%%+    %% %%%%.  %% %%   %%%  .*      
   .%%%*      %% %%.%%=%%  %%  %%%  *%       
  #%% %%+     %% %%=-%%%   %%  %% *%%        
 +%    +%     %%  %%%%%%%  %%  %%%%#         
         %    %%   .   %%@ %%    .           
   ...::::... %%        =%%%%                
     .-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=-.   
              *%  .-=*%%%%%%%%%%%%%%%%%%%%%%%
              *%           :%%.     ..:::-:: 
     %%   .@%%=%           .%%%:             
     %%::%%%%*=%   +%%%     %%+%=+%%%*       
     .%%%%%.  -%  %%%%%%    %% .%%%%%-       
     +%%%:    -% %%%   @.   %%  %%%  *%      
    %%# %%-   :%%%%    *#   %% %%=%%  +%     
   #%    -%   :%%%     %%   %% %%  #%  %     
           :  .%%%    #%.   *%.%%   :% %     
               #%%*:%%%-    .%*%%    :%%     
               + %%%%@       %%*%%@%%%%@     
               =  .          %% @%%%%.  +    
               :                             
                                                                              
    ''')
    board = [["#", "#", "#"],
         ["#", "#", "#"],
         ["#", "#", "#"]]
    count = 0
    print("Tic Tac Toe!!")
    print('''Player 1 : "X" ; Player 2 : "O" ''')
    print("Format pengisian input baris lalu kolom")
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = '')
        print()

    while count <= 9:
        print("Player 1 silahkan memasukkan baris kemudian kolom yang ingin dimainkan : ")
        horizon1 = int(input())
        vertikal1 = int(input())

        while not(1<=horizon1<= 3 and 1<=vertikal1 <= 3):
            print("Inputan baris dan kolom salah")
            horizon1 = int(input())
            vertikal1 = int(input())
        
        while board[horizon1-1][vertikal1-1] != "#":
            print("Inputan yang diberikan sudah berisi")
            horizon1 = int(input())
            vertikal1 = int(input())
            if horizon1 > 3 or vertikal1 > 3:
                while not(1<=horizon1<= 3 and 1<=vertikal1 <= 3):
                    print("Inputan baris dan kolom salah")
                    horizon1 = int(input())
                    vertikal1 = int(input())


        board[horizon1-1][vertikal1-1] = "X"
        count += 1

        print("------------------------------------ ")
        for i in range(3):
            for j in range(3):
                print(board[i][j], end='') 
            print()

        if win(count, board) == True:
            break

        print("Player 2 silahkan memasukkan baris kemudian kolom yang ingin dimainkan : ")
        horizon2 = int(input())
        vertikal2 = int(input())

        while not(1<=horizon2<= 3 and 1<=vertikal2 <= 3):
            print("Inputan baris dan kolom salah")
            horizon2 = int(input())
            vertikal2 = int(input())
        
        while board[horizon2-1][vertikal2-1] != "#":
            print("Inputan yang diberikan sudah berisi")
            horizon2 = int(input())
            vertikal2 = int(input())
            if horizon2 > 3 or vertikal2 > 3:
                while not(1<= horizon2 <= 3 and 1<= vertikal2 <= 3):
                    print("Inputan baris dan kolom salah")
                    horizon2 = int(input())
                    vertikal2 = int(input())

        board[horizon2-1][vertikal2-1] = "O"
        count += 1
        
        print("------------------------------------ ")
        for i in range(3):
            for j in range(3):
                print(board[i][j], end='')
            print()
         
        if win(count, board) == True:
            break
    return


def win(count, board):
    flag = False
    if count >= 5:
            if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                print("Player 2 menang !!!")
                flag = True
            elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                print("Player 1 menang !!!")
                flag = True
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                print("Player 1 menang !!!")
                flag = True
    if count == 9:
        print("----------------Hasil Seri-----------------")
        flag = True
        
    return flag

    
tictactoe()