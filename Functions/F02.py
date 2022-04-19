# F02 - Register

import os; import sys; import math; import time; import argparse; import datetime ; import rCSV as r


#-----------------------F02--------------------------------
def validasi_username(username):
    valid = True
    for letter in username:
        if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_":
            valid = False
            break
    return valid
    
def register(): 
    #Menambahkan data user ke dalam database
    #I.S. data user terdefinisi
    #F.S. data user dimasukkan ke dalam database
    

    #Variabel Global
    global user
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
                password = input("Masukkan password: ")
                            
    # notUnik == False

    # Pembuatan id
    count = 0
    for i in range(r.length(user)):
         count += 1
    id_user = str(count + 1)
    
    
    # Data user baru ditambahkan ke dalam matriks data user
    register = [[id_user,username,name,password,"User", 0 ]]
    user += register
    save()

    print("Username {} telah berhasil register ke dalam Binomo.".format(username))  

    
