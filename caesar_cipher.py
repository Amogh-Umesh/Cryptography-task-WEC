def caesar_decrypt(text: str, shift):
    if(shift>26):
        shift = shift%26
    dtext = ''
    for i in text:
        if not (64<ord(i)<91 or 96<ord(i)<123):
            dtext += i
        else:
            a = ord(i) - shift
            if(i.isupper()):
                if(a<65):
                    a = 91 - 65 + a
            else:
                if(a<97):
                    a = 123 - 97 + a

            dtext += (chr(a))
    return dtext

def brute_force(text: str):
    for a in range(1, 25):
        print(caesar_decrypt(text, a))
        print('\n')

print(caesar_decrypt('PDA JATP YELDAN GAUOMQWNA EO PDA WHLDWXAPO SEPDKQP FOPXWODPSKQLONCXQNUJEOLXPWAEHMOUZOEQXXVKUJOWBLMWXPQUIOELPMYKYEHMOGOKYQXAXKYKDLYQZYLYHAWWBLMWXQYLWVWOY', 100))


brute_force('TM, DTZ KTZSI RJ😔. HTSLWFYX. YMNX NX YMJ JSILTFQ. TW NX NY?🤨')
