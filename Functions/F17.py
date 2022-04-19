def exit():
    # Keluar dari program
    # I.S. program sedang berjalan
    # F.S. program ditutup dan selesai
    
    out = input("Apakah anda ingin keluar dari program? (y/n)")
    if out == 'y' or out =='Y':                                                                    
        b=input("Apakah anda ingin melakukan penyimpanan file yang sudah diubah? (y/n)")
        if b == 'y' or b == 'Y':                                                                     
            save()                                                                        
            print("Menutup program...")                                                          
            time.sleep(1.5)
        elif b == 'n' or b == 'N':
            print("Menutup program")
            time.sleep(1.5)
        else:
            print("Masukan tidak valid! (Y/N/y/n)")
            exit()
        
        time.sleep(3)
        os.system('cls')
        sys.exit()
    elif out == 'n' or out == 'N':
        if role == 'admin':
            menu_admin()
        else:
            menu_user()
    else:
        print("Masukan tidak valid! (Y/N/y/n)")               
        exit()

