import os
import getpass
inp = input()
while(inp!="" and inp!="stap"):
    t = getpass.getpass(inp+': ')
    #print(os.environ[inp])
    os.system(f'export "{inp}"="{t}"')
    inp = input()

