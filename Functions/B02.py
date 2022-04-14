# B02 - Magic Conch Shell
import time

def kerangajaib():
    t = time.time()
    question = input("Apa pertanyaanmu? ")
    magicshell = int(str(t-int(t))[2:])%7

    if magicshell == 0:
        print("Iya.")
    elif magicshell == 1:
        print("Tidak.")
    elif magicshell == 2:
        print("Bisa Jadi.")
    elif magicshell == 3:
        print("Mungkin.")
    elif magicshell == 4:
        print("Tidak mungkin")
    elif magicshell == 5:
        print("Tentu.")
    else:
        print("YO NDA TAU")

kerangajaib()
