# F07 - Listing Game di toko

skema = input('Skema sorting: ')

y = copy(datagame)
x = length(datagame)
if skema == 'tahun-' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if (y[j][3]) < (y[j+1][3]) :
                y[j], y[j+1] = y[j+1], y[j]
    for i in y :
        print(i)
elif skema == 'tahun+' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if (y[j][3]) > (y[j+1][3]) :
                y[j], y[j+1] = y[j+1], y[j]
    for i in y :
        print(i)
elif skema == 'harga+' :
    for i in range(x-1):
        for j in range(0,x-i-1):
            if (y[j][4]) > (y[j+1][4]) :
                y[j], y[j+1] = y[j+1], y[j]
    for i in y :
        print(i)
elif skema == 'harga-' :  
    for i in range(x-1):
        for j in range(0,x-i-1):
            if (y[j][4]) < (y[j+1][4]) :
                y[j], y[j+1] = y[j+1], y[j]
    for i in y :
        print(i)
elif skema == '':
    for i in range(x-1):
        for j in range(0,x-i-1):
            if (y[j][0][4]) < (y[j+1][0][4]) :
                y[j], y[j+1] = y[j], y[j+1]
            elif (y[j][0][4]) > (y[j+1][0][4]):
                y[j], y[j+1] = y[j+1], y[j]
            else:
                if (y[j][0][5]) < (y[j+1][0][5]) :
                    y[j], y[j+1] = y[j], y[j+1]
                elif (y[j][0][5]) > (y[j+1][0][5]):
                    y[j], y[j+1] = y[j+1], y[j]
                else:
                    if (y[j][0][6]) < (y[j+1][0][6]) :
                        y[j], y[j+1] = y[j], y[j+1]
                    elif (y[j][0][6]) > (y[j+1][0][6]):
                        y[j], y[j+1] = y[j+1], y[j]
                    else:
                        y[j], y[j+1] = y[j], y[j+1]
    for i in y :
        print(i)
else:
    print("Skema sorting tidak valid")
        
