def base64_encode(b64text):
    res = ''.join(format(ord(i), '08b') for i in b64text)
    if len(res)%6 != 0:
        print("Invalid b64 text")
        return -1
    temp = ''
    count = 0
    arr = []
    for i,a in enumerate(res):
        if count%6 == 0:
            if temp != '':
                arr.append(temp)
                temp = ''
        temp += a
        count += 1
    for i, a in enumerate(arr):
        t = int(a,2)
        if t<26:
            t += 65
        elif t<52:
            t+= 71
        elif t<62:
            t-=4
        elif t == 62:
            t = 43
        elif t == 63:
            t = 47
        arr[i] = ascii(t)
    dtext = ''.join(arr)
    return dtext

def base64_decode(b64text):
    btext = ''
    for i, a in enumerate(b64text):
        t = ord(a)
        if 64 < t < 95:
            t -= 65
            btext += "{0:06b}".format(t)
        elif 96<t<123:
            t-= 71
            btext += "{0:06b}".format(t)
        elif 47<t<58:
            t+=4
            btext += "{0:06b}".format(t)
        elif t == 43:
            t = 62
            btext += "{0:06b}".format(t)
        elif t == 47:
            t = 63
            btext += "{0:06b}".format(t)
    temp = ''
    count = 0
    dtext = ''
    for i,a in enumerate(btext):
        if count%8 == 0:
            if temp != '':
                dtext += chr(int(temp, 2))
                temp = ''
        if count == len(btext)-1:
            if len(temp)<6:
                while(len(temp)<6):
                    temp += '0'
            dtext += chr(int(temp, 2))
        temp += a
        count += 1

    return dtext


print(base64_decode('R3JlYXQgam9iLiBKdWxpdXMgQ2Flc2VyIHdhcyBib3JuIGluIHRoZSAxMDAgQkM6ClBEQSBKQVRQIFlFTERBTiBHQVVPTVFXTkEgRU8gUERBIFdITERXWEFQTyBTRVBES1FQIEYKT1BYV09EUFNLUUxPTkNYUU5VSkVPTFhQV0FFSE1PVVpPRVFYWFZLVUpPV0JMTVdYUFFVSU9FTFBNWUtZRUhNT0dPS1lRWEFYS1lLRExZUVpZTFlIQVdXQkxNV1hRWUxXVldPWQ'))

base_64_encode_table = {
'000000':	'A',
'000001':   'B'	,
'000010':	'C'	,
'000011':	'D'	,
'000100':	'E'	,
'000101':	'F'	,
'000110':	'G'	,
'000111':	'H'	,
'001000':	'I'	,
'001001':	'J'	,
'001010':	'K'	,
'001011':	'L'	,
'001100':	'M'	,
'001101':	'N'	,
'001110':	'O'	,
'001111':	'P'	,
'010000':	'Q',
'010001':	'R',
'010010':	'S',
'010011':	'T',
'010100':	'U'	,
'010101':	'V',
'010110':	'W',
'010111':	'X',
'011000':	'Y',
'011001':	'Z',
'011010':	'a',
'011011':	'b',
'011100':	'c',
'011101':	'd',
'011110':	'e'	,
'011111':	'f',
'100000':	'g',
'100001':	'h',
'100010':	'i',
'100011':	'j',
'100100':	'k',
'100101':	'l',
'100110':	'm',
'100111':	'n',
'101000':	'o',
'101001':	'p',
'101010':	'q',
'101011':	'r',
'101100':	's',
'101101':	't',
'101110':	'u',
'101111':	'v',
'110000':	'w',
'110001':	'x',
'110010':	'y',
'110011':	'z',
'110100':	'0',
'110101':	'1',
'110110':	'2',
'110111':	'3',
'111000':	'4',
'111001':	'5',
'111010':	'6',
'111011':	'7',
'111100':	'8',
'111101':	'9',
'111110':	'+',
'111111':	'/'
}
