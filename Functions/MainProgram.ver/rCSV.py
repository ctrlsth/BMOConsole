# functions

def splits(string, delimiters):
# function : { Menghasilkan array dengan elemen string yang dipisahkan oleh suatu karakter (delimiters) }

# KAMUS LOKAL
# parameters
    # string, delimiters : str
# variables
    # array : array of str
    # word : str

# ALGORITMA
    array = []
    word = ""
    for char in string:
      if char not in delimiters:
        word += char
      else:
        array += [word]
        word = ""
    array += [word]

    return array


def length(array):
# function : { Menghasilkan panjang suatu array }

# KAMUS LOKAL
# parameters
    # array : array
# variables
    # sum : integer

# ALGORITMA
    sum = 0
    for i in array:
        sum += 1
    return sum


def copy(array):
# function : { Menghasilkan salinan dari suatu array }

# KAMUS LOKAL
# parameters
    # array : array
# variables
    # copy : array

# ALGORITMA
    copy = []
    for element in array:
        copy += [element]
  
    return copy


def convertValue(csvdata, csvfilename):
# function : { Mengubah elemen string yang berisikan hanya angka pada array menjadi integer }

# KAMUS LOKAL
# parameters
    # csvdata : array of datalines
    # csvfilename : str

# ALGORITMA
    for i in range (length(csvdata)):
      if csvfilename == "user":
        if (i == 0) or (i == 5):
          csvdata[i] = int(csvdata[i])

      elif csvfilename == "game":
        if (i == 3) or (i == 4) or (i == 5):
          csvdata[i] = int(csvdata[i])

      elif csvfilename == "riwayat":
        if (i == 2) or (i == 3) or (i == 4):
          csvdata[i] = int(csvdata[i]) 

      elif csvfilename == "kepemilikan":
        if (i == 1):
          csvdata[i] = int(csvdata[i]) 
    
    return csvdata


def dataonly(csv):
# function : { Memisahkan header dengan data dari csv dan mengembalikan data csv }

# KAMUS LOKAL
# parameters
    # csv : array of datalines
# variables
    # data : array of datalines

# ALGORITMA
    data = []
    
    for line in range (1, length(csv)):
      data += [csv[line]]
      
    return data


def discard(string, delimiters):
# function : { Menghasilkan string yang suatu karakter dalamnya telah disingkirkan }

# KAMUS LOKAL
# parameters
    # string, delimiters : str
# variables
    # word : str

# ALGORITMA
    word = ""
    for char in string:
        if char not in delimiters:
            word += char

    return word


def join(array, separateby=";"):
# function : { Menghasilkan string hasil penggabungan elemen-elemen array dan dipisahkan dengan suatu karakter }

# KAMUS LOKAL
# parameters
    # array : array
    # separateby : str
# variables
    # word : str

# ALGORITMA
    word = ""
    for i in range (length(array)):
      word += array[i]
      if i != (length(array)-1): 
        word += separateby
    
    return word


# todata(): fungsi buat ngubah csv jadi matrix (array of datalines) isinya value dalem csv
def todata(rawcsv, globalheader, globaldata, csv_name):
# { I.S. Data dan Header Terdefinisi; F.S. Data dan Header terisi }
# procedure : Convert csv into data that can be manipulated

# KAMUS LOKAL
# parameters
    # rawcsv : array of str
    # globalheader : array of str
    # globaldata : array
    # csv_name : str
# variables
    # counter : int
    # replaced : str
    # line2array : array of str
    # clean : array of str
    # tails : array of datalines

# ALGORITMA
    #1 Remove The \n in Every Line In The rawcsv (an array)
    counter = 0
    for line in rawcsv:
      replaced = discard(line, "\n")
      rawcsv[counter] = replaced
      counter += 1

    #2 Make An Array for Each Line
    counter = 0
    for line in rawcsv:
      line2array = splits(line, ";")
      rawcsv[counter] = line2array
      counter += 1

    #3 Assign The Header and The Data To A New Variable
    globalheader += rawcsv[0]
    tails = dataonly(rawcsv)

    #4 Change the number-only string into integer
    for line in tails:
      clean = convertValue(line, csv_name)
      globaldata += [clean]
    
    return


# modif(): modif data csv
def modif(globaldata, index, col, value):
# { I.S. globaldata terdefinisi , F.S. value dalam globaldata berubah }

# KAMUS LOKAL
    # parameters
    # globaldata : array
    # index, col : int
    # value : free (tergantung csv)

# ALGORITMA
    globaldata[index][col] = value

    return

# save(): menyimpan data ke csv
def saving(globalheader, globaldata):
# function : { Menghasilkan string yang berisikan header dan data dalam format csv }

# KAMUS LOKAL
# parameters
    # csvheader : array of str
    # globaldata : array
# variables
    # data2string, line2str, array2str : str

# ALGORITMA   
    #1 Make the header into str separated with ";" then add "\n" in the end
    data2string = join(globalheader) + "\n"

    #2.1 Changing the number value into str; Changing format into csv; Combine with header
    for line in globaldata:
      line2str = [str(elmt) for elmt in line] # bikin elemen array menjadi str
      data2string += join(line2str)
      data2string += "\n"

    return data2string


