import numpy as np

def search_letter(matrix:list, key:str):
    for y in range(5):
        for x in range(5):
            if(matrix[y][x] == key):
                return (y, x)

def plain_fair_decode(text: str, key: str):
    matrix = ''.join(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    cipher_matrix = [[0 for i in range(5)] for j in range(5)]
    for a in alphabet:
        if a in alphabet:
            continue
        else:
            matrix += a
    for y in range(5):
        for x in range(5):
            cipher_matrix[y][x] = matrix[5*y + x]
    doublets = []
    cur = ''
    prev = ''
    count = 0
    ftext = text[0]
    ind = 1
    x_indices = []
    for i in range(1,len(text)):
        if text[i] == text[i-1] and ind%2 == 1:
            ftext += 'X' + text[i]
            x_indices.append(ind)
        else:
            ftext += text[i]
        ind += 1
    if len(ftext)%2 == 1:
        x_indices.append(len(ftext))
        ftext += 'X'

    for a in ftext:
        prev = cur
        cur = a
        count += 1
        if count == 2:
            if cur != prev:
                doublets.append(prev+cur)
                count = 0
                
            else:
                print('error')
    decrypted_string = ''
    for doublet in doublets:
        (y1, x1) = search_letter(cipher_matrix, doublet[0])
        (y2, x2) = search_letter(cipher_matrix, doublet[1])
        if y1 == y2:
            
            if x1 == 0:
                x1 =  4
            else:
                x1 -= 1
            if x2 == 0:
                x2 = 4
            else:
                x2 -= 1
                
            decrypted_string += cipher_matrix[y1][x1] + cipher_matrix[y2][x2]
        elif x1 == x2:
            if y1 == 0:
                y1 =  4
            else: 
                y1 -= 1
            if y2 == 0:
                y2 = 4
            else: 
                y2 -= 1
            
            decrypted_string += cipher_matrix[y1][x1] + cipher_matrix[y2][x2]
        else:
            decrypted_string += cipher_matrix[y1][x2] + cipher_matrix[y2][x1]
    final_string = ''
    
    for a in range(len(decrypted_string)):
        if a in x_indices:
            pass
        else:
            final_string += decrypted_string[a]
    return final_string


print(plain_fair_decode('STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC', 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))
