skema = input('Skema sorting: ')
        
x = length(datagame)
if skema == 'tahun-' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if int(datagame[j][3]) < int(datagame[j+1][3]) :
                datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
    for i in datagame :
        print(i)
elif skema == 'tahun+' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if int(datagame[j][3]) > int(datagame[j+1][3]) :
                datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
    for i in datagame :
        print(i)
elif skema == 'harga+' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if int(datagame[j][4]) > int(datagame[j+1][4]) :
                datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
    for i in datagame :
        print(i)
elif skema == 'harga-' :  
    for i in range(x-1):
        for j in range(0,x-i-1):
            if int(datagame[j][4]) < int(datagame[j+1][4]) :
                datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
    for i in datagame :
        print(i)
elif skema == '':
    for i in range(x-1):
        for j in range(0,x-i-1):
            if int(datagame[j][0][4]) < int(datagame[j+1][0][4]) :
                datagame[j], datagame[j+1] = datagame[j], datagame[j+1]
            elif int(datagame[j][0][4]) > int(datagame[j+1][0][4]):
                datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
            else:
                if int(datagame[j][0][5]) < int(datagame[j+1][0][5]) :
                    datagame[j], datagame[j+1] = datagame[j], datagame[j+1]
                elif int(datagame[j][0][5]) > int(datagame[j+1][0][5]):
                    datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
                else:
                    if int(datagame[j][0][6]) < int(datagame[j+1][0][6]) :
                        datagame[j], datagame[j+1] = datagame[j], datagame[j+1]
                    elif int(datagame[j][0][6]) > int(datagame[j+1][0][6]):
                        datagame[j], datagame[j+1] = datagame[j+1], datagame[j]
                    else:
                        datagame[j], datagame[j+1] = datagame[j], datagame[j+1]
    for i in datagame :
        print(i)
else:
    print("Skema sorting tidak valid")
        
