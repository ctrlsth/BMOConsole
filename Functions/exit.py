def exit():
    global program

    # ALGORITMA
    if <fungsi login>:
        save_ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        while not cekYN(save_ans):
            save_ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if save_ans == "Y":
  #          save()
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

