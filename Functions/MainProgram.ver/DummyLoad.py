import rCSV as r

def game(header_data, csv_data):
    f = open("CSV/game.csv","r")
    raw_lines = f.readlines()
    f.close()

    csv_name = "game"

    # print("raw_lines / rawcsv")
    # print(raw_lines1)
    # print(raw_lines2)

    r.todata(raw_lines, header_data, csv_data, csv_name)

    return

def user(header_data, csv_data):
    f = open("CSV/user.csv","r")
    raw_lines = f.readlines()
    f.close()

    csv_name = "user"

    # print("raw_lines / rawcsv")
    # print(raw_lines1)
    # print(raw_lines2)

    r.todata(raw_lines, header_data, csv_data, csv_name)

    return

def kepemilikan(header_data, csv_data):
    f = open("CSV/kepemilikan.csv","r")
    raw_lines = f.readlines()
    f.close()

    csv_name = "kepemilikan"

    # print("raw_lines / rawcsv")
    # print(raw_lines1)
    # print(raw_lines2)

    r.todata(raw_lines, header_data, csv_data, csv_name)

    return

def riwayat(header_data, csv_data):
    f = open("CSV/riwayat.csv","r")
    raw_lines = f.readlines()
    f.close()

    csv_name = "riwayat"

    # print("raw_lines / rawcsv")
    # print(raw_lines1)
    # print(raw_lines2)

    r.todata(raw_lines, header_data, csv_data, csv_name)

    return
