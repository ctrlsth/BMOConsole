   
def exit():
    # Keluar dari program
    # I.S. program sedang berjalan
    # F.S. program ditutup dan selesai
                                                                 
    b = input("Apakah anda ingin melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if b == 'y' or b == 'Y':                                                                     
        return True                                                                       
    elif b == 'n' or b == 'N':
        return False
    else:
        print("Masukan tidak valid! (Y/N/y/n)")               
        exit()