def findLongest(data, his=False):
# function : Menentukan string terpanjang untuk setiap kolom dalam game_data

# KAMUS LOKAL
# parameters
    # game_data : matrix
# variable
    # maxlen : array of int
    # str_data : matrix of str
    # str_element : array of str

# ALGORITMA
    maxleng = [7, 9, 16, 11, 5, 4]
    maxlenh = [7, 9, 5, 10]

    if not his:
        finish = 6
        maxlen = maxleng
    else:
        finish = 4
        maxlen = maxlenh

    str_data = []
    for dataline in data:
        str_element = []
        for i in range (finish):
            str_element += [str(dataline[i])]
        str_data += [str_element]
    
    for dataline in str_data:
        for i in range (1,finish):
            if length(dataline[i]) > maxlen[i]:
                maxlen[i] = length(dataline[i])

    return maxlen


def listDiv(lengtharray, finish, his, stock, title=True):

    if not his:
        titlelist = " DAFTAR GAME "
        lentitle = 13
        if stock:
            sum = 19
        else:
            sum = 16
    else:
        titlelist = " RIWAYAT "
        lentitle = 9
        sum = 13

    for k in range (finish):
        sum += lengtharray[k]

    if title:
        sum -= lentitle

        div = "=" * (sum // 2)
        print(div, end="")
        print(titlelist, end="")
        div = "=" * (sum - (sum // 2))
        print(div)

    else:
        div = "-" * sum
        print(div)

    return


def neatList(data, stock=True, his=False):
# { I.S. Data/List game terdefinisi; F.S. Data/List game ditampilkan ke layar }
# procedure: Menampilkan list game ke layar

# KAMUS LOKAL
# parameters
    # game_data : matrix
    # stock : boolean
# variables
    # header, str_element : array of str
    # lengtharray : array of int
    # finish, counter : int
    # combined, str_data : matrix of str
    # base, space, div : str

    headergame = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
    headerhis = ["ID Game", "Nama Game", "Harga", "Tahun Beli"]

    if not his:
        lengtharray = findLongest(data)
        header = headergame
        if stock:
            finish = 6
        else:
            finish = 5
    else:
        lengtharray = findLongest(data, True)
        header = headerhis
        finish = 4

    str_data = []
    for dataline in data:
        str_element = []
        for i in range (finish):
            str_element += [str(dataline[i])]
        str_data += [str_element]

    combined = [header]
    combined += str_data

    listDiv(lengtharray, finish, his, stock)
    listDiv(lengtharray, finish, his, stock, False)

    counter = 0
    for datalines in combined:
        base = "| "
        for j in range (finish):
            if length(datalines[j]) == lengtharray[j]:
                base += datalines[j]
            elif length(datalines[j]) < lengtharray[j]:
                base += datalines[j]
                space = " " * (lengtharray[j] - length(datalines[j]))
                base += space
            base += " | "
        
        print(base)

        if counter == 0 or counter == (length(combined)-1):
            listDiv(lengtharray, finish, his, stock, False)
        counter += 1

    return


# How To Open CSV File:

# ganti semua <tanda kurung gini> jadi yang kelian pengen
# Karena ini bentuknya komentar (#), biar ga ngapusin 1 1 (#)-nya, pake [CTRL+/] di codenya

# 1. AKSES FILE CSV
# import <NAMA FILE INI> as r                 # Buat Bisa Manggil Fuction dalem file (or module) rCSV.py
#                                             # How To Manggil: r.<function/procedure>
#                                             # Ganti <function/procedure> sesuai fungsi/procedure yang pengen digunain

# f = open("CSVs/<Nama File>.csv","r")        # Ngebuka file CSV
# raw_lines = f.readlines()                   # Baca file CSV per line
# f.close()                                   # Tutup file CSV

# csv_name = "<nama csvnya : user/game/kepemilikan/riwayat>"

# data = []                                           # Ntar diisi dari data csv secara otomatis stlh manggil fungsi yang dibawah ini
# csvtuple = r.todata(raw_lines, data, csv_name)      # ISinya bentuk tuple 2 elemen dimana tuple[0] isinya header dan tuple[1] isinya data dari csv
# header = csvtuple[0]                                # yaa isinya header csv

# incase gatau: kita manipulasi data pada variabel data

# ----------------
# print()                                             # ini aktifin kalo mau liat isi data
# print("Data")
# for i in data:
#     print(i)

# print()                                             # ini aktifin kalo mau liat isi header
# print("Header")
# print(header)
# ----------------



# 1.5 MODIF DATA CSV
# modif(data, <index>, <col>, <value>)                # Gimana cara kerjanya??? Liat di atas di prosedur modif()

# -----------------
# print()                                             # ini aktifin kalo mau liat isi data hasil modif
# print("Data")
# for i in data:
#     print(i)
# -----------------

# 2. NYIMPEN DATA KE CSV (Tinggal Aktifin aja)
# datastring = r.saving(header, data, csv_name)

# ----------------------
# print()                                             # Kalo mau liat formatnya sblm masuk csv kek mana
# print("Data String")
# print(datastring)
# ----------------------

# g = open("CSVs/<Nama File>.csv", "w")               # Ini sisanya overwrite isi filenya
# g.write(datastring)
# g.close()
