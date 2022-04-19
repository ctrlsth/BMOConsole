def exit():
    # Keluar dari program
    # I.S. program sedang berjalan
    # F.S. program ditutup dan selesai

    # KAMUS LOKAL
    # save_ans : string

    # global variable
    global program
    # Function / Procedure
    # cekYN(jawaban : string) -> boolean
    # Mengecek input dari user lalu memberi koreksi, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. Input harus berlaku untuk Y atau N dalam huruf kecil maupun besar.

    # save()
    # Menyimpan data ke dalam file di folder yang diinputkan
    # I.S. user, game, riwayat, kepemilikan terdefinisi
    # F.S. file user, gadget, consumable, gadget_borrow_history, gadget_return_history, consumable_history, inventory_user tersimpan
    # ALGORITMA
    if login:
        save_ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        while not cekYN(save_ans):
            save_ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if save_ans == "Y":
            save()
    print()
    # Program berhenti
    program = False

def cekYN(string):
    # Mengecek input dari user lalu memberi koreksi, harus 'Y' atau 'N'
    # input -> string : string
    # output -> boolean
    
    # I.S. string terdefinisi
    # F.S. Input harus berlaku untuk Y atau N dalam huruf kecil maupun besar.

    # KAMUS LOKAL
    
    # ALGORITMA
    if (string == 'Y') or (string == 'N') or (string == 'y') or (string == 'n'):
        return True
    else:
        print("Input harus berlaku untuk Y atau N dalam huruf kecil maupun besar. ")
        print()
        return False

