# F03 - Login
import rCSV_rev as r

# baca csv
# user.csv
data = []
f = open("C:/Users/Alka/user.csv","r")   
csv_name = "user"     
raw_lines = f.readlines()                   
f.close()                                       
csvtuple = r.todata(raw_lines, data, csv_name)      
header = csvtuple[0]

def login() :
    loginValid = False
    in_username = input("Masukan username: ")
    in_password = input("Masukan password: ")
   
    for i in data :
        if (in_username == i[1] and in_password == i[3]) :
            nama = i[2]
            loginData = i
            loginValid = True
    if loginValid :
        print("Halo", nama,  "! Selamat datang di “Binomo”.") 
    else : # if not loginValid :
        print("Password atau username salah atau tidak ditemukan.")
    # print(loginData) ngecek doang
    return loginValid, loginData

# loginValid, loginData = login() #<- untuk dipake di fungsi lain?
# print(loginData)
# bagian melakukan perintahnya belom, mungkin nanti di main programnya?? 

