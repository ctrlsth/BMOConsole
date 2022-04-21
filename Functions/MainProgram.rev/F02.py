# F02 - Register
import rCSV as r

#-----------------------F02--------------------------------
def validasi_username(username):
    valid = True
    for i in range (r.length(username)) :
        if ((ord(username[i])==45) or (ord(username[i])==95) or (65<=ord(username[i])<=90) or (97<=ord(username[i])<=122) or (48<=ord(username[i])<=57)):
            valid = True
        else :
            valid = False
            break
    return valid
    
def register(user): 
    #Menambahkan data user ke dalam database
    #I.S. data user terdefinisi
    #F.S. data user dimasukkan ke dalam database
    
    #KAMUS lOKAL
    #name,username,password : str
    #notUnik : boolean 
    
    #ALGORITMA
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    while not validasi_username(username):
        print("Username anda tidak valid, silahkan coba lagi")
        username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    notUnik = True

    while notUnik:
        notUnik = False

        for i in range(r.length(user)):
            if user[i][1] == username:
                notUnik = True
                print()
                print("Username {} sudah terpakai, silakan menggunakan username lain.".format(username))
                print()
                name = input("Masukkan nama: ")
                username = input("Masukkan username: ")
                while not validasi_username(username):
                    print("Username anda tidak valid, silahkan coba lagi")
                    username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                            
    # notUnik == False

    # Pembuatan id
    count = 0
    for i in range(r.length(user)):
         count += 1
    id_user = str(count + 1)
    
    
    # Data user baru ditambahkan ke dalam matriks data user
    register = [[id_user, username, name, password, "user", 0]]
    user += register

    print("Username {} telah berhasil register ke dalam Binomo.".format(username))

    return