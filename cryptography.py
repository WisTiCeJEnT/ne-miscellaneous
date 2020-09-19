import string
Q = """
AUHC MVKFC V BYZUGC V IZMC CJ GUMBZYAZD UKUVM VC HZZGZB CJ GZ V
HCJJB PD CFZ VYJM KUCZ AZUBVMK CJ CFZ BYVWZ UMB OJY U IFVAZ V TJNAB MJC
ZMCZY OJY CFZ IUD IUH PUYYZB CJ GZ"""

A = {}

def replacing(underline = True):
    tmp = Q
    for k in A:
        tmp = tmp.replace(k, A[k])
    tmpp = ''
    if underline:
        for c in tmp:
            if c.isupper():
                tmpp += '_'
            else:
                tmpp += c
    
        print(tmpp)
    else:
        print(tmp)
def count():
    for c in string.ascii_uppercase:
        print(c, end = '  ')
    print()
    for c in string.ascii_uppercase:
        print(f'{Q.count(c):02}', end = ' ')
    print()