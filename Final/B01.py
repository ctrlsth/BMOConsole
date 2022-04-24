import rCSV as r

def cipher(password, encrypt=True):

    # Keyed Caesar Cipher
    cipheredword = [':', '<', '=', '>', '?', '0', '!', '(', '9', '"', '#', '$', '%', '&', "'", ')', '*', '+', ',', '-', '.', '/', '@', '1', '2', '3', '4', '5', '6', '7', '8', 'Y', 'U', 'K', 'D', 'A', 'S', 'P', 'R', 'O', 'H', 'E', 'Z', 'B', 'C', 'F', 'G', 'I', 'J', 'L', 'M', 'N', 'Q', 'T', 'V', 'W', 'X', '`', '[', ']', '^', '_', 'y', 'u', 'k', 'd', 'a', 's', 'p', 'r', 'o', 'h', 'e', 'z', 'b', 'c', 'f', 'g', 'i', 'j', 'l', 'm', 'n', 'q', 't', 'v', 'w', 'x']
    encryptpsw = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '<', '=', '>', '?', '@',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    ordlist = [0 for ord in range (r.length(password))]
    encryptedpwd = ""
    decryptedpwd = ""

    if encrypt:

        for i in range (r.length(password)):
            if 97 <= ord(password[i]) <= 122 :
                ordlist[i] += (ord(password[i]) - 35)
            elif 65 <= ord(password[i]) <= 90 :
                ordlist[i] += (ord(password[i]) - 34)
            elif 33 <= ord(password[i]) <= 57 :
                ordlist[i] += (ord(password[i]) - 33)

        for j in range (r.length(ordlist)):
            encryptedpwd += cipheredword[ordlist[j]]
            
        return encryptedpwd
        
    else:

        for i in range(r.length(password)):
            for j in range(r.length(cipheredword)):
                if password[i] == cipheredword[j]:
                    decryptedpwd += encryptpsw[j]
            
        return decryptedpwd


# print("Encrypt: neelyak")
# encrypted = cipher("neelyak")
# print(encrypted)
# print()
# print("Decrypt :", encrypted)
# print(cipher(encrypted, False))
