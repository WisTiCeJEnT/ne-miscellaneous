num = {'m': 0, 'j': 1, 'k': 2, 'l': 3, 'u': 4, 'i': 5, 'o': 6, '7': 7, '8': 8, '9': 9}
inp = ""
while(inp.lower()!="stop"):
    for c in inp:
        print(num[c],end='')
    print()
    inp = input()
